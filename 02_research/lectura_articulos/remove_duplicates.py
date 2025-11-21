#!/usr/bin/env python3
"""
Script para eliminar duplicados de campos en archivos .md
"""

import re
from pathlib import Path

def remove_duplicate_fields(content):
    """
    Elimina campos duplicados manteniendo solo la primera ocurrencia
    """
    # Patrones de campos que pueden estar duplicados (con saltos de línea)
    patterns = [
        (r'^\*\*Revista[/]?Fuente?:\*\*\s*[^\n]+\n+', 'revista'),
        (r'^\*\*Año:\*\*\s*\d{4}\n+', 'año'),
        (r'^\*\*DOI:\*\*\s*[^\n]+\n+', 'doi'),
    ]
    
    modified = False
    for pattern, field_name in patterns:
        matches = list(re.finditer(pattern, content, re.MULTILINE | re.IGNORECASE))
        
        if len(matches) > 1:
            # Mantener solo la primera ocurrencia, eliminar las demás
            # Eliminar de atrás hacia adelante para no afectar índices
            for match in reversed(matches[1:]):
                start = match.start()
                end = match.end()
                content = content[:start] + content[end:]
                modified = True
            print(f"    ✓ Eliminados {len(matches)-1} duplicados de {field_name}")
    
    # Limpiar múltiples líneas en blanco
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    return content, modified


def process_file(md_file):
    """
    Procesa un archivo eliminando duplicados
    """
    try:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        cleaned_content, was_modified = remove_duplicate_fields(content)
        
        if was_modified:
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"  ❌ Error: {str(e)}")
        return False


def main():
    print("=" * 80)
    print("ELIMINACIÓN DE CAMPOS DUPLICADOS")
    print("=" * 80)
    
    base_dir = Path(__file__).parent
    md_files = sorted(base_dir.glob('notas_*.md'))
    
    print(f"\n📁 Archivos encontrados: {len(md_files)}\n")
    
    cleaned = 0
    
    for md_file in md_files:
        print(f"📄 {md_file.name}")
        if process_file(md_file):
            cleaned += 1
    
    print("\n" + "=" * 80)
    print(f"✅ {cleaned} archivos limpiados")
    print("=" * 80)


if __name__ == "__main__":
    main()
