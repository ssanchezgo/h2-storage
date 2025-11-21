#!/usr/bin/env python3
"""
Limpieza y Validación de Archivos de Notas
==========================================
Este script:
1. Detecta y elimina estructuras duplicadas en archivos .md
2. Extrae datos de los PDFs correspondientes para completar campos vacíos
3. Consolida la información en una versión limpia y completa
4. Genera respaldos antes de hacer cambios

Autor: ANH951 Project
Fecha: 2025-11-19
"""

import os
import re
import sys
import shutil
from pathlib import Path
from datetime import datetime
import PyPDF2
from collections import defaultdict

# ============================================================================
# DETECCIÓN Y LIMPIEZA DE DUPLICADOS
# ============================================================================

def detect_duplicate_sections(content):
    """
    Detecta secciones duplicadas en un archivo markdown.
    Retorna la mejor versión (la más completa).
    """
    # Dividir por títulos principales (# Title)
    sections = re.split(r'\n(?=#\s+[^#])', content)
    
    if len(sections) <= 1:
        return content, False
    
    print(f"  - Detectadas {len(sections)} secciones principales")
    
    # Analizar cada sección
    section_scores = []
    for i, section in enumerate(sections):
        # Calcular "completitud" de la sección
        score = 0
        
        # Penalizar "No especificado"
        no_especificado = len(re.findall(r'No especificado', section, re.IGNORECASE))
        score -= no_especificado * 2
        
        # Premiar datos numéricos
        numeros = len(re.findall(r'\d+\.?\d*\s*(?:mm|cm|m|kg|g|bar|°C|K|L|min|h|%)', section))
        score += numeros * 3
        
        # Premiar longitud de contenido útil
        lineas_con_contenido = [l for l in section.split('\n') if l.strip() and not l.startswith('#')]
        score += len(lineas_con_contenido)
        
        # Premiar presencia de secciones clave
        if re.search(r'##\s+\d+\.?\s*Puntos Clave', section):
            score += 10
        if re.search(r'##\s+\d+\.?\s*Características Técnicas', section):
            score += 10
        if re.search(r'##\s+\d+\.?\s*Transferencia de Calor', section):
            score += 10
        if re.search(r'##\s+\d+\.?\s*Conclusiones', section):
            score += 10
        
        section_scores.append((i, score, len(section)))
        print(f"    Sección {i+1}: score={score}, longitud={len(section)} chars")
    
    # Seleccionar la mejor sección
    best_section_idx = max(section_scores, key=lambda x: x[1])[0]
    best_section = sections[best_section_idx]
    
    has_duplicates = len(sections) > 1
    
    print(f"  ✓ Mejor sección: #{best_section_idx + 1}")
    
    return best_section, has_duplicates


def clean_markdown_structure(content):
    """
    Limpia estructuras problemáticas en el markdown.
    """
    # Eliminar múltiples líneas vacías consecutivas
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Eliminar secciones con "Ver contenido original más abajo"
    content = re.sub(r'Ver contenido original más abajo\s*\n?', '', content)
    
    # Limpiar espacios en blanco al final de líneas
    content = '\n'.join(line.rstrip() for line in content.split('\n'))
    
    return content


# ============================================================================
# EXTRACCIÓN DE DATOS DE PDFs
# ============================================================================

def find_corresponding_pdf(md_file, articulos_path):
    """
    Encuentra el PDF correspondiente a un archivo .md
    """
    # Estrategias de búsqueda
    base_name = md_file.stem
    
    # Extraer año del nombre
    year_match = re.search(r'(19|20)\d{2}', base_name)
    year = year_match.group(0) if year_match else None
    
    # Buscar por similitud de nombre
    pdf_files = list(articulos_path.glob("*.pdf"))
    
    best_match = None
    best_score = 0
    
    for pdf in pdf_files:
        score = 0
        pdf_name = pdf.stem.lower()
        md_name = base_name.lower()
        
        # Coincidencia de año
        if year and year in pdf_name:
            score += 10
        
        # Palabras clave comunes
        md_words = set(re.findall(r'\w{4,}', md_name))
        pdf_words = set(re.findall(r'\w{4,}', pdf_name))
        common_words = md_words & pdf_words
        score += len(common_words) * 5
        
        if score > best_score:
            best_score = score
            best_match = pdf
    
    return best_match if best_score > 10 else None


