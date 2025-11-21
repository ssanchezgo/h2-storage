#!/usr/bin/env python3
"""
Script para:
1. Eliminar asteriscos problemáticos en los archivos .md
2. Extraer y completar información faltante desde los PDFs
3. Mejorar la estructura de datos para mejor extracción
"""

import os
import re
import PyPDF2
from pathlib import Path
from datetime import datetime

def clean_markdown_asterisks(content):
    """
    Elimina asteriscos problemáticos pero mantiene los necesarios para énfasis
    """
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        original_line = line
        
        # Patron 1: **Palabra:** al inicio de línea (MANTENER - es énfasis válido)
        # Patron 2: **Texto** en medio de frase (MANTENER - es énfasis válido)
        
        # ELIMINAR: Asteriscos sueltos o mal formados
        # Asterisco simple seguido de palabra: "* Palabra" → "Palabra" (si no es lista)
        if not line.strip().startswith('- '):  # No es lista con guión
            # Si hay un solo asterisco al inicio sin ser lista
            line = re.sub(r'^\s*\*\s+', '', line)
        
        # Corregir patrones específicos problemáticos:
        # "**Autor:** texto" puede estar causando problemas si hay espacios raros
        # Normalizar a formato consistente
        if re.match(r'^\*\*[^*]+:\*\*\s*', line):
            line = re.sub(r'^\*\*([^*]+):\*\*\s*', r'**\1:** ', line)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)


