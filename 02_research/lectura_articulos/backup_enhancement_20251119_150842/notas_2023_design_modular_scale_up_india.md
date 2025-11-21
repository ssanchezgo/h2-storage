# Notas de Lectura: Design and modular scale-up of shell and tube metal hydride hydrogen storage reactor utilizing multi-pass water flow


**Autor:** Satyaki Chandra, Pratibha Sharma, P. Muthukumar, Sankara Sarma V. Tatiparti

**Revista:** Energy


**Revista:** Energy

**Referencia BibTeX:** `chandra2024design`

**Fecha de Publicación:** 2024

---

## 1. Resumen


Este artículo investiga el diseño y la optimización de reactores de almacenamiento de hidrógeno de hidruro metálico (MH) del tipo carcasa y tubos, centrándose en el impacto de un flujo de agua de múltiples pasadas para la gestión térmica. Se simularon reactores con diferentes diámetros de carcasa y arreglos de tubos para albergar 25 kg de LaNi5. El estudio identifica un diseño equilibrado (141.3 mm de diámetro exterior, 60 tubos) que reduce significativamente el tiempo de absorción de hidrógeno al usar un esquema de cuatro pasadas de agua en comparación con una sola pasada. Posteriormente, este diseño optimizado se escala modularmente a una capacidad de 100 kg de LaNi5, conectando cuatro reactores en serie y en paralelo. Los resultados muestran que la configuración en serie es más eficiente a bajos caudales de agua, mientras que a caudales altos, ambas configuraciones (serie y paralelo) tienen un rendimiento similar. El objetivo principal es mejorar la cinética de la reacción de absorción mediante una refrigeración superior, abordando la pobre conductividad térmica de los lechos de MH.

## 2. Imagen de Referencia


![Imagen de referencia](../../../01_design/img/modular_scale_up_india_2023.png)

## 3. Puntos Clave y Datos


### Aspectos Principales


- **Diseño Modular y Escalabilidad:** El estudio demuestra un método claro para escalar la capacidad de almacenamiento de 25 kg a 100 kg mediante un enfoque modular, conectando múltiples reactores. Esto es fundamental para aplicaciones prácticas que requieren mayores capacidades de hidrógeno.

- **Gestión Térmica Multi-paso:** La novedad clave es el uso de un flujo de agua de múltiples pasadas (4 pasadas) en un diseño de carcasa y tubos, lo cual es común en intercambiadores de calor pero no en reactores de MH. Esto mejora significativamente la transferencia de calor.

- **Trade-off en el Diseño:** Existe un compromiso (trade-off) entre el volumen ocupado por los tubos del intercambiador de calor y el rendimiento de la absorción. Más tubos mejoran la transferencia de calor pero reducen el volumen disponible para el hidruro.

- **Rendimiento Serie vs. Paralelo:** La configuración en serie es más rápida a bajos caudales de agua (10 LPM), mientras que a caudales más altos (40 LPM), el rendimiento de las configuraciones en serie y paralelo es comparable.

## 4. Características Técnicas del Sistema


### 4.1 Hidruro Metálico


**Tipo de hidruro:** LaNi5
**Cantidad de hidruro:** 25 kg por reactor (total 100 kg en el sistema escalado)
**Conductividad Térmica MH (efectiva):** 1.2 W/m*K

### 4.2 Configuración Geométrica


**Descripción del sistema:** Reactor de tipo carcasa y tubos (Shell-and-tube) con flujo de agua interno para refrigeración. Se analiza un diseño base de 25 kg y un sistema modular de 100 kg compuesto por cuatro de estos reactores.
**Configuración geométrica:** Cilíndrica
**Diámetro (mm):** Se estudian carcasas de 114.3, 141.3 y 168.3 mm de diámetro exterior. El diseño optimizado es de 141.3 mm.
**Tubos:** El diseño optimizado contiene 60 tubos para el intercambiador de calor.

### 4.3 Transferencia de Calor