def extract_metadata_from_pdf(pdf_path):
    """
    Extrae metadatos y datos clave del PDF.
    """
    data = {}
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            # Extraer metadata
            if pdf_reader.metadata:
                metadata = pdf_reader.metadata
                if metadata.title:
                    data['title'] = metadata.title
                if metadata.author:
                    data['author'] = metadata.author
            
            # Extraer texto de primeras páginas
            text = ""
            for i in range(min(5, len(pdf_reader.pages))):
                text += pdf_reader.pages[i].extract_text() + "\n"
            
            # Extraer información específica
            data['text'] = text
            
            # DOI
            doi_match = re.search(r'doi[:\s]*(10\.\d{4,}/[^\s]+)', text, re.IGNORECASE)
            if doi_match:
                data['doi'] = doi_match.group(1).rstrip('.,')
            
            # Journal/Revista
            journal_patterns = [
                r'published in\s+([A-Z][^\n]{10,80})',
                r'journal[:\s]+([A-Z][^\n]{10,60})',
                r'International Journal of ([^\n]{10,60})',
            ]
            for pattern in journal_patterns:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    data['journal'] = match.group(1).strip()
                    break
            
            # Dimensiones del reactor
            dim_patterns = [
                r'diameter[:\s]*(\d+[\d.,]*)\s*(mm|cm)',
                r'length[:\s]*(\d+[\d.,]*)\s*(mm|cm)',
                r'volume[:\s]*(\d+[\d.,]*)\s*(L|liters?)',
            ]
            
            dimensions = []
            for pattern in dim_patterns:
                matches = re.findall(pattern, text, re.IGNORECASE)
                dimensions.extend([f"{m[0]} {m[1]}" for m in matches[:3]])
            
            if dimensions:
                data['dimensions'] = dimensions
            
            # Temperaturas
            temp_matches = re.findall(r'(\d+[\d.,]*)\s*[°]?[CK]\b', text)
            if temp_matches:
                data['temperatures'] = [t for t in temp_matches[:10]]
            
            # Presiones
            pressure_matches = re.findall(r'(\d+[\d.,]*)\s*(?:bar|MPa|Pa)\b', text)
            if pressure_matches:
                data['pressures'] = [p for p in pressure_matches[:10]]
            
            # Tipo de estudio (buscar palabras clave)
            if any(word in text.lower() for word in ['experimental', 'experiment', 'testing', 'prototype']):
                data['study_type'] = 'Experimental'
            elif any(word in text.lower() for word in ['numerical', 'simulation', 'cfd', 'modeling', 'comsol']):
                data['study_type'] = 'Simulación'
            elif any(word in text.lower() for word in ['review', 'state of the art', 'survey']):
                data['study_type'] = 'Review'
            
            # Escala
            if any(word in text.lower() for word in ['industrial scale', 'commercial', 'large-scale']):
                data['scale'] = 'Industrial'
            elif any(word in text.lower() for word in ['pilot', 'prototype']):
                data['scale'] = 'Piloto'
            elif any(word in text.lower() for word in ['laboratory', 'lab-scale', 'bench']):
                data['scale'] = 'Laboratorio'
            
    except Exception as e:
        print(f"    ⚠ Error extrayendo del PDF: {e}")
    
    return data


def complete_missing_data(content, pdf_data):
    """
    Completa campos "No especificado" con datos del PDF.
    """
    if not pdf_data:
        return content, 0
    
    replacements = 0
    
    # Tipo de Estudio
    if 'study_type' in pdf_data and 'Tipo de Estudio: No especificado' in content:
        content = content.replace(
            'Tipo de Estudio: No especificado',
            f'Tipo de Estudio: {pdf_data["study_type"]}'
        )
        replacements += 1
    
    # Escala
    if 'scale' in pdf_data and 'Escala: No especificado' in content:
        content = content.replace(
            'Escala: No especificado',
            f'Escala: {pdf_data["scale"]}'
        )
        replacements += 1
    
    # Revista
    if 'journal' in pdf_data and 'Revista/Fuente: No especificado' in content:
        content = content.replace(
            'Revista/Fuente: No especificado',
            f'Revista/Fuente: {pdf_data["journal"]}'
        )
        replacements += 1
    
    # DOI
    if 'doi' in pdf_data and 'Referencia PDF: `No especificado`' in content:
        content = content.replace(
            'Referencia PDF: `No especificado`',
            f'Referencia PDF: DOI: {pdf_data["doi"]}'
        )
        replacements += 1
    
    # Dimensiones
    if 'dimensions' in pdf_data and 'Dimensiones: No especificado' in content:
        dims = ', '.join(pdf_data['dimensions'][:3])
        content = content.replace(
            'Dimensiones: No especificado',
            f'Dimensiones: {dims}'
        )
        replacements += 1
    
    # Temperatura
    if 'temperatures' in pdf_data and 'Temperatura de Operación: No especificado' in content:
        temps = ', '.join(pdf_data['temperatures'][:5])
        content = content.replace(
            'Temperatura de Operación: No especificado',
            f'Temperatura de Operación: {temps} °C (valores extraídos del texto)'
        )
        replacements += 1
    
    # Presión
    if 'pressures' in pdf_data and 'Presión de Operación: No especificado' in content:
        press = ', '.join(pdf_data['pressures'][:5])
        content = content.replace(
            'Presión de Operación: No especificado',
            f'Presión de Operación: {press} bar (valores extraídos del texto)'
        )
        replacements += 1
    
    return content, replacements


# ============================================================================
# PROCESAMIENTO DE ARCHIVOS
# ============================================================================

