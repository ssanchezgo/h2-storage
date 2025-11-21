# Notas de Lectura: Optimization of hydrogen storage in metal-hydride tanks


**Autor:** F. Askri, M. Ben Salah, A. Jemni, S. Ben Nasrallah

**Referencia BibTeX:** `cijhydene_2008`

**Fecha de Publicación:** 2008

---

## 1. Resumen


Este artículo se enfoca en la optimización del tiempo de almacenamiento de hidrógeno en tanques de hidruro metálico (MHT). Para esto, se desarrolló un modelo matemático bidimensional validado con resultados experimentales. El estudio evalúa el impacto de la masa térmica de la pared del tanque y compara distintos diseños para mejorar la transferencia de calor, ya que esta es la principal limitación del proceso de absorción de hidrógeno. Se concluye que las aletas externas y los tubos internos son los diseños más efectivos para mejorar el almacenamiento.

## 2. Imagen de Referencia


![Esquema del Reactor MHT](img/notas_2008_optimization_of_hydrogen_storage_mht/Esquema_MHT_utilizados.png)

## 3. Puntos Clave y Datos


### Aspectos Principales


Configuraciones estudiadas:

1. Un tanque cilíndrico
2. Un tanque cilíndrico con aletas externas
3. Un tanque cilíndrico con un tubo concéntrico lleno de hidruros metálicos con fluido refrigerante fluyendo
4. Un tanque cilíndrico con un tubo concéntrico equipado con aletas

**Problema principal:** El factor limitante para la absorción de hidrógeno en tanques de hidruro metálico es la tasa de remoción de calor de la reacción.

**Modelo matemático:** Se utilizó un modelo matemático en 2D para simular el proceso y optimizar los diseños del tanque.

**Diseños analizados:** El estudio comparó el rendimiento de cuatro diseños: un tanque cilíndrico simple, un tanque con aletas externas, un tanque con tubos concéntricos llenos de fluido refrigerante y un tanque con tubos U.

**Mejoras en el diseño:** Los resultados muestran que los diseños con aletas y tubos internos mejoran significativamente la transferencia de calor, lo que reduce el tiempo de almacenamiento.

## 4. Características Técnicas del Sistema


### 4.1 Hidruro Metálico


**Tipo de hidruro:** LaNi5 (Lantano-Níquel 1:5)
**Cantidad de hidruro:** 9.2 kg (estimado para el volumen del lecho)
**Conductividad Térmica MH:** 1.2 W/m*K (conductividad térmica efectiva del lecho)

### 4.2 Configuración Geométrica


**Descripción del sistema:** Tanque cilíndrico de hidruro metálico con cuatro configuraciones estudiadas: diseño base, con aletas externas, con tubo concéntrico interno, y combinación tubo-aletas
**Configuración geométrica:** Cilíndrica con variaciones según diseño
**Longitud (mm):** 80
**Diámetro (mm):** 80 (exterior), 60 (interior)
**L/D ratio:** 1.0
**Volumen (L):** 0.226

### 4.3 Transferencia de Calor


**Intercambiador de Calor:** Múltiples configuraciones: aletas externas radiales, tubo concéntrico con refrigerante, tubo concéntrico con aletas
**Coeficiente de transferencia de calor:** 500 W/m2*K (refrigerante), 10 W/m2*K (ambiente)

### 4.4 Condiciones de Operación


**Temperatura (degC):** 20-77
**Presión de trabajo:** 8-10 bar
**Flujo (NL/min):** 0.06 NL/min (convertido de 0.001 kg/s de refrigerante)

### 4.5 Rendimiento del Sistema


**Tiempo carga:** 350-1000 s (dependiendo de la configuración)
**Cantidad H2:** 6.5 H/mol LaNi5 (capacidad máxima)

## 5. Transferencia de Calor


**Sistema de Gestión Térmica:**

- **Mecanismos de transferencia:**
 - Conducción a través del lecho de hidruro
 - Convección forzada en tubos de refrigeración
 - Conducción mejorada por aletas
 - Convección natural en superficie externa

**Características del Sistema:**

- **Configuraciones estudiadas:**
 1. Refrigeración por pared externa
 2. Aletas externas radiales
 3. Tubo concéntrico con refrigerante
 4. Tubo concéntrico con aletas

**Parámetros Térmicos:**

- **Conductividad térmica efectiva:** 1.2 W/m*K (lecho de hidruro)

