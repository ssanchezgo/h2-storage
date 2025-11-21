# Notas de Lectura: Thermal management of metal hydride hydrogen storage tank coupled with proton exchange membrane fuel cells


**Autor:** Liang Tong, Chengqing Yuan, Tianqi Yang, Yupeng Yuan, Richard Chahine, Jinsheng Xiao

**Revista:** Energy


**Referencia BibTeX:** `tong2023thermal`

**Fecha de Publicación:** 2023

---

## 1. Resumen


Este estudio investiga la gestión térmica integrada entre un tanque de almacenamiento de hidrógeno con hidruro metálico (MH) y una celda de combustible de membrana de intercambio de protones (PEMFC). El trabajo desarrolla y valida un modelo de parámetros agrupados para el sistema PEMFC-MH completo. La innovación principal radica en el aprovechamiento del calor residual producido por la PEMFC para calentar el lecho de MH durante la deshidrogenación, mejorando así la eficiencia energética global del sistema. Los resultados demuestran que es factible usar el calor de desecho de la PEMFC para proporcionar el calor necesario para la liberación de hidrógeno del tanque MH. El grado de apertura de una válvula de tres vías se identifica como una medida de control efectiva para ajustar la tasa de suministro de hidrógeno según diferentes requerimientos de potencia. El sistema fue diseñado para aplicaciones en transporte fluvial y vehículos ligeros, demostrando que aproximadamente el 21% del calor generado por la PEMFC es suficiente para mantener la deshidrogenación del lecho MH.

## 2. Imagen de Referencia


![Imagen de referencia](../../../01_design/img/thermal_management_pemfc_mh_2023.png)

## 3. Puntos Clave y Datos


### Aspectos Principales


- **Integración Térmica PEMFC-MH:** El calor residual de la celda de combustible se reutiliza para calentar el tanque de hidruro metálico, eliminando la necesidad de una fuente de calor externa para la deshidrogenación.

- **Control mediante Válvula de Tres Vías:** El grado de apertura de la válvula (parámetro "a") permite distribuir el flujo de agua de enfriamiento entre el tanque MH y un intercambiador de calor ambiental, proporcionando un control preciso de la temperatura.

- **Aplicación en Transporte Fluvial:** El sistema está diseñado específicamente para embarcaciones de río propulsadas por hidrógeno, donde los requisitos de potencia son moderados y las rutas son cortas.

- **Operación a Baja Presión:** El tanque MH opera a presiones mucho menores (< 4 bar) que los tanques de hidrógeno comprimido convencionales (350-700 bar), reduciendo costos de seguridad y reabastecimiento.

## 4. Características Técnicas del Sistema


### 4.1 Hidruro Metálico


**Tipo de hidruro:** LaNi5H6
**Cantidad de hidruro:** 12.95 kg
**Conductividad Térmica MH:** No especificada directamente (se utiliza modelo de parámetros agrupados)
**Capacidad de almacenamiento:** 177.4 g de H2 (1.37 wt%)

### 4.2 Configuración Geométrica


**Descripción del sistema:** Tanque cilíndrico con intercambiador de calor de tubo recto interno. El agua de enfriamiento de la PEMFC circula a través del tubo para calentar el lecho de MH durante la deshidrogenación.
**Configuración geométrica:** Cilíndrica con tubo de enfriamiento interno recto
**Diámetro externo:** 130 mm
**Diámetro interno:** 110 mm
**Longitud total del tanque:** 600 mm
**Longitud del tubo de enfriamiento:** 580 mm
**Diámetro del tubo de enfriamiento:** 12 mm (diámetro externo)
**Volumen del lecho MH:** ~70% del volumen total del tanque
**Porosidad:** 0.5

### 4.3 Transferencia de Calor


**Intercambiador de Calor:** Tubo recto interno por el que circula agua de refrigeración
**Área de intercambio de calor:** 0.02187 m2
**Coeficiente de transferencia de calor:** Calculado mediante correlación de Sieder-Tate (ecuación 16 del artículo)
**Fluido de transferencia de calor:** Agua

### 4.4 Condiciones de Operación


**Temperatura inicial MH:** 323 K (50degC)
**Temperatura de operación PEMFC:** 323 K (50degC)
**Presión inicial:** 4.576 bar
**Presión máxima de operación:** ~3.5 bar
**Presión mínima requerida:** 1.1 bar (para suministro directo sin compresor adicional)
**Flujo de agua de enfriamiento:** 0.02608 kg/s
**Tasa de suministro de H2:** 15.17 L/min (2.25 * 10−2 g/s) en condición nominal

### 4.5 Rendimiento del Sistema


**Potencia de la PEMFC:** ~926.5 W (potencia nominal con 45 celdas de 50 cm2 cada una)
**Tiempo de operación continua:** ~2 horas con una carga completa del tanque MH
**Tiempo para liberar 95% del H2:** ~7500 s (~2.08 h) con apertura de válvula a = 0.5
**Eficiencia de aprovechamiento de calor:** Máximo 21% del calor generado por PEMFC es transferido al tanque MH

## 5. Importancia de la Gestión Térmica para Diseño Modular


**Por qué es crítica la gestión térmica:**

La gestión térmica en sistemas MH-PEMFC es fundamental por las siguientes razones:

1. **Naturaleza Endotérmica de la Desorción:** La liberación de hidrógeno desde el hidruro metálico es una reacción endotérmica que requiere un suministro continuo de calor. Sin una fuente de calor adecuada, la temperatura del lecho disminuye, lo que reduce drásticamente la presión de equilibrio y, por ende, la tasa de liberación de hidrógeno.