def process_note_file(md_file, articulos_path, backup_dir):
    """
    Procesa un archivo de notas: detecta duplicados, limpia y valida con PDF.
    """
    print(f"\n{'='*70}")
    print(f"Procesando: {md_file.name}")
    print(f"{'='*70}")
    
    # Leer contenido
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"  ✗ Error leyendo archivo: {e}")
        return False
    
    original_size = len(original_content)
    print(f"  Tamaño original: {original_size} caracteres")
    
    # 1. Detectar y eliminar duplicados
    clean_content, had_duplicates = detect_duplicate_sections(original_content)
    
    if had_duplicates:
        print(f"  ✓ Duplicados eliminados. Nueva longitud: {len(clean_content)} caracteres")
    else:
        print(f"  ℹ No se detectaron duplicados")
    
    # 2. Limpiar estructura
    clean_content = clean_markdown_structure(clean_content)
    
    # 3. Buscar PDF correspondiente
    pdf_file = find_corresponding_pdf(md_file, articulos_path)
    
    pdf_data = {}
    if pdf_file:
        print(f"  ✓ PDF encontrado: {pdf_file.name}")
        pdf_data = extract_metadata_from_pdf(pdf_file)
        print(f"    - Datos extraídos del PDF: {len(pdf_data)} campos")
    else:
        print(f"  ⚠ No se encontró PDF correspondiente")
    
    # 4. Completar datos faltantes
    completed_content, replacements = complete_missing_data(clean_content, pdf_data)
    
    if replacements > 0:
        print(f"  ✓ Completados {replacements} campos con datos del PDF")
    
    # 5. Verificar si hubo cambios significativos
    if completed_content == original_content:
        print(f"  ℹ Sin cambios necesarios")
        return False
    
    # 6. Crear backup
    backup_path = backup_dir / md_file.name
    shutil.copy2(md_file, backup_path)
    print(f"  ✓ Backup creado: {backup_path.name}")
    
    # 7. Guardar versión limpia
    try:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(completed_content)
        
        new_size = len(completed_content)
        reduction = ((original_size - new_size) / original_size) * 100 if original_size > 0 else 0
        
        print(f"  ✓ Archivo actualizado")
        print(f"    - Tamaño final: {new_size} caracteres")
        print(f"    - Reducción: {reduction:.1f}%")
        print(f"    - Duplicados eliminados: {'Sí' if had_duplicates else 'No'}")
        print(f"    - Datos completados: {replacements}")
        
        return True
        
    except Exception as e:
        print(f"  ✗ Error guardando archivo: {e}")
        # Restaurar backup
        shutil.copy2(backup_path, md_file)
        return False


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("\n" + "="*70)
    print("LIMPIEZA Y VALIDACIÓN DE ARCHIVOS DE NOTAS")
    print("="*70)
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Rutas
    script_path = Path(__file__).parent
    articulos_path = script_path.parent / "articulos"
    backup_dir = script_path / "notas_backup" / datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Crear directorio de backup
    backup_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\nDirectorios:")
    print(f"  - Notas: {script_path}")
    print(f"  - Artículos PDF: {articulos_path}")
    print(f"  - Backup: {backup_dir}")
    
    # Verificar directorios
    if not articulos_path.exists():
        print(f"\n✗ Error: No existe el directorio de artículos")
        return
    
    # Obtener archivos .md (excluir backups y plantillas)
    md_files = [
        f for f in script_path.glob("notas_*.md")
        if not f.name.endswith('.backup') and 'plantilla' not in f.name.lower()
    ]
    
    print(f"\n✓ Encontrados {len(md_files)} archivos de notas para procesar")
    
    if not md_files:
        print("✗ No hay archivos para procesar")
        return
    
    # Procesar cada archivo
    stats = {
        'total': len(md_files),
        'processed': 0,
        'with_duplicates': 0,
        'completed_fields': 0,
        'errors': 0
    }
    
    for i, md_file in enumerate(sorted(md_files), 1):
        print(f"\n[{i}/{len(md_files)}]")
        
        try:
            success = process_note_file(md_file, articulos_path, backup_dir)
            if success:
                stats['processed'] += 1
        except Exception as e:
            print(f"  ✗ Error procesando archivo: {e}")
            stats['errors'] += 1
            import traceback
            traceback.print_exc()
    
    # Resumen final
    print("\n" + "="*70)
    print("RESUMEN DEL PROCESAMIENTO")
    print("="*70)
    print(f"  Total de archivos: {stats['total']}")
    print(f"  Procesados exitosamente: {stats['processed']}")
    print(f"  Errores: {stats['errors']}")
    print(f"  Sin cambios: {stats['total'] - stats['processed'] - stats['errors']}")
    print(f"\n  Backups guardados en: {backup_dir}")
    print("="*70 + "\n")
    
    # Sugerencia para re-ejecutar análisis
    if stats['processed'] > 0:
        print("💡 Sugerencia: Re-ejecuta los scripts de extracción para actualizar la matriz:")
        print("   python knowledge_base_extractor_v3.py")
        print("   python analyze_statistical_matrix.py")


if __name__ == "__main__":
    main()