**Intercambiador de Calor:** Tipo carcasa y tubos con un esquema de flujo de agua de 4 pasadas.
**Fluido de transferencia de calor:** Agua

### 4.4 Condiciones de Operación


**Temperatura (degC):** 30 degC (temperatura de entrada del agua)
**Presión de trabajo:** 20 bar (presión de suministro de hidrógeno)
**Flujo (LPM):** 10 LPM y 40 LPM (caudal de agua)

### 4.5 Rendimiento del Sistema


**Tiempo de carga (90%):**

- **Reactor único (25 kg, 4 pasadas):** ~320 segundos

- **Reactor único (25 kg, 1 pasada):** ~380 segundos

- **Sistema modular en serie (100 kg, 10 LPM):** 320, 425, 545 y 665 s para cada reactor.

- **Sistema modular en paralelo (100 kg, 10 LPM):** 625 s para cada reactor.

**Cantidad H2:** 25 kg de LaNi5 por módulo.

## 5. Importancia de Reactores Modulares y Gestión Térmica


**Reactores Modulares:**
El enfoque modular es crucial para la escalabilidad de los sistemas de almacenamiento de hidrógeno. En lugar de diseñar un único reactor masivo de 100 kg (lo cual sería complejo y costoso de fabricar y manejar), el estudio utiliza cuatro módulos de 25 kg.

- **Ventajas:**
 - **Fabricación Simplificada:** Es más fácil y económico fabricar múltiples reactores estandarizados más pequeños.
 - **Flexibilidad Operativa:** Permite operar con una capacidad parcial si es necesario, o realizar mantenimiento en un módulo sin detener todo el sistema.
 - **Escalabilidad Lineal:** Se puede aumentar la capacidad total simplemente añadiendo más módulos.
 - **Transporte e Instalación:** Módulos más pequeños son más fáciles de transportar e instalar.

**Gestión Térmica:**
La gestión térmica es el factor más crítico que limita el rendimiento de los reactores de MH. La reacción de absorción es exotérmica y, sin una eliminación de calor eficiente, la temperatura del lecho de hidruro aumenta, lo que a su vez eleva la presión de equilibrio y detiene o ralentiza drásticamente la absorción de hidrógeno.

- **Solución del Artículo:**
 - **Flujo Multi-paso:** El uso de un flujo de agua de 4 pasadas aumenta la velocidad del agua dentro de los tubos (para un caudal total fijo), lo que mejora el coeficiente de transferencia de calor.
 - **Diseño Carcasa y Tubos:** Este diseño maximiza la superficie de contacto entre el lecho de hidruro y la superficie de enfriamiento (los tubos).
 - **Impacto Directo:** Una mejor gestión térmica se traduce directamente en tiempos de carga más rápidos, como se demuestra con la reducción del tiempo de 380 s (1 pasada) a 320 s (4 pasadas).

## 6. Conclusiones y Observaciones


**Resultados principales:**

- Un diseño de carcasa y tubos con un diámetro de 141.3 mm y 60 tubos ofrece el mejor compromiso entre capacidad de almacenamiento y rendimiento de absorción.

- El esquema de 4 pasadas de agua es un 15-20% más rápido que el de una sola pasada para la absorción de hidrógeno en las condiciones estudiadas.

- Para sistemas modulares a gran escala, la configuración en serie es superior a bajos caudales de refrigerante, pero ambas son equivalentes a caudales altos. Esto ofrece flexibilidad en el diseño del sistema de bombeo.

**Recomendaciones:**
El estudio valida que los diseños modulares con gestión térmica mejorada (multi-paso) son una vía prometedora para sistemas de almacenamiento de hidrógeno prácticos y a gran escala.

---

### Notas Adicionales


Este artículo proporciona una metodología de diseño muy clara y datos cuantitativos sobre cómo escalar un reactor de MH. La comparación entre configuraciones en serie y en paralelo es particularmente útil para el diseño de sistemas a escala industrial.
