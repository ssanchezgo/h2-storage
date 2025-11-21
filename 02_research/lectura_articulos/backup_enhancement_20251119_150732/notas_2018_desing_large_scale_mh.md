# Notas de Lectura: Design of Large-scale Metal Hydride Storage Systems


**Autor:** Kumar, S., Kojima, Y., Dutta, I., Varma, A.

**Referencia BibTeX:** `kumar2018`

**Fecha de Publicación:** 2018

---

## 1. Resumen


Este estudio aborda el escalamiento de sistemas de almacenamiento de hidrógeno basados en hidruros metálicos (MH) para aplicaciones industriales, presentando un marco de diseño integral para sistemas de gran escala (1000 kg H2). Se analiza configuración modular, gestión térmica, seguridad y viabilidad económica con módulos de 0.5-1.0m diámetro y 2-4m longitud.

## 2. Imagen de Referencia


![Diseño del sistema a gran escala](img/notas_2018_desing_large_scale_mh.png)

## 3. Puntos Clave y Datos


### Aspectos Principales


- Capacidad: 1000 kg H2 en configuración modular (10-20 unidades)

- Volumen total: 50-100 m3, peso sistema: 80-120 ton

- Gestión térmica crítica: 14.6 kW/kg H2, pico térmico: 2-3 MW

- Sistema tubo-carcasa SS316L con área contacto: 2-4 m2/m3

- Costos capital: reactores 40-50%, intercambiadores 20-25%

- Recuperación calor: 60-70%, energía: 2-3 kWh/kg H2

## 4. Características Técnicas del Sistema


### 4.1 Hidruro Metálico


- **Tipo de hidruro:** Variable según aplicación (no especificado en resumen)

- **Cantidad de hidruro:** 1000 kg H2 capacidad total del sistema

- **Conductividad Térmica MH:** Según tipo de MH seleccionado

### 4.2 Configuración Geométrica


- **Descripción del sistema:** Sistema modular con 10-20 reactores cilíndricos en paralelo, intercambiador tubo-carcasa SS316L, redundancia N+1, control PID cascada

- **Configuración geométrica:** Cilíndrica modular en paralelo

- **Longitud (mm):** 2000-4000 por módulo

- **Diámetro (mm):** 500-1000 por módulo

- **L/D ratio:** 3-4

- **Volumen (L):** 50000-100000 (50-100 m3 total)

### 4.3 Transferencia de Calor


- **Intercambiador de Calor:** Tubo-carcasa SS316L, área contacto 2-4 m2/m3, sistema dual redundante

- **Coeficiente de transferencia de calor:** dT diseño: 40-60 K

### 4.4 Condiciones de Operación


- **Temperatura (degC):** Máxima: 80-100 (353-373K), Mínima: 20-40 (293-313K)

- **Presión de trabajo:** Carga: 30-50 bar, Descarga: 5-10 bar

- **Flujo (NL/min):** Carga H2: 100-200 kg/h, Descarga: 50-100 kg/h, Refrigerante: 20-40 m3/h

### 4.5 Rendimiento del Sistema


- **Tiempo carga:** Tiempo respuesta: 10-15 min para pico térmico

- **Cantidad H2:** 1000 kg capacidad total

## 5. Transferencia de Calor


**Métodos de transferencia de calor utilizados:**

- Intercambiador tubo-carcasa principal tipo SS316L

- Red de distribución térmica en paralelo con redundancia

- Control PID cascada con monitoreo en tiempo real

- Sistema de enfriamiento dual para backup

**Materiales y propiedades térmicas:**

- Cuerpo: Acero inoxidable SS316L

- Área de contacto térmica: 2-4 m2/m3

- dT de diseño: 40-60 K

- Sistema modular para optimizar transferencia

**Eficiencia térmica:**

- Calor generado (absorción): 14.6 kW/kg H2

- Calor requerido (desorción): 14.6 kW/kg H2

- Pico térmico: 2-3 MW durante carga

- Recuperación de calor: 60-70%

- Tiempo respuesta térmica: 10-15 min

**Problemas y soluciones relacionados con el manejo térmico:**

- Problema: Pico térmico de 2-3 MW durante carga

- Solución: Sistema modular con intercambiadores redundantes

- Problema: Control de temperatura en gran escala

- Solución: Control PID cascada con monitoreo tiempo real

- Problema: Pérdidas térmicas en sistema grande

- Solución: Recuperación de calor 60-70% e integración térmica

## 6. Conclusiones y Observaciones


**Resultados principales:**

- Escalabilidad técnicamente viable para 1000 kg H2

- Control térmico robusto con sistema modular 10-20 unidades

- Seguridad garantizada con redundancia N+1 y sistemas fail-safe

- CAPEX dominado por reactores MH (40-50%) e intercambiadores (20-25%)

- Costos operativos: energía 2-3 kWh/kg H2, personal 2-3 operadores/turno

- Mantenimiento: 3-5% CAPEX/año, arranque: 60-90 min

- Recuperación calor: 60-70% mejora eficiencia energética

**Recomendaciones:**

- Optimizar geometría modular para reducir peso sistema (80-120 ton actual)

- Mejorar integración térmica para aumentar recuperación de calor >70%

- Aumentar densidad energética volumétrica del sistema

- Implementar control avanzado predictivo para optimizar ciclos

- Reducir costos de fabricación mediante producción en serie

- Maximizar automatización de procesos operativos

- Evaluar integración con procesos industriales para aprovechamiento térmico

## 7. Referencias Adicionales


- Kojima et al. (2017) "Industrial-scale metal hydride tanks"

- Varma et al. (2016) "Scale-up considerations for MH systems"

- Dutta et al. (2018) "Economic analysis of H2 storage"

- ISO 16111:2018 "H2 Storage Systems"

- ASME BPVC Section VIII "Pressure Vessels"

- NFPA 2 "Hydrogen Technologies Code"

---

### Notas Adicionales


Sistema de protección incluye sensores H2 catalíticos, monitoreo RTD, válvulas fail-safe y venteo automático. UPS para 2 horas. Tiempo respuesta emergencias <1 min con aislamiento automático. Instalación incluye obra civil (15-20%), montaje (10-15%), instrumentación (8-12%). Software diseño: Aspen Plus, COMSOL. Limitaciones: alto CAPEX inicial, inercia sistema, espacio requerido.
