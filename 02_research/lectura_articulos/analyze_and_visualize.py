import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import numpy as np

# Configuración de estilo
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_context("paper", font_scale=1.2)

# Rutas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_FILE = os.path.join(BASE_DIR, "matriz_informacion_articulos.xlsx")
IMG_DIR = os.path.join(BASE_DIR, "img")

if not os.path.exists(IMG_DIR):
    os.makedirs(IMG_DIR)

def clean_numeric(value):
    """Convierte valores a float, manejando strings con unidades o rangos."""
    if pd.isna(value):
        return np.nan
    if isinstance(value, (int, float)):
        return float(value)
    
    # Convertir a string y limpiar
    value_str = str(value).strip()
    
    # Manejar rangos "10-15" -> promedio 12.5
    if '-' in value_str:
        parts = value_str.split('-')
        try:
            # Intentar extraer números de las partes
            nums = [float(re.findall(r"[\d\.]+", p)[0]) for p in parts if re.findall(r"[\d\.]+", p)]
            if len(nums) > 0:
                return sum(nums) / len(nums)
        except:
            pass

    # Extraer el primer número encontrado
    match = re.search(r"([\d\.]+)", value_str)
    if match:
        try:
            return float(match.group(1))
        except ValueError:
            return np.nan
    return np.nan

def standardize_geometry(text):
    """Agrupa las configuraciones de reactor en categorías principales."""
    if pd.isna(text):
        return "No especificado"
    text = str(text).lower()
    
    if "modular" in text or "multi" in text or "stack" in text:
        return "Modular / Multi-tubular"
    elif "placa" in text or "plate" in text:
        return "Placas (Plate-Frame)"
    elif "cilíndrico" in text or "cylindrical" in text or "tubular" in text:
        return "Cilíndrico / Tubular"
    elif "disco" in text or "disc" in text:
        return "Disco"
    elif "conic" in text or "cónico" in text:
        return "Cónico"
    else:
        return "Otro / No especificado"

