import os
import re
import pandas as pd
from pathlib import Path
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# Estilos para el Excel
thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin")
)

header_font = Font(bold=True, color="FFFFFF")
header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
header_alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
data_alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

DEFAULT_COLUMNS = [
    "Archivo", "Título", "Autor", "Año", 
    "Configuración geométrica", "Dimensiones",
    "Diámetro", "Longitud", "Volumen",
    "Temperatura", "Presión", "Flujo",
    "Sistema de transferencia de calor",
    "Tipo de hidruro", "Cantidad de hidruro",
    "Descripción", "Conclusiones", "Imágenes"
]

def clean_value(text):
    """Limpia y normaliza el texto extraído."""
    if not text:
        return ""
    # Eliminar múltiples espacios
    text = re.sub(r"\s+", " ", text)
    # Eliminar marcadores markdown
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    # Limpiar espacios al inicio y final
    return text.strip()

def extract_specific_data(file_path):
    """Extrae información específica del archivo markdown."""
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    # Dividir el contenido en secciones
    sections = re.split(r"\n##\s+", content)
    
    patterns = {
        "Título": [
            r"# Notas de Lectura:\s*(.*?)(?=\n|$)",
            r"title\s*=\s*\{([^}]+)\}",
            r"^#\s*(.*?)(?=\n|$)"
        ],
        "Autor": [
            r"\*\*Autor(?:es)?:\*\*\s*(.*?)(?=\n|$)",
            r"author\s*=\s*\{([^}]+)\}",
            r"Por:\s*(.*?)(?=\n|$)"
        ],
        "Año": [
            r"\*\*Fecha de Publicación:\*\*\s*(\d{4})",
            r"year\s*=\s*\{(\d{4})\}",
            r"(?:19|20)\d{2}(?=\s*\})"
        ],
        "Configuración geométrica": [
            r"\*\*Configuración(?:\s+geométrica)?:\*\*\s*(.*?)(?=\n|$)",
            r"\*\*Diseño:\*\*\s*(.*?)(?=\n|$)",
            r"\*\*Tipo(?:\s+de\s+(?:reactor|tanque))?:\*\*\s*(.*?)(?=\n|$)",
            r"(?:Configuración|Diseño)(?:\s+del\s+(?:reactor|tanque))?:\s*(.*?)(?=\n|$)"
        ],
        "Sistema de transferencia de calor": [
            r"\*\*Sistema de (?:transferencia de )?calor:\*\*\s*(.*?)(?=\n|$)",
            r"\*\*Enfriamiento:\*\*\s*(.*?)(?=\n|$)",
            r"\*\*Gestión térmica:\*\*\s*(.*?)(?=\n|$)",
            r"Sistema de enfriamiento:\s*(.*?)(?=\n|$)"
        ],
        "Tipo de hidruro": [
            r"\*\*(?:Tipo de )?[Hh]idruro:\*\*\s*(.*?)(?=\n|$)",
            r"\*\*Material:\*\*\s*(.*?)(?=\n|$)",
            r"\*\*Composición:\*\*\s*(.*?)(?=\n|$)",
            r"Material(?:\s+utilizado)?:\s*(.*?)(?=\n|$)"
        ],
        "Descripción": [
            r"(?:1\.\s*)?Resumen\n\n(.*?)(?=\n\n|$)",
            r"Descripción\n\n(.*?)(?=\n\n|$)"
        ],
        "Conclusiones": [
            r"(?:4\.\s*)?Conclusiones\n\n(.*?)(?=\n\n|$)",
            r"Conclusión\n\n(.*?)(?=\n\n|$)"
        ]
    }
    
    # Patrones para medidas técnicas
    technical_patterns = {
        "Dimensiones": [
            r"\*\*Dimensiones:\*\*\s*(.*?)(?=\n|$)",
            r"\*\*Medidas:\*\*\s*(.*?)(?=\n|$)",
            r"Dimensiones del (?:reactor|tanque):\s*(.*?)(?=\n|$)"
        ],
        "Diámetro": [
            r"\*\*Diámetro:\*\*\s*([\d.,]+\s*(?:mm|cm|m))",
            r"\*\*D:\*\*\s*([\d.,]+\s*(?:mm|cm|m))",
            r"[Dd]iámetro[^:]*:\s*([\d.,]+\s*(?:mm|cm|m))"
        ],
        "Longitud": [
            r"\*\*Longitud:\*\*\s*([\d.,]+\s*(?:mm|cm|m))",
            r"\*\*L:\*\*\s*([\d.,]+\s*(?:mm|cm|m))",
            r"[Ll]ongitud[^:]*:\s*([\d.,]+\s*(?:mm|cm|m))"
        ],
        "Volumen": [
            r"\*\*Volumen:\*\*\s*([\d.,]+\s*(?:m³|L|cm³|ml))",
            r"\*\*V:\*\*\s*([\d.,]+\s*(?:m³|L|cm³|ml))",
            r"[Vv]olumen[^:]*:\s*([\d.,]+\s*(?:m³|L|cm³|ml))"
        ],
        "Temperatura": [
            r"\*\*Temperatura:\*\*\s*([\d.,]+(?:\s*[-–~]\s*[\d.,]+)?\s*[°]?[KC])",
            r"\*\*T:\*\*\s*([\d.,]+(?:\s*[-–~]\s*[\d.,]+)?\s*[°]?[KC])",
            r"[Tt]emperatura[^:]*:\s*([\d.,]+(?:\s*[-–~]\s*[\d.,]+)?\s*[°]?[KC])"
        ],
        "Presión": [
            r"\*\*Presión:\*\*\s*([\d.,]+(?:\s*[-–~]\s*[\d.,]+)?\s*(?:bar|MPa|atm))",
            r"\*\*P:\*\*\s*([\d.,]+(?:\s*[-–~]\s*[\d.,]+)?\s*(?:bar|MPa|atm))",
            r"[Pp]resión[^:]*:\s*([\d.,]+(?:\s*[-–~]\s*[\d.,]+)?\s*(?:bar|MPa|atm))"
        ],
        "Flujo": [
            r"\*\*Flujo:\*\*\s*([\d.,]+(?:\s*[-–~]\s*[\d.,]+)?\s*(?:L/min|kg/s|m³/h|slpm))",
            r"\*\*(?:Q|F):\*\*\s*([\d.,]+(?:\s*[-–~]\s*[\d.,]+)?\s*(?:L/min|kg/s|m³/h|slpm))",
            r"[Ff]lujo[^:]*:\s*([\d.,]+(?:\s*[-–~]\s*[\d.,]+)?\s*(?:L/min|kg/s|m³/h|slpm))"
        ],
        "Cantidad de hidruro": [
            r"\*\*Cantidad de hidruro:\*\*\s*([\d.,]+\s*(?:kg|g))",
            r"\*\*Masa:\*\*\s*([\d.,]+\s*(?:kg|g))",
            r"[Cc]antidad[^:]*:\s*([\d.,]+\s*(?:kg|g))"
        ]
    }
    
    # Inicializar datos
    extracted_data = {col: "" for col in DEFAULT_COLUMNS}
    extracted_data["Archivo"] = Path(file_path).stem
    
    # Buscar en todo el contenido
    for key, pattern_list in patterns.items():
        for pattern in pattern_list:
            match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
            if match:
                extracted_data[key] = clean_value(match.group(1))
                break
    
    # Buscar datos técnicos
    for section in sections:
        for key, pattern_list in technical_patterns.items():
            if not extracted_data.get(key):  # Solo si no se encontró antes
                for pattern in pattern_list:
                    match = re.search(pattern, section, re.IGNORECASE)
                    if match:
                        extracted_data[key] = clean_value(match.group(1))
                        break
    
    # Contar imágenes
    img_matches = len(re.findall(r"!\[.*?\]\(.*?\)", content))
    extracted_data["Imágenes"] = img_matches if img_matches > 0 else ""
    
    return extracted_data