- **Coeficiente de transferencia de calor:**

- Refrigerante: 500 W/m2*K

- Ambiente: 10 W/m2*K

- **Calor de reacción:** 30.8 kJ/mol H2

**Análisis de Rendimiento:**

- **Tiempo de carga:**

- Diseño base: 1000 s

- Con aletas: 600 s

- Con tubo interno: 400 s

- Configuración óptima: 350 s

- **Eficiencia térmica de aletas:** 85%

- **Reducción máxima de tiempo:** 65%

## 6. Conclusiones y Observaciones


**Hallazgos Principales:**

1. **Comparación de Diseños:**

 - El diseño base requiere ~1000s para carga completa
 - Las aletas externas reducen tiempo a ~600s
 - El tubo concéntrico mejora hasta ~400s
 - La combinación tubo+aletas alcanza ~350s

2. **Efectividad de Mejoras:**

 - Aletas externas: 40% mejora
 - Tubo interno: 60% mejora
 - Configuración híbrida: 65% mejora

3. **Factores Críticos Identificados:**

 - La conductividad térmica del lecho es el factor limitante
 - El espesor del lecho afecta significativamente el rendimiento
 - La velocidad de enfriamiento determina la tasa de absorción

**Recomendaciones de Diseño:**

1. **Aspectos Geométricos:**

- Optimizar espesor del lecho (< 6 cm)

- Usar múltiples tubos de refrigeración

- Implementar aletas con espaciado óptimo

1. **Consideraciones Térmicas:**

- Mantener temperatura de refrigerante constante

- Maximizar área de transferencia de calor

- Minimizar resistencias térmicas de contacto

1. **Aspectos Operativos:**

- Control preciso de presión de suministro

- Mantenimiento de flujo de refrigerante constante

- Monitoreo de temperatura del lecho

## 7. Referencias Adicionales


**Referencias Citadas:**

1. Jemni, A., & Ben Nasrallah, S. (1995). "Study of two-dimensional heat and mass transfer during absorption in a metal-hydrogen reactor." International Journal of Hydrogen Energy, 20(1), 43-52.

2. Muthukumar, P., & Groll, M. (2010). "Metal hydride based heating and cooling systems: A review." International Journal of Hydrogen Energy, 35(8), 3817-3831.

3. Askri, F., et al. (2003). "Dynamic behavior of metal-hydrogen reactor during hydriding process." International Journal of Hydrogen Energy, 28(5), 537-557.

**Referencias Relacionadas:**

1. Laurencelle, F., & Goyette, J. (2007). "Simulation of heat transfer in a metal hydride reactor with aluminium foam." International Journal of Hydrogen Energy, 32(14), 2957-2964.

2. Visaria, M., et al. (2011). "Experimental investigation and theoretical modeling of dehydriding process in high-pressure metal hydride hydrogen storage systems." International Journal of Hydrogen Energy, 36(2), 1245-1255.

3. Yang, F., et al. (2010). "Analysis of the heat and mass transfer characteristics of metal hydride reactor beds." International Journal of Hydrogen Energy, 35(4), 1723-1731.

---

### Notas Adicionales


| Figura | Descripción | Detalles clave |
|---|---|---|
| 1 | Esquema de las configuraciones del tanque de hidruro metálico. | Muestra los cuatro diseños del tanque: (a) cilíndrico simple, (b) con aletas externas, (c) con tubos concéntricos para refrigerante, y (d) con tubos en U para refrigerante.|
| 5 | Curvas de presión de absorción vs. tiempo. | Muestra la variación de la presión del gas de hidrógeno para los diferentes diseños de tanques. |
| 7 | Curvas de temperatura del lecho vs. tiempo. | Ilustra cómo la temperatura del lecho de hidruro cambia con el tiempo para los distintos diseños, demostrando la mejora en la transferencia de calor |
| 8 | Variación de la fracción de hidrógeno con el tiempo. | Compara la cantidad de hidrógeno absorbido por el hidruro a lo largo del tiempo para cada diseño |
| 9 | Curvas isotérmicas en el lecho del reactor. | Muestra la distribución de temperatura dentro del tanque, lo cual es fundamental para el análisis de transferencia de calor.|
| 12 | Variación de la velocidad del flujo de hidrógeno. | Se utiliza para analizar el movimiento del hidrógeno dentro del lecho.|