def extract_author_from_pdf(pdf_path):
    """
    Extrae el autor del PDF usando múltiples estrategias
    """
    if not pdf_path.exists():
        return None
    
    try:
        with open(pdf_path, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            
            # Estrategia 1: Metadata del PDF
            if pdf.metadata and '/Author' in pdf.metadata:
                author = pdf.metadata['/Author']
                if author and len(author.strip()) > 3:
                    return author.strip()
            
            # Estrategia 2: Primera página - buscar patrones de autor
            if len(pdf.pages) > 0:
                first_page = pdf.pages[0].extract_text()
                
                # Patrón común: líneas con nombres (mayúsculas, comas)
                # Buscar antes de "Abstract" o "Introduction"
                intro_pos = first_page.lower().find('abstract')
                if intro_pos == -1:
                    intro_pos = first_page.lower().find('introduction')
                if intro_pos == -1:
                    intro_pos = len(first_page) // 2
                
                header_section = first_page[:intro_pos]
                
                # Buscar líneas con patrones de nombre
                lines = header_section.split('\n')
                author_candidates = []
                
                for i, line in enumerate(lines[1:10]):  # Primeras 10 líneas después del título
                    line = line.strip()
                    # Detectar nombres: Mayúscula + minúsculas, puede tener comas
                    if re.search(r'^[A-Z][a-z]+(?:\s+[A-Z]\.?)(?:\s+[A-Z][a-z]+)', line):
                        author_candidates.append(line)
                    # Detectar formato: Apellido, Nombre
                    elif re.search(r'^[A-Z][a-z]+,\s*[A-Z]', line):
                        author_candidates.append(line)
                
                if author_candidates:
                    # Unir candidatos (máximo 5 autores)
                    return ', '.join(author_candidates[:5])
    
    except Exception as e:
        print(f"  ⚠️  Error extrayendo autor de PDF: {str(e)}")
    
    return None


def extract_year_from_pdf(pdf_path):
    """
    Extrae el año del PDF
    """
    if not pdf_path.exists():
        return None
    
    try:
        with open(pdf_path, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            
            # Metadata
            if pdf.metadata:
                if '/CreationDate' in pdf.metadata:
                    date_str = pdf.metadata['/CreationDate']
                    year_match = re.search(r'(\d{4})', str(date_str))
                    if year_match:
                        return year_match.group(1)
            
            # Primera página
            if len(pdf.pages) > 0:
                text = pdf.pages[0].extract_text()
                # Buscar año en formato común (2015, 2020, etc.)
                year_match = re.search(r'\b(20[0-2]\d)\b', text)
                if year_match:
                    return year_match.group(1)
    
    except Exception as e:
        print(f"  ⚠️  Error extrayendo año de PDF: {str(e)}")
    
    return None


def extract_journal_from_pdf(pdf_path):
    """
    Extrae el nombre de la revista del PDF
    """
    if not pdf_path.exists():
        return None
    
    try:
        with open(pdf_path, 'rb') as f:
            pdf = PyPDF2.PdfReader(f)
            
            if len(pdf.pages) > 0:
                first_page = pdf.pages[0].extract_text()
                
                # Patrones comunes de revistas
                patterns = [
                    r'International Journal of Hydrogen Energy',
                    r'Applied Energy',
                    r'Energy',
                    r'Journal of Alloys and Compounds',
                    r'International Journal of [A-Za-z\s]+',
                    r'Journal of [A-Za-z\s]+',
                ]
                
                for pattern in patterns:
                    match = re.search(pattern, first_page, re.IGNORECASE)
                    if match:
                        return match.group(0)
    
    except Exception as e:
        print(f"  ⚠️  Error extrayendo revista de PDF: {str(e)}")
    
    return None


def find_corresponding_pdf(md_file, articulos_dir):
    """
    Encuentra el PDF correspondiente a un archivo .md
    """
    md_name = md_file.stem.replace('notas_', '')
    
    # Extraer año si está en el nombre
    year_match = re.search(r'(\d{4})', md_name)
    year = year_match.group(1) if year_match else None
    
    # Buscar en directorio de artículos
    if not articulos_dir.exists():
        return None
    
    # Buscar por año primero
    if year:
        for pdf in articulos_dir.glob('*.pdf'):
            if year in pdf.stem:
                return pdf
    
    # Buscar por palabras clave del nombre
    keywords = re.findall(r'[a-z]{4,}', md_name.lower())
    best_match = None
    best_score = 0
    
    for pdf in articulos_dir.glob('*.pdf'):
        pdf_lower = pdf.stem.lower()
        score = sum(1 for kw in keywords if kw in pdf_lower)
        if score > best_score:
            best_score = score
            best_match = pdf
    
    return best_match if best_score >= 2 else None


def enhance_markdown_with_pdf_data(md_path, pdf_path):
    """
    Mejora el archivo .md con datos extraídos del PDF
    """
    try:
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return content, False
    
    modified = False
    
    # Verificar si falta autor
    if not re.search(r'\*\*Autor(es)?:\*\*', content, re.IGNORECASE):
        author = extract_author_from_pdf(pdf_path)
        if author:
            # Insertar después del título
            title_match = re.search(r'^#[^#].+$', content, re.MULTILINE)
            if title_match:
                insert_pos = title_match.end()
                content = (content[:insert_pos] + 
                          f'\n\n**Autor:** {author}\n' + 
                          content[insert_pos:])
                modified = True
                print(f"    ✓ Autor agregado: {author[:50]}...")
    
    # Verificar si falta año
    if not re.search(r'\*\*Año:\*\*|\*\*Fecha de Publicación:\*\*', content, re.IGNORECASE):
        year = extract_year_from_pdf(pdf_path)
        if year:
            # Insertar después de autor o título
            insert_after = re.search(r'\*\*Autor[^:]*:[^\n]+', content)
            if not insert_after:
                insert_after = re.search(r'^#[^#].+$', content, re.MULTILINE)
            
            if insert_after:
                insert_pos = insert_after.end()
                content = (content[:insert_pos] + 
                          f'\n\n**Año:** {year}\n' + 
                          content[insert_pos:])
                modified = True
                print(f"    ✓ Año agregado: {year}")
    
    # Verificar si falta revista (y eliminar duplicados si existen)
    revista_matches = list(re.finditer(r'\*\*Revista[/]?Fuente?:\*\*\s*([^\n]+)', content, re.IGNORECASE))
    
    if len(revista_matches) > 1:
        # Hay duplicados, mantener solo el primero
        for match in reversed(revista_matches[1:]):
            # Eliminar línea duplicada
            start = match.start()
            end = match.end()
            # Incluir saltos de línea extra
            if end < len(content) and content[end:end+2] == '\n\n':
                end += 2
            elif end < len(content) and content[end] == '\n':
                end += 1
            content = content[:start] + content[end:]
        modified = True
        print(f"    ✓ Duplicados de revista eliminados")
    
    if not re.search(r'\*\*Revista[/]?Fuente?:\*\*', content, re.IGNORECASE):
        journal = extract_journal_from_pdf(pdf_path)
        if journal:
            # Insertar después de año o autor
            insert_after = re.search(r'\*\*Año:[^\n]+', content)
            if not insert_after:
                insert_after = re.search(r'\*\*Autor[^:]*:[^\n]+', content)
            
            if insert_after:
                insert_pos = insert_after.end()
                content = (content[:insert_pos] + 
                          f'\n\n**Revista:** {journal}\n' + 
                          content[insert_pos:])
                modified = True
                print(f"    ✓ Revista agregada: {journal[:50]}...")
    
    return content, modified


def process_file(md_file, articulos_dir, backup_dir):
    """
    Procesa un archivo .md: limpia asteriscos y completa datos desde PDF
    """
    print(f"\n📄 Procesando: {md_file.name}")
    
    # Leer contenido original
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e:
        print(f"  ❌ Error leyendo archivo: {str(e)}")
        return False
    
    # Paso 1: Limpiar asteriscos problemáticos
    cleaned_content = clean_markdown_asterisks(original_content)
    
    # Paso 2: Encontrar PDF correspondiente
    pdf_path = find_corresponding_pdf(md_file, articulos_dir)
    
    if pdf_path:
        print(f"  📑 PDF encontrado: {pdf_path.name}")
        # Paso 3: Completar información desde PDF
        enhanced_content, was_enhanced = enhance_markdown_with_pdf_data(
            md_file, pdf_path
        )
        
        if was_enhanced:
            cleaned_content = enhanced_content
    else:
        print(f"  ⚠️  No se encontró PDF correspondiente")
    
    # Verificar si hubo cambios
    if original_content != cleaned_content:
        # Crear backup
        backup_file = backup_dir / md_file.name
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # Guardar versión mejorada
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"  ✅ Archivo mejorado y guardado")
        return True
    else:
        print(f"  ○ Sin cambios necesarios")
        return False


def main():
    """Función principal"""
    print("=" * 80)
    print("LIMPIEZA Y MEJORA DE ARCHIVOS MARKDOWN CON DATOS DE PDF")
    print("=" * 80)
    
    # Directorios
    base_dir = Path(__file__).parent
    articulos_dir = base_dir.parent / 'articulos'
    
    # Crear directorio de backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_dir = base_dir / f'backup_enhancement_{timestamp}'
    backup_dir.mkdir(exist_ok=True)
    print(f"\n📁 Backup en: {backup_dir}")
    
    # Buscar archivos
    md_files = sorted(base_dir.glob('notas_*.md'))
    
    if not md_files:
        print("⚠️  No se encontraron archivos notas_*.md")
        return
    
    print(f"\n📚 Archivos encontrados: {len(md_files)}")
    
    if not articulos_dir.exists():
        print(f"⚠️  Directorio de artículos no encontrado: {articulos_dir}")
        print("   Continuando solo con limpieza de asteriscos...")
    
    print("-" * 80)
    
    # Contadores
    processed = 0
    enhanced = 0
    errors = 0
    
    # Procesar archivos
    for md_file in md_files:
        try:
            was_enhanced = process_file(md_file, articulos_dir, backup_dir)
            processed += 1
            if was_enhanced:
                enhanced += 1
        except Exception as e:
            errors += 1
            print(f"  ❌ ERROR: {str(e)}")
    
    # Resumen
    print("\n" + "=" * 80)
    print("RESUMEN DEL PROCESAMIENTO")
    print("=" * 80)
    print(f"Total de archivos:        {len(md_files)}")
    print(f"Procesados exitosamente:  {processed}")
    print(f"Archivos mejorados:       {enhanced}")
    print(f"Sin cambios:              {processed - enhanced}")
    print(f"Errores:                  {errors}")
    print("=" * 80)
    
    if enhanced > 0:
        print(f"\n✅ Se mejoraron {enhanced} archivos")
        print(f"📁 Backups guardados en: {backup_dir}")


if __name__ == "__main__":
    main()
