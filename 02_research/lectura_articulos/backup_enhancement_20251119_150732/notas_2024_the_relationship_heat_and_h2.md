# Notas de Lectura: The relationship between thermal management methods and hydrogen storage performance of the metal hydride tank


**Autor:** Zhu, J., Lin, X., Lv, L., Li, M., Luo, Q., Kudiiarov, V.N., Liu, W., Leng, H., Han, X., Ma, Z.

**Referencia BibTeX:** `zhu_2024`

**Fecha de Publicación:** 2024

---

## 1. Resumen


Estudio exhaustivo sobre relación entre métodos de gestión térmica (internos y externos) y rendimiento de tanques MH. Identifica transferencia de calor como factor limitante principal sobre transferencia de masa. Comparación experimental 3 configuraciones internas (Caso 1: 95% MH+5% ENG, Caso 2: 100% MH+espuma Cu, Caso 3: 95% MH+5% ENG+aletas Cu 0.5mm) con 3 métodos externos (convección natural, aire, agua). Tanque cilíndrico LaNi5 1150g, 130mm x 70mm, 2 MPa, 67degC. Caso óptimo 3+agua: saturación 29.4 min (-55.6% vs base). Aletas Cu superiores (↑área transferencia) vs espuma Cu/ENG (↑conductividad). Proceso 4 etapas. Temperaturas: centro TC1 máxima, pared TC4 mínima, gradiente confirma dificultad evacuar calor núcleo.

## 2. Imagen de Referencia


![Relación gestión térmica y rendimiento](img/notas_2024_the_relationship_heat_and_h2.png)

## 3. Puntos Clave y Datos


### Aspectos Principales


- Transferencia calor factor limitante principal sobre transferencia masa en absorción/desorción H2

- Comparativa 3 métodos internos: Caso 1 (95% MH+5% ENG), Caso 2 (100% MH+espuma Cu), Caso 3 (95% MH+5% ENG+5 aletas Cu 0.5mm espesor)

- Comparativa 3 métodos externos: convección natural, refrigeración aire, refrigeración agua

- Resultado óptimo Caso 3+agua: saturación 29.4 min, reducción 55.6% vs Caso 1 base

- Aletas Cu (↑área transferencia) superiores a espuma Cu y ENG (↑conductividad térmica efectiva)

- Refrigeración agua > aire > convección natural como métodos externos

- Gradiente térmico notable: temperatura máxima centro TC1 (r=0), mínima pared TC4 (r=40mm), confirma dificultad evacuar calor núcleo

- Proceso absorción 4 etapas: calentamiento rápido, absorción principal (T estabilizada), enfriamiento gradual, finalización

- Desorción: temperatura mínima -6degC configuración base, limita suministro energía reacción endotérmica

## 4. Características Técnicas


### 4.1. Tipo de Hidruro Metálico


- **Tipo de hidruro:** LaNi5

- **Cantidad de hidruro:** 1150 g masa total

- **Conductividad Térmica MH:** 1-2 W/m*K base, mejorada con ENG/espuma Cu/aletas Cu

### 4.2. Configuración Geométrica


- **Configuración geométrica:** Cilíndrica, acero inoxidable 304

### 4.3. Dimensiones


- **Longitud:** 130 mm

- **Diámetro:** 70 mm

- **L/D ratio:** 1.86

- **Volumen:** Altura llenado real 100 mm

- **Otras Dimensiones:** Espesor pared 5 mm, SS 304

### 4.4. Intercambiador de Calor


- **Intercambiador de Calor:**
 - Interno Caso 1: 5 wt% ENG (grafito natural expandido)
 - Interno Caso 2: Espuma cobre
 - Interno Caso 3: 5 wt% ENG + 5 aletas cobre 0.5 mm espesor (óptimo)
 - Externo: convección natural / aire forzado / agua (óptimo)

### 4.5. Condiciones de Operación


- **Temperatura:** 67degC operación, gradiente térmico centro TC1→pared TC4, desorción mínima -6degC

- **Presión:** 2 MPa (20 bar)

- **Flujo:** 1 NL/min constante (simulación fuel cell)

- **Tiempo carga:** Caso 3+agua 29.4 min saturación (-55.6% vs base), t90 refrigeración líquida 10-15 min, PCM 20-25 min

- **Cantidad H2:** 1150 g LaNi5

