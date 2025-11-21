#!/usr/bin/env python3
"""
Script para normalizar y homogeneizar todos los archivos markdown de notas.
Asegura que todos tengan una estructura consistente con campos estándar.
"""

import os
import re
import unicodedata
from pathlib import Path


def extract_info_from_content(content, filename):
    """Extrae información del contenido existente.

    Antes de extraer, se aplica una normalización ligera de caracteres
    especiales para facilitar los patrones regex y la extracción numérica.
    """

    # Normalizar caracteres especiales sin perder significado científico
    content = normalize_special_chars(content)
    info = {
        'titulo': '',
        'referencia_pdf': '',
        'autores': '',
        'año': '',
        'revista': '',
        'pais': '',
        'tipo_estudio': '',
        'escala': '',
        'configuracion': '',
        'dimensiones': '',
        'capacidad_h2': '',
        'material_hidruro': '',
        'cantidad_hidruro': '',
        'sistema_termico': '',
        'tipo_aletas': '',
        'fluido_termico': '',
        'temperatura': '',
        'presion': '',
        'tiempo_absorcion': '',
        'tiempo_desorcion': '',
        'resultados': '',
        'conclusiones_modularidad': '',
        'conclusiones_termica': '',
        'contenido_original': content
    }
    
    # Extraer título
    titulo_patterns = [
        r'# Notas sobre "([^"]+)"',
        r'# Análisis: ([^\n]+)',
        r'# Notas de Lectura: ([^\n]+)',
        r'^# ([^\n]+)'
    ]
    for pattern in titulo_patterns:
        match = re.search(pattern, content, re.MULTILINE)
        if match:
            info['titulo'] = match.group(1).strip()
            break
    
    # Extraer referencia PDF
    pdf_match = re.search(r'\*\*Referencia PDF:\*\*\s*`([^`]+)`', content)
    if pdf_match:
        info['referencia_pdf'] = pdf_match.group(1)
    
    # Extraer año del filename si no se encuentra
    year_match = re.search(r'(19|20)\d{2}', filename)
    if year_match:
        info['año'] = year_match.group(0)
    
    # Extraer año del contenido
    year_patterns = [
        r'\*\*Año:\*\*\s*(\d{4})',
        r'\((\d{4})\)',
        r'year\s*=\s*\{(\d{4})\}'
    ]
    for pattern in year_patterns:
        match = re.search(pattern, content)
        if match:
            info['año'] = match.group(1)
            break
    
    # Extraer autores
    autor_patterns = [
        r'\*\*Autor(?:es)?:\*\*\s*([^\n]+)',
        r'author\s*=\s*\{([^}]+)\}'
    ]
    for pattern in autor_patterns:
        match = re.search(pattern, content)
        if match:
            info['autores'] = match.group(1).strip()
            break
    
    # Extraer configuración del reactor
    config_patterns = [
        r'\*\*Configuración[^:]*:\*\*\s*([^\n]+)',
        r'configuración[^:]*:\s*([^\n]+)',
        r'(cilíndric[oa]|tubular|multi[- ]?tubular|placas|anular|shell[- ]and[- ]tube)'
    ]
    for pattern in config_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            info['configuracion'] = match.group(1).strip()
            break
    
    # Extraer material de hidruro
    hidruro_patterns = [
        r'\*\*(?:Material|Hidruro|Tipo de hidruro):\*\*\s*([^\n]+)',
        r'(LaNi5|LaNi₅|MgH2|MgH₂|TiFe|NaAlH4|NaAlH₄|AB5|AB2|MmNi)'
    ]
    for pattern in hidruro_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            info['material_hidruro'] = match.group(1).strip()
            break
    
    # Extraer cantidad de hidruro
    cantidad_patterns = [
        r'\*\*Cantidad[^:]*:\*\*\s*([\d.,]+\s*(?:kg|g))',
        r'([\d.,]+\s*kg)[^a-z]*(?:de\s+)?(?:aleación|hidruro|LaNi|MH)'
    ]
    for pattern in cantidad_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            info['cantidad_hidruro'] = match.group(1).strip()
            break
    
    # Extraer dimensiones
    dim_patterns = [
        r'\*\*Dimensiones:\*\*\s*([^\n]+)',
        r'\*\*Diámetro:\*\*\s*([\d.,]+\s*(?:mm|cm|m))',
        r'\*\*Longitud:\*\*\s*([\d.,]+\s*(?:mm|cm|m))'
    ]
    dims = []
    for pattern in dim_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            dims.append(match.group(1).strip())
    if dims:
        info['dimensiones'] = ' | '.join(dims)
    
    # Extraer capacidad H2
    capacidad_patterns = [
        r'capacidad[^:]*:\s*([\d.,]+\s*(?:kg|L|m³))',
        r'almacen[aóo][^:]*:\s*([\d.,]+\s*(?:kg|L|m³))'
    ]
    for pattern in capacidad_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            info['capacidad_h2'] = match.group(1).strip()
            break
    
    # Extraer sistema térmico
    termico_patterns = [
        r'\*\*Sistema[^:]*:\*\*\s*([^\n]+)',
        r'(aletas?|fins|tubos de calor|heat pipe|PCM|grafito expandido|ENG|espuma metálica)'
    ]
    for pattern in termico_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            info['sistema_termico'] = match.group(1).strip()
            break
    
    # Extraer tipo de aletas
    aletas_patterns = [
        r'aletas?\s+(anulares?|longitudinales?|radiales?|cónicas?|disco|helicoidales?|honeycomb)',
        r'\*\*(?:Tipo de\s+)?Aletas:\*\*\s*([^\n]+)'
    ]
    for pattern in aletas_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            info['tipo_aletas'] = match.group(1).strip()
            break
    
    # Extraer temperatura
    temp_match = re.search(r'temperatura[^:]*:\s*([\d.,]+(?:\s*[-–~]\s*[\d.,]+)?\s*[°]?[CK])', content, re.IGNORECASE)
    if temp_match:
        info['temperatura'] = temp_match.group(1).strip()
    
    # Extraer presión
    pres_match = re.search(r'presión[^:]*:\s*([\d.,]+(?:\s*[-–~]\s*[\d.,]+)?\s*(?:bar|MPa|atm))', content, re.IGNORECASE)
    if pres_match:
        info['presion'] = pres_match.group(1).strip()
    
    # Extraer tiempos
    tiempo_abs = re.search(r'(?:tiempo[^:]*absorción|absorción[^:]*tiempo)[^:]*:\s*([\d.,]+\s*(?:s|min|h))', content, re.IGNORECASE)
    if tiempo_abs:
        info['tiempo_absorcion'] = tiempo_abs.group(1).strip()
    
    tiempo_des = re.search(r'(?:tiempo[^:]*desorción|desorción[^:]*tiempo)[^:]*:\s*([\d.,]+\s*(?:s|min|h))', content, re.IGNORECASE)
    if tiempo_des:
        info['tiempo_desorcion'] = tiempo_des.group(1).strip()
    
    return info


