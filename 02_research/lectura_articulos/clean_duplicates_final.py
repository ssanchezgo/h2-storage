#!/usr/bin/env python3
"""
Script definitivo para eliminar campos duplicados en archivos .md
"""

import re
from pathlib import Path

def clean_duplicate_fields(content):
    """
    Elimina campos duplicados manteniendo solo la primera ocurrencia
    """
    lines = content.split('\n')
    seen_fields = {}
    new_lines = []
    removed = []
    
    field_patterns = [
        (r'^\*\*Revista[/]?Fuente?:\*\*', 'revista'),
        (r'^\*\*Año:\*\*', 'año'),
        (r'^\*\*DOI:\*\*', 'doi'),
        (r'^\*\*Autores?:\*\*', 'autor'),
        (r'^\*\*Fecha de Publicación:\*\*', 'fecha'),
    ]
    
    for line_num, line in enumerate(lines):
        should_keep = True
        
        for pattern, field_name in field_patterns:
            if re.match(pattern, line, re.IGNORECASE):
                if field_name in seen_fields:
                    should_keep = False
                    removed.append((field_name, line_num + 1))
                    break
                else:
                    seen_fields[field_name] = True
        
        if should_keep:
            new_lines.append(line)
    
    # Limpiar líneas en blanco excesivas
    new_content = '\n'.join(new_lines)
    new_content = re.sub(r'\n{4,}', '\n\n\n', new_content)
    
    return new_content, removed


def process_all_files():
    """
    Procesa todos los archivos .md
    """
    print("=" * 80)
    print("ELIMINACIÓN DE CAMPOS DUPLICADOS - VERSIÓN DEFINITIVA")
    print("=" * 80)
    
    base_dir = Path(__file__).parent
    md_files = sorted(base_dir.glob('notas_*.md'))
    
    print(f"\n📁 Archivos encontrados: {len(md_files)}\n")
    
    total_cleaned = 0
    total_removed = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content, removed = clean_duplicate_fields(content)
            
            if removed:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"✓ {md_file.name}")
                for field_name, line_num in removed:
                    print(f"    Eliminado {field_name} duplicado (línea {line_num})")
                total_cleaned += 1
                total_removed += len(removed)
        
        except Exception as e:
            print(f"❌ {md_file.name}: Error - {str(e)}")
    
    print("\n" + "=" * 80)
    print(f"✅ {total_cleaned} archivos limpiados")
    print(f"   {total_removed} duplicados eliminados")
    print("=" * 80)


if __name__ == "__main__":
    process_all_files()