def main():
    print(f"Cargando datos desde: {EXCEL_FILE}")
    if not os.path.exists(EXCEL_FILE):
        print("Error: No se encuentra el archivo Excel. Ejecuta primero extract_md_data.py")
        return

    df = pd.read_excel(EXCEL_FILE)
    
    # --- PREPROCESAMIENTO ---
    print("Procesando datos...")
    
    # Limpieza de columnas numéricas clave
    numeric_cols = [
        'Mejora_Tiempo_%', 
        'Conductividad_Térmica_W_mK', 
        'Cantidad_Hidruro_kg', 
        'Tiempo_Absorción_min',
        'Mejora_Conductividad_%',
        'Capacidad_H2_wt%'
    ]
    
    for col in numeric_cols:
        if col in df.columns:
            df[f'{col}_clean'] = df[col].apply(clean_numeric)
        else:
            print(f"Advertencia: Columna {col} no encontrada")

    # Estandarización de Geometría
    if 'Configuración_Reactor' in df.columns:
        df['Geometria_Std'] = df['Configuración_Reactor'].apply(standardize_geometry)
    
    # --- VISUALIZACIÓN ---
    
    # 1. Distribución de Geometrías (Pastel)
    plt.figure(figsize=(10, 8))
    geo_counts = df['Geometria_Std'].value_counts()
    plt.pie(geo_counts, labels=geo_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
    plt.title('Distribución de Configuraciones de Reactor en la Literatura')
    plt.savefig(os.path.join(IMG_DIR, '1_distribucion_geometrias.png'))
    plt.close()
    print("Generado: 1_distribucion_geometrias.png")

    # 2. Mejora de Tiempo por Sistema de Gestión Térmica (Barras)
    if 'Sistema_Gestión_Térmica' in df.columns and 'Mejora_Tiempo_%_clean' in df.columns:
        plt.figure(figsize=(12, 6))
        # Filtrar datos con mejora > 0
        plot_data = df[df['Mejora_Tiempo_%_clean'] > 0].sort_values('Mejora_Tiempo_%_clean', ascending=False)
        
        # Tomar top 15 para no saturar
        top_data = plot_data.head(15)
        
        sns.barplot(data=top_data, y='Sistema_Gestión_Térmica', x='Mejora_Tiempo_%_clean', palette='viridis')
        plt.title('Top Estrategias de Gestión Térmica por Reducción de Tiempo de Carga')
        plt.xlabel('Reducción de Tiempo (%)')
        plt.ylabel('Estrategia')
        plt.tight_layout()
        plt.savefig(os.path.join(IMG_DIR, '2_mejora_tiempo_estrategias.png'))
        plt.close()
        print("Generado: 2_mejora_tiempo_estrategias.png")

    # 3. Conductividad Térmica vs Aditivos (Boxplot)
    if 'Aditivo_Conductividad' in df.columns and 'Conductividad_Térmica_W_mK_clean' in df.columns:
        plt.figure(figsize=(10, 6))
        # Limpiar categorías de aditivos
        df['Aditivo_Std'] = df['Aditivo_Conductividad'].fillna('Sin Aditivo').astype(str)
        df['Aditivo_Std'] = df['Aditivo_Std'].apply(lambda x: 'ENG/Grafito' if 'grafito' in x.lower() or 'eng' in x.lower() else x)
        df['Aditivo_Std'] = df['Aditivo_Std'].apply(lambda x: 'Espuma Metálica' if 'espuma' in x.lower() or 'foam' in x.lower() else x)
        
        # Filtrar solo categorías relevantes
        relevant_additives = ['ENG/Grafito', 'Espuma Metálica', 'Sin Aditivo']
        plot_data = df[df['Aditivo_Std'].isin(relevant_additives) | (df['Conductividad_Térmica_W_mK_clean'] > 0)]
        
        if not plot_data.empty and plot_data['Conductividad_Térmica_W_mK_clean'].notna().sum() > 0:
            sns.boxplot(data=plot_data, x='Aditivo_Std', y='Conductividad_Térmica_W_mK_clean', hue='Aditivo_Std', palette='Set2', legend=False)
            plt.title('Conductividad Térmica Efectiva por Tipo de Aditivo')
            plt.ylabel('Conductividad (W/m·K)')
            plt.xlabel('Tipo de Aditivo')
            plt.savefig(os.path.join(IMG_DIR, '3_conductividad_aditivos.png'))
            plt.close()
            print("Generado: 3_conductividad_aditivos.png")
        else:
            print("Advertencia: No hay suficientes datos para el gráfico de conductividad.")

    # 4. Escala vs Mejora de Tiempo (Scatter) - Modularidad
    # Nota: Tiempo_Absorción_min no está disponible en el Excel actual, usamos Mejora_Tiempo_%
    if 'Cantidad_Hidruro_kg_clean' in df.columns and 'Mejora_Tiempo_%_clean' in df.columns:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(
            data=df, 
            x='Cantidad_Hidruro_kg_clean', 
            y='Mejora_Tiempo_%_clean', 
            hue='Geometria_Std',
            style='Modularidad',
            s=100,
            alpha=0.7
        )
        plt.title('Relación Escala (Masa) vs Mejora de Tiempo')
        plt.xlabel('Masa de Hidruro (kg)')
        plt.ylabel('Mejora de Tiempo (%)')
        plt.xscale('log') # Escala logarítmica suele ser mejor para masa
        plt.grid(True, which="both", ls="-", alpha=0.2)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(os.path.join(IMG_DIR, '4_escala_vs_mejora.png'))
        plt.close()
        print("Generado: 4_escala_vs_mejora.png")

    # --- REPORTE DE TEXTO ---
    print("\n--- RESUMEN DE HALLAZGOS ---")
    
    summary_lines = ["--- RESUMEN DE HALLAZGOS ---"]

    # Mejor estrategia por tiempo
    best_time = df.loc[df['Mejora_Tiempo_%_clean'].idxmax()] if not df['Mejora_Tiempo_%_clean'].isna().all() else None
    if best_time is not None:
        msg = f"\nMayor reducción de tiempo reportada: {best_time['Mejora_Tiempo_%_clean']}%\nEstrategia: {best_time['Sistema_Gestión_Térmica']}\nArtículo: {best_time['Archivo_Nota']}"
        print(msg)
        summary_lines.append(msg)

    # Mejor conductividad
    best_cond = df.loc[df['Conductividad_Térmica_W_mK_clean'].idxmax()] if not df['Conductividad_Térmica_W_mK_clean'].isna().all() else None
    if best_cond is not None:
        msg = f"\nMayor conductividad térmica reportada: {best_cond['Conductividad_Térmica_W_mK_clean']} W/m·K\nAditivo/Método: {best_cond['Aditivo_Conductividad']}\nArtículo: {best_cond['Archivo_Nota']}"
        print(msg)
        summary_lines.append(msg)

    # Conteo Modular vs No Modular
    if 'Modularidad' in df.columns:
        mod_counts = df['Modularidad'].value_counts()
        msg = "\nDesglose de Modularidad:\n" + mod_counts.to_string()
        print(msg)
        summary_lines.append(msg)
        
    # Guardar resumen en texto
    with open(os.path.join(BASE_DIR, "resumen_hallazgos.txt"), "w") as f:
        f.write("\n".join(summary_lines))
    print(f"\nResumen guardado en: {os.path.join(BASE_DIR, 'resumen_hallazgos.txt')}")

