#!/usr/bin/env python3
"""
Script para corregir problemas de formato en archivos Markdown
Soluciona:
- Líneas separadoras mal formateadas (- -- → ---)
- Asteriscos mal formateados (- * → **)
- Espacios en blanco excesivos en líneas
- Múltiples líneas en blanco consecutivas
"""

import os
import re
from pathlib import Path

def fix_markdown_formatting(content):
    """
    Corrige problemas de formato en contenido Markdown
    
    Args:
        content: String con el contenido del archivo
        
    Returns:
        String con el contenido corregido
    """
    lines = content.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Limpiar espacios al final de líneas
        line = line.rstrip()
        
        # Corregir líneas separadoras mal formadas: "- --" → "---"
        if re.match(r'^-\s*--+\s*$', line):
            line = '---'
        
        # Corregir asteriscos de énfasis mal formados: "- *texto:**" → "**texto:**"
        # Patrón: "- *" al inicio de la palabra, seguido de texto y ":"
        line = re.sub(r'^-\s+\*([^*]+?):\*\*', r'**\1:**', line)
        
        # Corregir variante sin los dos puntos: "- *texto**" → "**texto**"
        line = re.sub(r'^-\s+\*([^*]+?)\*\*', r'**\1**', line)
        
        # Corregir caso donde falta el segundo asterisco: "- *texto:" → "**texto:**"
        line = re.sub(r'^-\s+\*([^*]+?):', r'**\1:**', line)
        
        fixed_lines.append(line)
    
    # Unir las líneas
    fixed_content = '\n'.join(fixed_lines)
    
    # Reducir múltiples líneas en blanco a máximo 2
    fixed_content = re.sub(r'\n{4,}', '\n\n\n', fixed_content)
    
    # Asegurar que hay línea en blanco después de encabezados
    fixed_content = re.sub(r'^(#{1,6}\s+.+)$', r'\1\n', fixed_content, flags=re.MULTILINE)
    
    # Asegurar línea en blanco antes de encabezados (excepto al inicio)
    fixed_content = re.sub(r'([^\n])\n(#{1,6}\s+)', r'\1\n\n\2', fixed_content)
    
    # Asegurar línea en blanco antes de listas
    fixed_content = re.sub(r'([^\n])\n(-\s+)', r'\1\n\n\2', fixed_content)
    
    # Limpiar líneas en blanco al final del archivo
    fixed_content = fixed_content.rstrip() + '\n'
    
    return fixed_content


def process_markdown_file(file_path):
    """
    Procesa un archivo Markdown y corrige su formato
    
    Args:
        file_path: Path al archivo
        
    Returns:
        bool: True si se realizaron cambios, False si no
    """
    try:
        # Leer contenido original
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Aplicar correcciones
        fixed_content = fix_markdown_formatting(original_content)
        
        # Verificar si hubo cambios
        if original_content != fixed_content:
            # Guardar contenido corregido
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error procesando {file_path.name}: {str(e)}")
        return False


def main():
    """Función principal"""
    print("=" * 80)
    print("CORRECCIÓN DE FORMATO EN ARCHIVOS MARKDOWN")
    print("=" * 80)
    
    # Directorio actual
    base_dir = Path(__file__).parent
    
    # Buscar todos los archivos notas_*.md
    md_files = sorted(base_dir.glob('notas_*.md'))
    
    if not md_files:
        print("⚠️  No se encontraron archivos notas_*.md")
        return
    
    print(f"\n📁 Archivos encontrados: {len(md_files)}")
    print("-" * 80)
    
    # Contadores
    processed = 0
    modified = 0
    unchanged = 0
    errors = 0
    
    # Procesar cada archivo
    for md_file in md_files:
        try:
            was_modified = process_markdown_file(md_file)
            processed += 1
            
            if was_modified:
                modified += 1
                print(f"✓ {md_file.name:60s} [CORREGIDO]")
            else:
                unchanged += 1
                print(f"○ {md_file.name:60s} [SIN CAMBIOS]")
                
        except Exception as e:
            errors += 1
            print(f"✗ {md_file.name:60s} [ERROR: {str(e)}]")
    
    # Resumen final
    print("\n" + "=" * 80)
    print("RESUMEN DEL PROCESAMIENTO")
    print("=" * 80)
    print(f"Total de archivos:        {len(md_files)}")
    print(f"Procesados exitosamente:  {processed}")
    print(f"Archivos corregidos:      {modified}")
    print(f"Sin cambios necesarios:   {unchanged}")
    print(f"Errores:                  {errors}")
    print("=" * 80)
    
    if modified > 0:
        print(f"\n✅ Se corrigieron {modified} archivos con problemas de formato")
    
    if errors > 0:
        print(f"\n⚠️  Se encontraron {errors} errores durante el procesamiento")


if __name__ == "__main__":
    main()