def create_normalized_content(info):
    """Crea contenido normalizado con estructura estándar."""
    
    normalized = f"""# {info['titulo'] if info['titulo'] else 'Sin título'}

**Referencia PDF:** `{info['referencia_pdf'] if info['referencia_pdf'] else 'No especificado'}`

---

## Información Bibliográfica

- **Autores:** {info['autores'] if info['autores'] else 'No especificado'}
- **Año:** {info['año'] if info['año'] else 'No especificado'}
- **Revista/Fuente:** {info['revista'] if info['revista'] else 'No especificado'}
- **País/Institución:** {info['pais'] if info['pais'] else 'No especificado'}

---

## Características del Estudio

- **Tipo de Estudio:** {info['tipo_estudio'] if info['tipo_estudio'] else 'No especificado'}
- **Escala:** {info['escala'] if info['escala'] else 'No especificado'}

---

## Especificaciones Técnicas del Reactor

### Configuración y Diseño

- **Configuración del Reactor:** {info['configuracion'] if info['configuracion'] else 'No especificado'}
- **Dimensiones:** {info['dimensiones'] if info['dimensiones'] else 'No especificado'}
- **Capacidad de H₂:** {info['capacidad_h2'] if info['capacidad_h2'] else 'No especificado'}

### Material de Almacenamiento

- **Material de Hidruro:** {info['material_hidruro'] if info['material_hidruro'] else 'No especificado'}
- **Cantidad de Hidruro:** {info['cantidad_hidruro'] if info['cantidad_hidruro'] else 'No especificado'}

### Sistema de Gestión Térmica

- **Sistema de Transferencia de Calor:** {info['sistema_termico'] if info['sistema_termico'] else 'No especificado'}
- **Tipo de Aletas:** {info['tipo_aletas'] if info['tipo_aletas'] else 'No especificado'}
- **Fluido Térmico:** {info['fluido_termico'] if info['fluido_termico'] else 'No especificado'}

### Condiciones de Operación

- **Temperatura de Operación:** {info['temperatura'] if info['temperatura'] else 'No especificado'}
- **Presión de Operación:** {info['presion'] if info['presion'] else 'No especificado'}
- **Tiempo de Absorción:** {info['tiempo_absorcion'] if info['tiempo_absorcion'] else 'No especificado'}
- **Tiempo de Desorción:** {info['tiempo_desorcion'] if info['tiempo_desorcion'] else 'No especificado'}

---

## Resultados Clave

{info['resultados'] if info['resultados'] else 'Ver contenido original más abajo'}

---

## Conclusiones para el Proyecto

### Sobre Modularidad y Escalabilidad

{info['conclusiones_modularidad'] if info['conclusiones_modularidad'] else 'Ver contenido original más abajo'}

### Sobre Gestión Térmica

{info['conclusiones_termica'] if info['conclusiones_termica'] else 'Ver contenido original más abajo'}

---

## Contenido Original

{info['contenido_original']}
"""
    
    return normalized