def main():
    """Función principal para procesar los archivos y generar el Excel."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    all_data = []
    
    for file in Path(base_dir).glob("*.md"):
        if file.name.startswith("notas_"):
            try:
                data = extract_specific_data(file)
                all_data.append(data)
            except Exception as e:
                print(f"Error procesando {file.name}: {str(e)}")
    
    if all_data:
        df = pd.DataFrame(all_data)
        df = df.reindex(columns=DEFAULT_COLUMNS)
        
        output_file = os.path.join(base_dir, "matriz_informacion.xlsx")
        wb = Workbook()
        ws = wb.active
        ws.title = "Matriz de Información"
        
        # Escribir encabezados
        for col, header in enumerate(DEFAULT_COLUMNS, 1):
            cell = ws.cell(row=1, column=col, value=header)
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = header_alignment
            cell.border = thin_border
        
        # Escribir datos
        for row_idx, row in enumerate(df.values, 2):
            for col_idx, value in enumerate(row, 1):
                cell = ws.cell(row=row_idx, column=col_idx)
                cell.value = str(value) if pd.notnull(value) and value != "" else None
                cell.alignment = data_alignment
                cell.border = thin_border
        
        # Ajustar ancho de columnas
        for col in ws.columns:
            max_length = 0
            for cell in col:
                try:
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                except:
                    pass
            ws.column_dimensions[col[0].column_letter].width = min(max_length + 2, 50)
        
        wb.save(output_file)
        print(f"Archivo Excel creado: {output_file}")
    else:
        print("No se encontraron datos para exportar.")

if __name__ == "__main__":
    main()