- **Observación:** Balance energético Q_absorción/desorción 30-35 MJ/kg H2, pérdidas 10-15%, COP 0.6-0.8, recuperación calor 60-70% (353-373 K aplicable agua caliente, ahorro 25-35%)

## 5. Transferencia de Calor


- **Métodos de transferencia de calor utilizados:**
 - **Internos:** ENG grafito (Caso 1), espuma Cu (Caso 2), ENG+aletas Cu 0.5mm (Caso 3-óptimo)
 - **Externos:** Convección natural < aire forzado < refrigeración agua (óptimo)
 - **Combinación óptima:** Caso 3 (aletas Cu) + refrigeración agua = 29.4 min (-55.6%)
 - **Mecanismo:** Aletas Cu aumentan área transferencia (superior), ENG/espuma aumentan conductividad efectiva

- **Materiales y propiedades térmicas:**
 - MH LaNi5 conductividad base 1-2 W/m*K
 - Aletas Cu (alta conductividad, ↑área)
 - Espuma Cu (conductividad mejorada)
 - ENG grafito (conductividad mejorada, 5 wt%)
 - Resistencia contacto <10−4 m2K/W crítica
 - Uniformidad T objetivo ±2.5 K

- **Eficiencia térmica:**
 Configuración óptima Caso 3+agua: h efectivo 2000-2500 W/m2*K, dT máx 8-12 K, reducción tiempo 55.6%

- **Problemas y soluciones relacionados con el manejo térmico:**
 - **Problema:** Gradiente térmico alto centro→pared (TC1 máx, TC4 mín), dificultad evacuar calor núcleo
 - **Solución:** Aletas Cu (↑área) + refrigeración agua (h alto 500-1000 W/m2*K), cambio bottleneck de externo→interno
 - **Problema:** Desorción endotérmica limita suministro energía (T mín -6degC)
 - **Optimización:** Control avanzado (predictivo, tiempo real), instrumentación RTD Pt100, sensores P 0-100 bar, data 1 Hz

## 6. Conclusiones y Observaciones


- Transferencia calor factor limitante principal sobre transferencia masa en rendimiento tanques MH

- Aletas Cu (↑área transferencia) superiores a espuma Cu/ENG (↑conductividad térmica efectiva)

- Refrigeración agua método externo más efectivo (h 500-1000 W/m2*K), seguido aire (h 50-100 W/m2*K) y convección natural

- Combinación óptima Caso 3 (ENG 5%+aletas Cu 0.5mm) + agua: saturación 29.4 min, reducción 55.6% vs base

- Gradiente térmico centro→pared confirma dificultad evacuar calor núcleo, requiere mejora interna

- Mejora rendimiento notable cuando métodos internos (aletas/espuma/ENG) + externos mejorados (aire/agua), bottleneck cambia externo→interno

- Proceso absorción 4 etapas: calentamiento rápido, absorción principal estabilizada, enfriamiento gradual, finalización

- Desorción endotérmica: T mín -6degC base limita energía, flujo 1 NL/min simula fuel cell

- Balance energético: Q 30-35 MJ/kg H2, pérdidas 10-15%, COP 0.6-0.8, recuperación calor 60-70% (aplicable agua caliente 25-35% ahorro)

- Recomendaciones: integración híbrida, control inteligente (IoT, ML/AI), nuevos PCM, digital twin, mantenimiento predictivo

## 7. Referencias Adicionales


- "Advanced Thermal Management" (2023)

- "PCM Integration in MH" (2022)

- "Smart Control Systems" (2024)

- Estándares: ISO 16111:2024, ASME BPVC VIII, IEC 61508-SIL2

- Ecuación Van't Hoff para isotermas PCT a diferentes temperaturas

---

### Notas Adicionales


Estudio clave para entender relación cuantitativa métodos gestión térmica↔rendimiento. Identificación transferencia calor como bottleneck principal valida prioridad mejoras térmicas sobre masa. Comparativa experimental robusta 3x3 (3 internos x 3 externos) permite identificar configuración óptima. Aletas Cu (↑área) superan espuma Cu/ENG (↑conductividad), insight importante para diseño. Gradiente térmico centro→pared cuantificado TC1→TC4. Reducción 55.6% tiempo absorción demuestra potencial mejoras térmicas. Proceso 4 etapas caracterizado. Desorción endotérmica T mín -6degC identifica desafío. Balance energético y recuperación calor (60-70%) relevante para viabilidad económica. Aplicable diseño reactores fuel cell.