2. **Aprovechamiento de Calor Residual:** Las celdas de combustible PEMFC generan una cantidad significativa de calor residual (típicamente 50-60% de la energía del hidrógeno se convierte en calor). Aprovechar este calor para la deshidrogenación del MH mejora la eficiencia energética global del sistema y reduce la necesidad de sistemas de enfriamiento externos para la PEMFC.

3. **Control de Cinética de Reacción:** La velocidad de deshidrogenación está directamente relacionada con la temperatura del lecho. Una gestión térmica efectiva permite controlar activamente la tasa de suministro de hidrógeno para satisfacer la demanda variable de potencia de la aplicación.

**Métodos de transferencia de calor utilizados:**

- Intercambiador de calor de tubo interno con circulación de agua

- Sistema de válvula de tres vías para distribuir el flujo de agua caliente entre el tanque MH y un radiador ambiental

- Uso de modelo de parámetros agrupados que simplifica el análisis térmico

**Materiales y propiedades térmicas:**

- LaNi5H6: Entalpía de reacción dH = 30.8 kJ/mol, Entropía dS = 108 J/mol*K

- Agua como fluido de transferencia de calor (cp = 4185 J/kg*K)

**Eficiencia térmica:**

- Hasta un 21% del calor generado por la PEMFC puede ser transferido al tanque MH en condiciones óptimas

- El resto del calor es disipado al ambiente mediante el intercambiador de calor

**Problemas y soluciones relacionados con el manejo térmico:**

- **Problema:** Distribución no uniforme de temperatura en el lecho MH puede limitar la tasa de deshidrogenación.

- **Solución:** Uso de un tubo de enfriamiento interno que atraviesa todo el lecho para proporcionar una fuente de calor distribuida.

- **Problema:** Balance entre la potencia de la PEMFC y el calor disponible para el tanque MH.

- **Solución:** Control mediante válvula de tres vías que ajusta la fracción del flujo de agua que pasa por el tanque MH (parámetro "a").

## 6. Relevancia para Diseño Modular Escalable


**Para Sistemas Modulares:**

Este estudio demuestra un enfoque integrado que es inherentemente modular:

- **Módulo PEMFC:** Un stack de 45 celdas (~1 kW). Para aplicaciones de mayor potencia, se pueden conectar múltiples stacks en paralelo o serie.

- **Módulo MH:** Un tanque de 12.95 kg de LaNi5. El artículo menciona explícitamente que "para aplicaciones de energía de hidrógeno con potencia relativamente grande, como montacargas impulsados por hidrógeno en puertos y embarcaciones propulsadas por PEMFC en ríos, se pueden diseñar e integrar múltiples tanques MH como un todo para satisfacer la demanda de suministro de hidrógeno."

- **Sistema de Gestión Térmica:** El circuito de agua con válvula de tres vías puede escalarse para incluir múltiples tanques MH conectados en paralelo o serie.

**Ventajas del Diseño Modular:**
1. **Escalabilidad:** Fácil ajuste de la capacidad de almacenamiento y potencia según la aplicación.
2. **Redundancia:** Si un módulo falla, el sistema puede seguir operando con capacidad reducida.
3. **Mantenimiento:** Los módulos individuales pueden ser reemplazados o recar gados sin detener todo el sistema.
4. **Optimización:** Cada módulo puede operar en su punto de eficiencia óptimo.

## 7. Conclusiones y Observaciones


**Resultados principales:**

- Es técnica y económicamente factible usar el calor residual de una celda de combustible PEMFC para mantener la deshidrogenación de un tanque de hidruro metálico.

- El grado de apertura de la válvula de tres vías es un parámetro de control crítico que permite ajustar la distribución de calor entre el tanque MH y el radiador ambiental.

- El sistema puede operar continuamente durante aproximadamente 2 horas con una carga completa del tanque MH para una PEMFC de ~1 kW.

- Para aplicaciones de mayor escala, la integración modular de múltiples tanques MH es una estrategia viable y recomendada.

**Recomendaciones:**

- Para aplicaciones con demanda de potencia variable, implementar un sistema de control automático que ajuste el grado de apertura de la válvula en tiempo real.

- Considerar el uso de otros hidruros metálicos de baja temperatura (como TiFe) para futuras iteraciones del diseño.

- Explorar configuraciones de tanques múltiples conectados tanto en serie como en paralelo para optimizar el tiempo de respuesta y la capacidad total.

- Incluir un compresor o bomba de hidrógeno de baja potencia para mantener el suministro cuando la presión del tanque cae por debajo de 1.1 bar y aún queda hidrógeno almacenado.

## 8. Referencias Adicionales


- Modelos de parámetros agrupados para tanques MH validados en trabajos previos de los autores

- Datos experimentales de PEMFC de 50 cm2 de área activa

- Correlaciones de transferencia de calor de Sieder-Tate para flujo en tubos

---

### Notas Adicionales


Este trabajo es particularmente relevante para el diseño de sistemas modulares escalables porque proporciona un modelo matemático validado y relativamente simple (parámetros agrupados) que puede ser utilizado para la optimización y el control en tiempo real de sistemas MH-PEMFC integrados. La demostración de que solo el 21% del calor de la PEMFC es necesario para la deshidrogenación sugiere que el mismo enfoque podría aplicarse a sistemas de mayor potencia sin saturar la capacidad térmica del tanque MH. La mención explícita de la escalabilidad modular como estrategia para aplicaciones de alta potencia refuerza la viabilidad de este enfoque para sistemas comerciales e industriales.