def normalize_special_chars(text: str) -> str:
    """Normaliza caracteres especiales en el texto para facilitar la extracción.

    Reglas principales (pensadas para tu dominio de almacenamiento de H2):
    - Subíndices/superíndices de H₂, H₂O, etc. -> H2, H2O
    - Superíndices de potencias: m², m³, 10⁻⁶ -> m2, m3, 10^-6
    - Símbolos de grados y unidades: °C -> degC (o C para regex), °K -> K
    - Punto medio y multiplicación: ·, × -> *
    - Comillas tipográficas “ ” -> "
    - Guiones en dash/em dash – — -> -
    - Letras griegas comunes: Δ -> d, λ -> lambda
    """

    if not text:
        return text

    # Normalización Unicode NFKC para descomponer compatibilidad
    norm = unicodedata.normalize("NFKC", text)

    # Reemplazos específicos por dominio
    replacements = {
        "H₂": "H2",
        "H₂O": "H2O",
        "₅": "5",
        "₆": "6",
        "₈": "8",
        "¹": "1",
        "²": "2",
        "³": "3",
        "⁴": "4",
        "⁵": "5",
        "⁶": "6",
        "⁻": "-",
        "°C": "degC",
        "°F": "degF",
        "°K": "K",
        "·": "*",
        "×": "*",
        "–": "-",
        "—": "-",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "Δ": "d",
        "λ": "lambda",
    }

    for old, new in replacements.items():
        norm = norm.replace(old, new)

    # Opcional: colapsar espacios múltiples
    norm = re.sub(r"[ \t]+", " ", norm)

    return norm


def normalize_file(file_path):
    """Normaliza un archivo markdown individual."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        filename = Path(file_path).stem
        info = extract_info_from_content(content, filename)
        normalized_content = create_normalized_content(info)
        
        # Crear backup
        backup_path = str(file_path) + '.backup'
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Escribir contenido normalizado
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(normalized_content)
        
        return True, None
    except Exception as e:
        return False, str(e)


def main():
    """Función principal."""
    base_dir = Path(__file__).parent
    md_files = list(base_dir.glob("notas_*.md"))
    
    print(f"Archivos markdown encontrados: {len(md_files)}\n")
    print("Iniciando normalización...\n")
    
    success_count = 0
    error_count = 0
    
    for file in md_files:
        print(f"Procesando: {file.name}... ", end="")
        success, error = normalize_file(file)
        
        if success:
            print("✓")
            success_count += 1
        else:
            print(f"✗ Error: {error}")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"Resumen:")
    print(f"  - Archivos normalizados exitosamente: {success_count}")
    print(f"  - Errores: {error_count}")
    print(f"  - Backups creados en: *.md.backup")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
