#!/usr/bin/env python3
"""
Análisis Estadístico de la Base de Conocimientos
Genera visualizaciones y estadísticas para el informe técnico ANH951

Análisis basados en:
1. Distribución de arquitecturas (Monolítico vs Modular)
2. Estrategias de gestión térmica (Activa/Pasiva/Híbrida)
3. Escalabilidad (Laboratorio → Industrial)
4. Materiales de hidruro
5. Mejoras de rendimiento reportadas
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pathlib import Path
from datetime import datetime

# Configuración de estilo
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# ============================================================================
# CARGA Y PREPARACIÓN DE DATOS
# ============================================================================

def load_latest_matrix(lectura_path):
    """Carga la matriz más reciente generada."""
    xlsx_files = list(lectura_path.glob("matriz_consolidada_v3*.xlsx"))
    
    if not xlsx_files:
        # Buscar versiones anteriores
        xlsx_files = list(lectura_path.glob("matriz_conocimiento*.xlsx"))
    
    if not xlsx_files:
        raise FileNotFoundError("No se encontró ninguna matriz de conocimiento")
    
    # Tomar la más reciente
    latest_file = max(xlsx_files, key=lambda p: p.stat().st_mtime)
    
    print(f"Cargando: {latest_file.name}")
    df = pd.read_excel(latest_file, sheet_name=0)
    
    return df, latest_file


def clean_and_prepare_data(df):
    """Limpia y prepara los datos para análisis."""
    print(f"\nDatos cargados: {len(df)} artículos")
    print(f"Columnas disponibles: {len(df.columns)}")
    
    # Reemplazar valores vacíos
    df = df.fillna("No especificado")
    
    # Limpiar espacios
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str).str.strip()
    
    return df


# ============================================================================
# ANÁLISIS 1: DISTRIBUCIÓN DE ARQUITECTURAS
# ============================================================================

def analyze_architecture(df, output_dir):
    """
    Analiza la distribución de arquitecturas de reactores.
    Monolítico vs Modular vs Híbrido
    """
    print("\n" + "="*70)
    print("ANÁLISIS 1: ARQUITECTURA DE REACTORES")
    print("="*70)
    
    # Contar arquitecturas
    arch_counts = df['Arquitectura'].value_counts()
    print("\nDistribución de arquitecturas:")
    for arch, count in arch_counts.items():
        pct = (count / len(df)) * 100
        print(f"  {arch}: {count} ({pct:.1f}%)")
    
    # Gráfico
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Pie chart
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6A994E']
    explode = [0.1 if i == 0 else 0 for i in range(len(arch_counts))]
    
    wedges, texts, autotexts = ax1.pie(
        arch_counts.values,
        labels=arch_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors[:len(arch_counts)],
        explode=explode
    )
    
    for autotext in autotexts:
        autotext.set_color('white')
        autotext.set_fontweight('bold')
    
    ax1.set_title('Distribución de Arquitecturas de Reactores', fontweight='bold', pad=20)
    
    # Bar chart con escala
    if 'Escala' in df.columns:
        cross_tab = pd.crosstab(df['Arquitectura'], df['Escala'])
        cross_tab.plot(kind='bar', ax=ax2, stacked=False)
        ax2.set_title('Arquitectura por Escala de Estudio', fontweight='bold')
        ax2.set_xlabel('Arquitectura')
        ax2.set_ylabel('Número de Estudios')
        ax2.legend(title='Escala', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax2.grid(axis='y', alpha=0.3)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    output_path = output_dir / '1_arquitecturas_reactores.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Gráfico guardado: {output_path.name}")
    plt.close()
    
    return arch_counts


# ============================================================================
# ANÁLISIS 2: ESTRATEGIAS DE GESTIÓN TÉRMICA
# ============================================================================

def analyze_thermal_management(df, output_dir):
    """
    Analiza estrategias de gestión térmica.
    Activa vs Pasiva vs Híbrida
    """
    print("\n" + "="*70)
    print("ANÁLISIS 2: GESTIÓN TÉRMICA")
    print("="*70)
    
    # Contar estrategias
    thermal_counts = df['Estrategia_Térmica'].value_counts()
    print("\nDistribución de estrategias térmicas:")
    for strategy, count in thermal_counts.items():
        pct = (count / len(df)) * 100
        print(f"  {strategy}: {count} ({pct:.1f}%)")
    
    # Analizar métodos activos
    if 'Método_Activo' in df.columns:
        active_methods = df[df['Método_Activo'] != 'No especificado']['Método_Activo']
        if len(active_methods) > 0:
            # Separar métodos múltiples
            all_methods = []
            for methods in active_methods:
                if isinstance(methods, str) and methods != '':
                    all_methods.extend([m.strip() for m in methods.split(',')])
            
            if all_methods:
                method_counts = pd.Series(all_methods).value_counts()
                print("\nMétodos activos más usados:")
                for method, count in method_counts.head(5).items():
                    print(f"  {method}: {count}")
    
    # Gráficos
    fig = plt.figure(figsize=(16, 6))
    gs = fig.add_gridspec(1, 3, hspace=0.3, wspace=0.3)
    
    # Gráfico 1: Estrategia térmica general
    ax1 = fig.add_subplot(gs[0, 0])
    thermal_counts.plot(kind='bar', ax=ax1, color=['#E63946', '#F1Faee', '#A8DADC'])
    ax1.set_title('Estrategias de Gestión Térmica', fontweight='bold')
    ax1.set_xlabel('Estrategia')
    ax1.set_ylabel('Número de Estudios')
    ax1.grid(axis='y', alpha=0.3)
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # Añadir valores en las barras
    for i, v in enumerate(thermal_counts.values):
        ax1.text(i, v + 0.5, str(v), ha='center', va='bottom', fontweight='bold')
    
    # Gráfico 2: Estrategia por arquitectura
    ax2 = fig.add_subplot(gs[0, 1])
    cross_thermal = pd.crosstab(df['Estrategia_Térmica'], df['Arquitectura'])
    cross_thermal.plot(kind='bar', ax=ax2, stacked=True)
    ax2.set_title('Estrategia Térmica por Arquitectura', fontweight='bold')
    ax2.set_xlabel('Estrategia Térmica')
    ax2.set_ylabel('Número de Estudios')
    ax2.legend(title='Arquitectura', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax2.grid(axis='y', alpha=0.3)
    plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # Gráfico 3: Top métodos activos
    if 'all_methods' in locals() and all_methods:
        ax3 = fig.add_subplot(gs[0, 2])
        method_counts.head(7).plot(kind='barh', ax=ax3, color='#457B9D')
        ax3.set_title('Métodos Activos Más Utilizados', fontweight='bold')
        ax3.set_xlabel('Número de Estudios')
        ax3.set_ylabel('Método')
        ax3.grid(axis='x', alpha=0.3)
        
        # Añadir valores
        for i, v in enumerate(method_counts.head(7).values):
            ax3.text(v + 0.2, i, str(v), va='center', fontweight='bold')
    
    plt.tight_layout()
    output_path = output_dir / '2_gestion_termica.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Gráfico guardado: {output_path.name}")
    plt.close()
    
    return thermal_counts


# ============================================================================
# ANÁLISIS 3: ESCALABILIDAD
# ============================================================================

def analyze_scalability(df, output_dir):
    """
    Analiza la distribución por escala de estudio.
    Laboratorio → Piloto → Industrial
    """
    print("\n" + "="*70)
    print("ANÁLISIS 3: ESCALABILIDAD")
    print("="*70)
    
    scale_counts = df['Escala'].value_counts()
    print("\nDistribución por escala:")
    for scale, count in scale_counts.items():
        pct = (count / len(df)) * 100
        print(f"  {scale}: {count} ({pct:.1f}%)")
    
    # Gráficos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Gráfico 1: Distribución general
    scale_counts.plot(kind='bar', ax=ax1, color=['#264653', '#2A9D8F', '#E9C46A', '#F4A261'])
    ax1.set_title('Distribución de Estudios por Escala', fontweight='bold')
    ax1.set_xlabel('Escala')
    ax1.set_ylabel('Número de Estudios')
    ax1.grid(axis='y', alpha=0.3)
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # Añadir valores
    for i, v in enumerate(scale_counts.values):
        ax1.text(i, v + 0.5, str(v), ha='center', va='bottom', fontweight='bold')
    
    # Gráfico 2: Escala por tipo de estudio
    if 'Tipo_Estudio' in df.columns:
        cross_scale = pd.crosstab(df['Escala'], df['Tipo_Estudio'])
        cross_scale.plot(kind='bar', ax=ax2, stacked=True)
        ax2.set_title('Escala por Tipo de Estudio', fontweight='bold')
        ax2.set_xlabel('Escala')
        ax2.set_ylabel('Número de Estudios')
        ax2.legend(title='Tipo', bbox_to_anchor=(1.05, 1), loc='upper left')
        ax2.grid(axis='y', alpha=0.3)
        plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    output_path = output_dir / '3_escalabilidad.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Gráfico guardado: {output_path.name}")
    plt.close()
    
    return scale_counts


# ============================================================================
# ANÁLISIS 4: MATERIALES DE HIDRURO
# ============================================================================

def analyze_materials(df, output_dir):
    """
    Analiza los materiales de hidruro metálico utilizados.
    """
    print("\n" + "="*70)
    print("ANÁLISIS 4: MATERIALES DE HIDRURO")
    print("="*70)
    
    # Limpiar datos de materiales (quitar asteriscos, espacios extras)
    df['Material_Hidruro_Clean'] = df['Material_Hidruro'].str.replace('**', '').str.strip()
    
    material_counts = df['Material_Hidruro_Clean'].value_counts().head(10)
    
    print("\nMateriales más utilizados:")
    for material, count in material_counts.items():
        pct = (count / len(df)) * 100
        print(f"  {material}: {count} ({pct:.1f}%)")
    
    # Gráfico
    fig, ax = plt.subplots(figsize=(12, 8))
    
    material_counts.plot(kind='barh', ax=ax, color='#06A77D')
    ax.set_title('Top 10 Materiales de Hidruro Metálico', fontweight='bold', pad=20)
    ax.set_xlabel('Número de Estudios')
    ax.set_ylabel('Material')
    ax.grid(axis='x', alpha=0.3)
    
    # Añadir valores
    for i, v in enumerate(material_counts.values):
        ax.text(v + 0.3, i, str(v), va='center', fontweight='bold')
    
    plt.tight_layout()
    output_path = output_dir / '4_materiales_hidruro.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Gráfico guardado: {output_path.name}")
    plt.close()
    
    return material_counts


# ============================================================================
# ANÁLISIS 5: TIMELINE DE INVESTIGACIÓN
# ============================================================================

def analyze_timeline(df, output_dir):
    """
    Analiza la evolución temporal de la investigación.
    """
    print("\n" + "="*70)
    print("ANÁLISIS 5: TIMELINE DE INVESTIGACIÓN")
    print("="*70)
    
    # Limpiar años
    df['Año_Clean'] = pd.to_numeric(df['Año'], errors='coerce')
    df_with_year = df[df['Año_Clean'].notna()].copy()
    
    if len(df_with_year) == 0:
        print("  ⚠ No hay datos de año suficientes")
        return None
    
    # Agrupar por año
    year_counts = df_with_year.groupby('Año_Clean').size().sort_index()
    
    print(f"\nRango temporal: {int(year_counts.index.min())} - {int(year_counts.index.max())}")
    print(f"Pico de publicaciones: {int(year_counts.idxmax())} con {year_counts.max()} estudios")
    
    # Gráfico
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Gráfico 1: Timeline general
    year_counts.plot(kind='bar', ax=ax1, color='#1D3557', width=0.7)
    ax1.set_title('Evolución Temporal de Publicaciones', fontweight='bold', fontsize=14)
    ax1.set_xlabel('Año')
    ax1.set_ylabel('Número de Publicaciones')
    ax1.grid(axis='y', alpha=0.3)
    
    # Añadir línea de tendencia
    z = np.polyfit(range(len(year_counts)), year_counts.values, 2)
    p = np.poly1d(z)
    ax1.plot(range(len(year_counts)), p(range(len(year_counts))), "r--", alpha=0.8, linewidth=2, label='Tendencia')
    ax1.legend()
    
    # Gráfico 2: Tipo de estudio por década
    df_with_year['Década'] = (df_with_year['Año_Clean'] // 10) * 10
    decade_type = pd.crosstab(df_with_year['Década'], df_with_year['Tipo_Estudio'])
    decade_type.plot(kind='bar', ax=ax2, stacked=True)
    ax2.set_title('Tipo de Estudio por Década', fontweight='bold')
    ax2.set_xlabel('Década')
    ax2.set_ylabel('Número de Estudios')
    ax2.legend(title='Tipo', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    output_path = output_dir / '5_timeline_investigacion.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Gráfico guardado: {output_path.name}")
    plt.close()
    
    return year_counts


# ============================================================================
# ANÁLISIS 6: MATRIZ DE CORRELACIÓN
# ============================================================================

def analyze_correlations(df, output_dir):
    """
    Matriz de correlación entre categorías principales.
    """
    print("\n" + "="*70)
    print("ANÁLISIS 6: CORRELACIONES")
    print("="*70)
    
    # Crear matriz de co-ocurrencia
    categories = ['Arquitectura', 'Estrategia_Térmica', 'Escala', 'Tipo_Estudio', 'Aplicación']
    available_cats = [cat for cat in categories if cat in df.columns]
    
    if len(available_cats) < 2:
        print("  ⚠ No hay suficientes categorías para análisis de correlación")
        return None
    
    # Crear DataFrame de correlación
    fig, axes = plt.subplots(2, 2, figsize=(16, 14))
    axes = axes.flatten()
    
    plot_idx = 0
    
    # Combinaciones de interés
    combinations = [
        ('Arquitectura', 'Estrategia_Térmica'),
        ('Arquitectura', 'Escala'),
        ('Estrategia_Térmica', 'Escala'),
        ('Escala', 'Tipo_Estudio')
    ]
    
    for cat1, cat2 in combinations:
        if cat1 in df.columns and cat2 in df.columns and plot_idx < 4:
            ax = axes[plot_idx]
            
            # Crear tabla de contingencia
            ct = pd.crosstab(df[cat1], df[cat2])
            
            # Heatmap
            sns.heatmap(ct, annot=True, fmt='d', cmap='YlOrRd', ax=ax, cbar_kws={'label': 'Frecuencia'})
            ax.set_title(f'{cat1} vs {cat2}', fontweight='bold')
            ax.set_xlabel(cat2)
            ax.set_ylabel(cat1)
            
            plot_idx += 1
    
    # Ocultar ejes no usados
    for idx in range(plot_idx, 4):
        axes[idx].axis('off')
    
    plt.tight_layout()
    output_path = output_dir / '6_correlaciones.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Gráfico guardado: {output_path.name}")
    plt.close()
    
    print("\nTablas de contingencia principales:")
    for cat1, cat2 in combinations[:2]:
        if cat1 in df.columns and cat2 in df.columns:
            ct = pd.crosstab(df[cat1], df[cat2])
            print(f"\n{cat1} vs {cat2}:")
            print(ct)


# ============================================================================
# GENERAR REPORTE ESTADÍSTICO
# ============================================================================

def generate_statistical_report(df, output_dir):
    """
    Genera un reporte estadístico en texto.
    """
    report_path = output_dir / 'reporte_estadistico.txt'
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("="*70 + "\n")
        f.write("REPORTE ESTADÍSTICO - BASE DE CONOCIMIENTOS ANH951\n")
        f.write(f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*70 + "\n\n")
        
        f.write(f"Total de artículos analizados: {len(df)}\n\n")
        
        # Estadísticas por categoría
        categories = ['Arquitectura', 'Estrategia_Térmica', 'Escala', 'Tipo_Estudio', 'Aplicación']
        
        for cat in categories:
            if cat in df.columns:
                f.write(f"\n{cat}:\n")
                f.write("-" * 50 + "\n")
                counts = df[cat].value_counts()
                for value, count in counts.items():
                    pct = (count / len(df)) * 100
                    f.write(f"  {value}: {count} ({pct:.1f}%)\n")
        
        # Años
        if 'Año' in df.columns:
            df['Año_Clean'] = pd.to_numeric(df['Año'], errors='coerce')
            years = df['Año_Clean'].dropna()
            if len(years) > 0:
                f.write(f"\n\nRango temporal:\n")
                f.write("-" * 50 + "\n")
                f.write(f"  Primer artículo: {int(years.min())}\n")
                f.write(f"  Último artículo: {int(years.max())}\n")
                f.write(f"  Mediana: {int(years.median())}\n")
        
        # Materiales
        if 'Material_Hidruro' in df.columns:
            f.write(f"\n\nMateriales de hidruro (Top 5):\n")
            f.write("-" * 50 + "\n")
            df['Material_Clean'] = df['Material_Hidruro'].str.replace('**', '').str.strip()
            top_materials = df['Material_Clean'].value_counts().head(5)
            for material, count in top_materials.items():
                pct = (count / len(df)) * 100
                f.write(f"  {material}: {count} ({pct:.1f}%)\n")
    
    print(f"\n✓ Reporte generado: {report_path.name}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print("\n" + "="*70)
    print("ANÁLISIS ESTADÍSTICO - BASE DE CONOCIMIENTOS ANH951")
    print("="*70)
    
    # Rutas
    lectura_path = Path(__file__).parent
    output_dir = lectura_path / "analisis_estadistico"
    output_dir.mkdir(exist_ok=True)
    
    print(f"\nDirectorio de salida: {output_dir}")
    
    # Cargar datos
    try:
        df, source_file = load_latest_matrix(lectura_path)
        df = clean_and_prepare_data(df)
    except Exception as e:
        print(f"\n✗ Error cargando datos: {e}")
        return
    
    print(f"\nColumnas disponibles en el dataset:")
    for col in df.columns:
        print(f"  - {col}")
    
    # Ejecutar análisis
    try:
        analyze_architecture(df, output_dir)
        analyze_thermal_management(df, output_dir)
        analyze_scalability(df, output_dir)
        analyze_materials(df, output_dir)
        analyze_timeline(df, output_dir)
        analyze_correlations(df, output_dir)
        generate_statistical_report(df, output_dir)
        
        print("\n" + "="*70)
        print("ANÁLISIS COMPLETADO")
        print("="*70)
        print(f"\nTodos los gráficos y reportes guardados en:")
        print(f"  {output_dir}")
        print("\nArchivos generados:")
        for file in sorted(output_dir.glob("*.png")):
            print(f"  📊 {file.name}")
        for file in sorted(output_dir.glob("*.txt")):
            print(f"  📄 {file.name}")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n✗ Error durante el análisis: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
