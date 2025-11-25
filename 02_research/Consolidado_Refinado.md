# Consolidado Técnico Detallado: Artículos de Investigación sobre Almacenamiento de Hidrógeno

Este documento presenta un análisis técnico profundo de los artículos de investigación, destacando datos numéricos específicos (tiempos, temperaturas, presiones, eficiencias), datos geométricos de los reactores y categorizando los estudios por material y estrategia de gestión térmica.

---

## 1. A hydrogen supply system utilizing PEMFC exhaust heat and modular metal hydride tanks for hydrogen-powered bicycles
**Referencia:** Miao et al., *Applied Energy*, 401, 126760 (2025).

**Resumen:** Se propone un sistema compacto de suministro de hidrógeno para bicicletas eléctricas (H-bike) que integra térmicamente tanques de hidruro metálico (MH) con una pila de combustible PEM (PEMFC). El sistema recupera el calor residual de la PEMFC mediante una configuración de tanque dividido y estructura de panal.

**Conclusión:** La estrategia de tanque dividido reduce los gradientes térmicos y mejora la uniformidad. La configuración de panal captura pasivamente el calor residual, logrando una eficiencia de recuperación del 22.62%. El diseño de dos capas alcanza una eficiencia de utilización térmica del 39.90% a 215 W, manteniendo un flujo de H2 de 2000 sccm durante 30 min.
*   **Detalles Técnicos:** Sistema acoplado térmicamente para movilidad ligera.
*   **Datos Geométricos:**
    *   **Estructura:** Panal de abeja (Honeycomb) hexagonal.
    *   **Configuración:** Modular compacta para integración en bicicleta.
*   **Datos Numéricos Clave:**
    *   **Potencia FC:** 215 W.
    *   **Eficiencia Térmica:** 39.90% (diseño de dos capas) vs 22.62% (panal simple).
    *   **Flujo H2:** Sostenido a 2000 sccm durante 30 min (diseño optimizado).
    *   **Estabilidad:** Mantiene flujo de 1000 sccm por >30 min en configuración base.

## 2. The porosity and effective thermal conductivity... of nano-structured FeTi
**Referencia:** Matsumasa et al., *International Journal of Hydrogen Energy* (2019).

**Resumen:** Estudio experimental sobre la porosidad y conductividad térmica efectiva (ETC) de un lecho empacado de FeTi nano-estructurado (n-FeTi). Se observó que el volumen del lecho disminuye con los ciclos de hidrogenación, a diferencia del LaNi5.

**Conclusión:** La compactación del lecho de n-FeTi con los ciclos es beneficiosa para el diseño de tanques. La ETC varía entre 0.4 y 1.1 W/mK, aumentando con la fracción de reacción y la disminución de la porosidad. Estos datos son clave para el modelado numérico.
*   **Detalles Técnicos:** Estudio de propiedades termofísicas dinámicas del n-FeTi.
*   **Datos Geométricos:**
    *   **Escala:** Muestras de laboratorio para medición de propiedades.
    *   **Porosidad:** Variable dinámica durante el ciclo.
*   **Datos Numéricos Clave:**
    *   **Conductividad Térmica Efectiva (ETC):** Varía de 0.4 a 1.1 W/mK.
    *   **Comportamiento:** El volumen del lecho *disminuye* con los ciclos (compactación), a diferencia del LaNi5 que se expande.

## 3. Precise temperature control of fuel cell stacks... using metal hydride based modules
**Referencia:** *International Journal of Hydrogen Energy* (2023).

**Resumen:** Demostración del uso de módulos de MH como almacenamiento térmico activo para el control preciso de temperatura en stacks de celdas de combustible. La presión del gas actúa como variable de control para definir la temperatura de liberación de energía.

**Conclusión:** Se logró estabilizar la temperatura del fluido refrigerante a 70°C ± 1.5 K utilizando un controlador PI basado en la presión. El sistema proporcionó potencias térmicas de 755 W/kgMH en absorción y 140 W/kgMH en desorción, con tiempos de respuesta inferiores a 5 segundos.
*   **Detalles Técnicos:** Uso de MH como buffer térmico activo.
*   **Datos Geométricos:**
    *   **Tipo:** Módulos compactos integrados en la línea de refrigerante.
*   **Datos Numéricos Clave:**
    *   **Material:** LaNi4.85Al0.15.
    *   **Control:** Estabiliza fluido a 70°C ± 1.5 K.
    *   **Potencia Térmica:** +755 W/kgMH (absorción) y -140 W/kgMH (desorción).
    *   **Respuesta:** < 5 segundos ante perturbaciones.

## 4. A modular MgH2 demonstration tank to store reversibly hydrogen
**Referencia:** El Alem et al., *International Journal of Hydrogen Energy*, 155, 150341 (2025).

**Resumen:** Diseño de un tanque modular de MgH2 optimizado para minimizar el tiempo de transferencia de calor. Se utilizó polvo de MgH2 micro-dimensionado y activado. Se realizaron simulaciones numéricas para analizar el impacto de placas calefactoras integradas.

**Conclusión:** El diseño propuesto de cápsulas apilables con calentadores resistivos asegura condiciones de sorción rápidas y eficientes. La simulación valida la respuesta térmica del sistema, destacando la importancia de la gestión térmica interna debido a la alta entalpía del MgH2.
*   **Detalles Técnicos:** Tanque modular de MgH2 con calentadores resistivos integrados.
*   **Datos Geométricos:**
    *   **Diseño:** Cápsulas apilables para minimizar distancia de conducción térmica.
*   **Datos Numéricos Clave:**
    *   **Material:** MgH2 activado por molienda de bolas de alta energía.
    *   **Estrategia:** Calentamiento interno resistivo.

## 5. Comparison, advancement, and performance evaluation of heat exchanger assembly...
**Referencia:** Sreeraj et al., *Renewable Energy*, 198, 667–678 (2022).

**Resumen:** Evaluación comparativa y optimización 3D de tres configuraciones de intercambiadores de calor (carcasa y tubo, tubo espiral, tubular) para un sistema de 5 kg de LaNi5.

**Conclusión:** El diseño tubular con diámetros pequeños ofrece la reacción más rápida (120 s para 90% sat.), pero penaliza la densidad gravimétrica. La incorporación de 4 tubos de calor (heat pipes) al diseño espiral mejoró la tasa de carga en un 21.5% y la tasa de energía específica en un 23.7% (527 W/kg).
*   **Detalles Técnicos:** Optimización de reactor tubular con "heat pipes".
*   **Datos Geométricos:**
    *   **Reactor:** Tubular cilíndrico.
    *   **Intercambiador:** 4 tubos de calor (heat pipes) insertados longitudinalmente.
*   **Datos Numéricos Clave:**
    *   **Carga:** 5 kg LaNi5.
    *   **Condiciones:** 303 K, 15 bar.
    *   **Mejora:** Diseño con 4 heat pipes logra 90% de saturación en 366 s.
    *   **Tasa de Energía:** 527 W/kg (23.7% superior al reactor sin heat pipes).

## 6. High Density Hydrogen Storage System Demonstration using NaAlH4
**Referencia:** Mosher et al., *Final Report DOE* (2007).

**Resumen:** Informe final sobre la demostración de un sistema de almacenamiento de hidrógeno de alta densidad utilizando hidruros complejos basados en NaAlH4.

**Conclusión:** Se identificó que los intercambiadores de tubo aleteado son superiores a las espumas metálicas para el transporte de calor a larga distancia. Se establecieron como realistas eficiencias gravimétricas del 50% y volumétricas del 70% para esta clase de sistemas. La densificación del polvo es crítica.
*   **Detalles Técnicos:** Sistema de hidruros complejos.
*   **Datos Geométricos:**
    *   **Optimización:** Comparación entre aletas transversales y espuma metálica.
*   **Datos Numéricos Clave:**
    *   **Eficiencia Gravimétrica:** 50% (meta del sistema).
    *   **Eficiencia Volumétrica:** 70%.
    *   **Hallazgo:** Aletas > Espumas metálicas para transporte de calor a larga distancia.

## 7. Optimization of hydrogen storage in metal-hydride tanks
**Referencia:** *International Journal of Hydrogen Energy* (2008).

**Resumen:** Desarrollo y validación de un modelo matemático 2D para tanques de MH. Se evaluó el impacto de la masa térmica de la pared y se optimizaron diversos diseños cilíndricos.

**Conclusión:** La masa térmica de la pared del tanque tiene un efecto despreciable. La optimización geométrica, específicamente el uso de un tubo concéntrico con aletas y fluido refrigerante, puede mejorar el tiempo de almacenamiento en casi un 80% comparado con un tanque no optimizado.
*   **Detalles Técnicos:** Modelo 2D de optimización geométrica.
*   **Datos Geométricos:**
    *   **Configuración:** Tubo concéntrico con aletas externas e internas.
    *   **Variable:** Espesor y espaciamiento de aletas.
*   **Datos Numéricos Clave:**
    *   **Mejora:** 80% de reducción en tiempo de almacenamiento con tubo concéntrico aleteado.
    *   **Material Pared:** Acero vs Latón muestra diferencia despreciable en tiempo de carga.

## 8. Hydrogen storage with metal foams
**Referencia:** *International Journal of Hydrogen Energy* (2009).

**Resumen:** Estudio numérico y experimental de un tanque de MH equipado con espuma metálica para mejorar la transferencia de calor y masa.

**Conclusión:** El uso de espuma de aluminio mejora la transferencia de calor, reduciendo el tiempo de almacenamiento (al 90%) en un 60%. La combinación de espuma metálica con un tubo intercambiador concéntrico es la configuración más efectiva, logrando una mejora del 75% (tiempo de carga ~2 min).
*   **Detalles Técnicos:** Uso de espumas metálicas para mejora térmica.
*   **Datos Geométricos:**
    *   **Material:** Espuma de aluminio.
    *   **Configuración:** Espuma integrada con tubo concéntrico.
*   **Datos Numéricos Clave:**
    *   **Mejora:** 60% reducción de tiempo (solo espuma), 75% reducción (espuma + tubo concéntrico).
    *   **Tiempo de Carga:** ~2 min para 90% de capacidad.

## 9. Experimental study of a metal hydride vessel based on a finned spiral heat exchanger
**Referencia:** *International Journal of Hydrogen Energy* (2010).

**Resumen:** Estudio experimental de un recipiente de hidruro metálico basado en un intercambiador de calor espiral aleteado.

**Conclusión:** La integración del intercambiador espiral aleteado reduce considerablemente los tiempos de absorción y desorción. Se demostró que la selección adecuada del flujo másico y la temperatura del fluido refrigerante es crucial para controlar la cinética del proceso.
*   **Detalles Técnicos:** Intercambiador espiral aleteado.
*   **Datos Geométricos:**
    *   **Tipo:** Espiral con aletas.
*   **Datos Numéricos Clave:**
    *   **Resultado:** Reducción considerable de tiempos de ciclo (cualitativo en resumen, ver texto completo para valores exactos).

## 10. Experimental and numerical study of MgH2 tank
**Referencia:** *International Journal of Hydrogen Energy* (2010).

**Resumen:** Diseño y prueba de un tanque experimental de MgH2 a pequeña escala (123 g) y desarrollo de un modelo numérico en Fluent.

**Conclusión:** La baja conductividad térmica del MgH2 limita severamente las tasas de sorción. Una segunda configuración utilizando un compósito de MgH2 y grafito natural expandido (ENG) mejoró drásticamente el rendimiento, permitiendo absorber 100 nl de H2 en solo 25 minutos.
*   **Detalles Técnicos:** MgH2 con Grafito Natural Expandido (ENG).
*   **Datos Geométricos:**
    *   **Escala:** Pequeña escala (123 g).
*   **Datos Numéricos Clave:**
    *   **Capacidad:** 80 nl (prototipo 1), 100 nl (prototipo 2).
    *   **Tiempo de Carga:** 25 min (con ENG) vs horas (sin ENG).

## 11. Experimental Study on Reaction Heat Recovery (THEUS)
**Referencia:** *International Journal of Hydrogen Energy* (2011).

**Resumen:** Resultados experimentales del sistema THEUS (Totalized Hydrogen Energy Utilization System) para nivelación de carga en edificios comerciales. Utiliza electrólisis nocturna y celdas de combustible diurnas, aprovechando el frío de la reacción de desorción para aire acondicionado.

**Conclusión:** El sistema THEUS es viable para operaciones de nivelación de carga. Se recuperó aproximadamente el 43.2% del calor de reacción total como fuente de frío. El sistema satisface los requisitos de flujo, presión y temperatura.
*   **Detalles Técnicos:** Sistema THEUS (Totalized Hydrogen Energy Utilization System).
*   **Datos Geométricos:**
    *   **Tipo:** Intercambiador de carcasa y tubos.
*   **Datos Numéricos Clave:**
    *   **Carga:** 50 kg de MH.
    *   **Recuperación de Frío:** ~43.2% del calor de reacción total.
    *   **Capacidad:** 5,400 NL de H2.

## 12. Experimental and comparative study of metal hydride hydrogen tanks
**Referencia:** *International Journal of Hydrogen Energy* (2011).

**Resumen:** Estudio comparativo de dos tanques de MH construidos con diseño modular simple para predecir el comportamiento de unidades más grandes. Se investigan los parámetros que influyen en el rendimiento.

**Conclusión:** El almacenamiento depende principalmente de la transferencia de calor; el tanque con mejor sistema de refrigeración es más rápido. El diseño de la entrada de hidrógeno y la elección de presión/temperatura operativa son factores clave de mejora.
*   **Detalles Técnicos:** Estudio de escalabilidad modular.
*   **Datos Geométricos:**
    *   **Diseño:** Modular simple.
*   **Datos Numéricos Clave:**
    *   **Hallazgo:** La cinética está dominada por la transferencia de calor.

## 13. Optimization of Heat Exchangers and System Simulation
**Referencia:** Kumar et al., *DOE Hydrogen Program* (2011).

**Resumen:** Parte del HSECoE, el equipo de GM desarrolla modelos de transporte detallados para sistemas de almacenamiento a bordo. Enfoque en la optimización del diseño de intercambiadores de calor para minimizar masa y mejorar la conductividad térmica mediante pellets y potenciadores.

**Conclusión:** Se presentaron modelos de simulación de sistemas y optimización de intercambiadores (helicoidales, lechos de MH). Se destaca la importancia de modelos detallados para justificar suposiciones y modelos de alto nivel para optimización de compensaciones (trade-offs).
*   **Detalles Técnicos:** Modelado de sistemas a bordo (Automotriz).
*   **Datos Geométricos:**
    *   **Tipos:** Helicoidal, lechos optimizados.
*   **Datos Numéricos Clave:**
    *   **Enfoque:** Minimización de masa del intercambiador.

## 14. Effects of heat exchanger design on the performance...
**Referencia:** *International Journal of Hydrogen Energy* (2015).

**Resumen:** Diseño de dispositivo cilíndrico con tubo intercambiador anular y aletas radiales de cobre. Modelo matemático 3D validado con prototipo de 1 kg de LaNi5.

**Conclusión:** Tiempo de carga de 18 min a 15 bar y 298 K. El aumento en número y espesor de aletas mejora la tasa de absorción. La transferencia de calor es eficiente debido a la corta distancia de conducción entre aletas.
*   **Detalles Técnicos:** Aletas radiales de cobre.
*   **Datos Geométricos:**
    *   **Configuración:** Tubo anular con aletas circulares.
*   **Datos Numéricos Clave:**
    *   **Carga:** 1 kg LaNi5.
    *   **Tiempo:** 18 min (15 bar, 298 K, 1 m/s flujo).
    *   **Material Aletas:** Cobre.

## 15. Performance analysis of MHR various heat exchange options
**Referencia:** Lototskyy et al., *International Journal of Hydrogen Energy* (2015).

**Resumen:** Modelo numérico 3D comparando configuraciones de reactores cilíndricos (MmNi4.6Al0.4): refrigeración interna (tubos rectos vs helicoidales) y externa (con/sin aletas transversales).

**Conclusión:** La dinámica de absorción mejora en el orden: tubo recto interno < refrigeración externa sin aletas < helicoidal interno ≈ externa con aletas. La refrigeración externa es más eficiente por mayor área de intercambio y simplicidad, sin reducir la capacidad de almacenamiento.
*   **Detalles Técnicos:** Comparativa de 4 configuraciones de intercambio.
*   **Datos Geométricos:**
    *   **Ganador:** Refrigeración externa con aletas transversales (o helicoidal interna).
*   **Datos Numéricos Clave:**
    *   **Coeficiente h:** Aumentar h por encima de 800 W/m2K no mejora significativamente la cinética (limitación por conductividad del lecho).

## 16. Efficient H2 storage up-scale equipped with aluminium foam...
**Referencia:** *International Journal of Hydrogen Energy* (2016).

**Resumen:** Estudio computacional 3D y optimización de reactores a gran escala para compresión de hidrógeno (LaNi5 y AB2). Comparación de tubos embebidos, aletas transversales y longitudinales.

**Conclusión:** Para LaNi5, 60 tubos embebidos logran 90% de carga en <2000 s. Para aletas transversales, la geometría óptima es 30 aletas (radio 8mm, espesor 2mm). Para longitudinales, 12 aletas (altura 5mm). Las aletas longitudinales resultaron ser la opción más eficiente para mejorar la cinética.
*   **Detalles Técnicos:** Optimización para compresión de H2.
*   **Datos Geométricos:**
    *   **Aletas Transversales:** 30 aletas, dist 9.8mm.
    *   **Aletas Longitudinales:** 12 aletas, altura 5mm.
    *   **Tubos:** 60 tubos embebidos.
*   **Datos Numéricos Clave:**
    *   **Tiempo:** < 2000 s para 90% carga.

## 17. The use of air as heating agent in MH reactors
**Referencia:** *International Journal of Hydrogen Energy* (2016).

**Resumen:** Demostración de repostaje de PEMFC refrigerada por aire usando hidrógeno desorbido de MH de baja temperatura calentado por el aire de escape de la FC.

**Conclusión:** El aire de escape de la PEMFC es suficiente para mantener un flujo constante de hidrógeno para una potencia de 1.1 kW durante más de 1 hora, sin necesidad de fuentes de calor externas adicionales.
*   **Detalles Técnicos:** Integración térmica Aire-Aire.
*   **Datos Geométricos:**
    *   **Fuente de Calor:** Aire de escape de la pila (exhaust air).
*   **Datos Numéricos Clave:**
    *   **Potencia Sostenida:** 1.1 kW (eléctrico).
    *   **Duración:** > 1 hora.

## 18. Impact of using a heat transfer fluid pipe in a metal hydride-phase change material tank
**Referencia:** Mellouli et al., *Applied Thermal Engineering*, 113, 554–565 (2017).

**Resumen:** Evaluación numérica de un tanque MH integrado con Material de Cambio de Fase (PCM) y un tubo de fluido de transferencia de calor (HTF).

**Conclusión:** El PCM por sí solo es insuficiente. Un tubo HTF que extraiga el 70% del calor reduce el tiempo de llenado en un 94%. Si el HTF extrae todo el calor hacia el PCM, la reducción es del 72%. La selección del fluido (ej. sales fundidas) es crítica.
*   **Detalles Técnicos:** Hibridación MH + PCM + HTF.
*   **Datos Geométricos:**
    *   **Configuración:** Tubo HTF central rodeado de MH y PCM.
*   **Datos Numéricos Clave:**
    *   **Mejora:** 94% reducción de tiempo con HTF activo.
    *   **PCM:** Ayuda, pero requiere gestión activa del calor.

## 19. Operation of a bench-scale TiFe-based alloy tank...
**Referencia:** Endo et al., *International Journal of Hydrogen Energy* (2017).

**Resumen:** Activación y operación de un tanque a escala de banco con 55 kg de aleación base TiFe. Comparación con tanque de 70 kg de LaNi5.

**Conclusión:** El tanque de TiFe requirió 7 ciclos para activación completa. Mostró un intercambio de calor superior al tanque de LaNi5, haciéndolo más adecuado para operaciones de alto flujo de hidrógeno. Absorbió >8 Nm3 a 20 NL/min.
*   **Detalles Técnicos:** Escala de banco (55 kg TiFe).
*   **Datos Geométricos:**
    *   **Tanque:** Convencional con circulación de salmuera.
*   **Datos Numéricos Clave:**
    *   **Activación:** 7 ciclos.
    *   **Capacidad:** > 8 Nm3.
    *   **Flujo:** 20 NL/min.
    *   **Comparación:** Mejor intercambio térmico que LaNi5.

## 20. Research on laboratory scale totalized hydrogen energy utilization system
**Referencia:** *International Journal of Hydrogen Energy* (2017).

**Resumen:** Pruebas de laboratorio del sistema THEUS (celda reversible URFC + tanque MH). Operación continua de 3 días para evaluar eficiencia energética.

**Conclusión:** Eficiencia total del sistema THEUS fue del 68% en modo separado y 63% en operación continua. La tasa de recuperación de calor de reacción del MH fue del 67-79%. Operación exitosa bajo 1.1 MPa.
*   **Detalles Técnicos:** Eficiencia del sistema THEUS.
*   **Datos Geométricos:**
    *   **Sistema:** URFC + MH Tank.
*   **Datos Numéricos Clave:**
    *   **Eficiencia Total:** 63-68%.
    *   **Recuperación Calor MH:** 67-79%.
    *   **Presión:** < 1.1 MPa.

## 21. Design of Large-scale MH System (210 kg)
**Referencia:** *International Journal of Hydrogen Energy* (2018).

**Resumen:** Diseño optimizado para un sistema estacionario de 210 kg de aleación Ti-Mn. Análisis de sensibilidad a parámetros de diseño y operación.

**Conclusión:** El rendimiento es muy sensible a la conductividad térmica y la presión. Se recomienda un reactor multitubular de 14 tubos. Absorción completa en 900 s y desorción en 2000 s (capacidad 0.7%). Después del 50% de reacción, la transferencia de calor deja de ser el factor limitante principal.
*   **Detalles Técnicos:** Sistema de gran escala (210 kg).
*   **Datos Geométricos:**
    *   **Diseño:** Multitubular (14 tubos).
*   **Datos Numéricos Clave:**
    *   **Tiempos:** 900 s (abs), 2000 s (des).
    *   **Capacidad:** 0.7% (sistema).

## 22. Numerical Investigation of Stackable MH Reactor
**Referencia:** *International Journal of Hydrogen Energy* (2018).

**Resumen:** Modelo 3D de un nuevo diseño de unidad de almacenamiento apilable, similar a un stack de celdas de combustible, donde el MEA se reemplaza por un reactor MH entre placas de flujo.

**Conclusión:** El diseño apilable supera los problemas de los intercambiadores tubulares internos (fugas, estrés). Permite una gran área de transferencia de calor y modularidad.
*   **Detalles Técnicos:** Diseño tipo "Stack" (apilable).
*   **Datos Geométricos:**
    *   **Concepto:** Placas bipolares de flujo refrigerante intercaladas con MH.
*   **Datos Numéricos Clave:**
    *   **Ventaja:** Modularidad y superficie de intercambio.

## 23. Ideal distance among metal hydride tanks in forced convection
**Referencia:** *International Journal of Hydrogen Energy* (2018).

**Resumen:** Investigación teórica y numérica sobre la distancia ideal entre tanques de MH en convección forzada para optimizar el flujo de hidrógeno.

**Conclusión:** La distancia ideal entre tanques disminuye al aumentar el número de Reynolds (velocidad del aire). El ajuste correcto de esta distancia maximiza la transferencia de calor y el flujo de hidrógeno.
*   **Detalles Técnicos:** Arreglo de bancos de tanques.
*   **Datos Geométricos:**
    *   **Variable:** Distancia entre cilindros.
*   **Datos Numéricos Clave:**
    *   **Reynolds:** A mayor Re, menor distancia requerida.

## 24. Design and thermal modelling of industrial scale reactor
**Referencia:** *International Journal of Hydrogen Energy* (2019).

**Resumen:** Propuesta de correlaciones aritméticas para diseñar reactores cilíndricos industriales con tubos de refrigeración embebidos (ECT). Validación con modelo 3D para 50 kg de LaNi4.7Al0.3.

**Conclusión:** Un reactor de 6 pulgadas con 99 tubos ECT mostró la mejor transferencia de calor. La presión de suministro tiene el efecto predominante en la cinética, seguida del flujo del fluido térmico (HTF).
*   **Detalles Técnicos:** Escalamiento industrial (50 kg).
*   **Datos Geométricos:**
    *   **Reactor:** 6 pulgadas de diámetro.
    *   **Intercambiador:** 99 tubos embebidos (ECT).
*   **Datos Numéricos Clave:**
    *   **Presión:** 30 bar.
    *   **Flujo HTF:** 60 lpm.

## 25. Hydrogen Storage: Industrial Perspectives (France)
**Referencia:** Barthelemy (2019/2021).

**Resumen:** Revisión de tecnologías de almacenamiento de hidrógeno comprimido (tanques metálicos y compuestos) y perspectivas industriales en Francia. Actualización de normas y regulaciones.

**Conclusión:** El almacenamiento comprimido es la tecnología más madura. Los desafíos actuales son mejorar la durabilidad y seguridad de los recipientes de presión compuestos (COPV) para 700 bar. Se requiere más investigación en técnicas no destructivas (NDT) para inspección.
*   **Detalles Técnicos:** Revisión industrial.
*   **Datos Geométricos:**
    *   **Enfoque:** Tanques de alta presión (Tipo III y IV).
*   **Datos Numéricos Clave:**
    *   **Presión:** Hasta 1100 bar (estudio de fatiga).

## 26. Modular Zero Emission Building (ZEB) System
**Referencia:** Endo et al., *International Journal of Hydrogen Energy* (2019).

**Resumen:** Sistema de energía de hidrógeno estacionario a escala de banco para un edificio de emisiones cero (ZEB). Integra electrolizador PEM, FC y 520 kg de aleación TiFe (segura y de bajo costo).

**Conclusión:** Se logró la operación ZEB durante 24 horas. La aleación TiFe demostró ser efectiva y segura bajo regulaciones japonesas. La integración térmica permitió la desorción completa usando calor parcial de la FC.
*   **Detalles Técnicos:** Sistema ZEB (Zero Emission Building).
*   **Datos Geométricos:**
    *   **Almacenamiento:** 520 kg de TiFe.
    *   **Contenedor:** 12 pies.
*   **Datos Numéricos Clave:**
    *   **Capacidad:** 80 Nm3.
    *   **Potencia:** 3.5 kW FC, 5 Nm3/h Electrolizador.

## 27. Materials for hydrogen-based energy storage
**Referencia:** Hirscher et al., *Journal of Alloys and Compounds* (2020).

**Resumen:** Revisión exhaustiva de materiales para almacenamiento de energía basada en hidrógeno: hidruros metálicos, complejos, químicos y adsorbentes.

**Conclusión:** Aunque existen métodos prometedores, todos requieren optimización. El proyecto HyCARE (tanque de 50 kg con PCM) es un ejemplo de demostración a gran escala en curso. La combinación de almacenamiento de H2 y calor es clave para la eficiencia.
*   **Detalles Técnicos:** Revisión de materiales.
*   **Datos Geométricos:**
    *   **Ejemplo:** Proyecto HyCARE (50 kg).
*   **Datos Numéricos Clave:**
    *   **Meta:** Optimización simultánea de >20 propiedades.

## 28. Metal Hydride hydrogen storage and compression systems
**Referencia:** Tarasov et al., *International Journal of Hydrogen Energy* (2020).

**Resumen:** Desarrollo de sistemas de almacenamiento y compresión de hidrógeno basados en hidruros metálicos AB5 y AB2.

**Conclusión:** Se demostraron sistemas de almacenamiento de energía de escala media que integran compresión térmica de hidrógeno (hasta 150-200 atm) para alimentar cilindros de gas y stacks de celdas de combustible.
*   **Detalles Técnicos:** Compresión térmica.
*   **Datos Geométricos:**
    *   **Materiales:** AB5 y AB2.
*   **Datos Numéricos Clave:**
    *   **Presión Salida:** 150-200 atm.
    *   **Potencia:** Hasta 30 kW (FC).

## 29. Studies on 10 kg MHR with embedded cooling tubes
**Referencia:** *International Journal of Hydrogen Energy* (2020).

**Resumen:** Diseño, fabricación y estudio experimental de un reactor de 10 kg de LaNi5 con tubos de refrigeración embebidos y camisa de agua externa.

**Conclusión:** Capacidad reversible máxima de 1.13 wt%. La presión de suministro es el factor más significativo en la absorción (25 bar óptimo). La temperatura ambiente es preferible para la absorción. Desorción completa y rápida a 80°C.
*   **Detalles Técnicos:** Reactor de 10 kg LaNi5.
*   **Datos Geométricos:**
    *   **Refrigeración:** Tubos embebidos + Camisa externa.
*   **Datos Numéricos Clave:**
    *   **Capacidad:** 1.13 wt%.
    *   **Tiempo Abs:** 1620 s (25 bar).
    *   **Tiempo Des:** 2700 s (80°C).

## 30. Numerical investigation of MH reactor with embedded embossed plate heat exchanger
**Referencia:** Lewis & Chippar, *Energy*, 194 (2020).

**Resumen:** Investigación numérica de un reactor MH integrado con un intercambiador de calor de placas estampadas (EPHX). Comparación de flujos: paralelo, pin, serpentina.

**Conclusión:** El diseño de serpentina vertical ofreció la mejor transferencia de calor y uniformidad de temperatura. Aunque el EPHX tuvo una eliminación de calor total ligeramente menor que un serpentín helicoidal, logró tasas de absorción similares con una distribución de temperatura mucho más uniforme.
*   **Detalles Técnicos:** Placas estampadas (EPHX).
*   **Datos Geométricos:**
    *   **Diseño:** Serpentina vertical.
*   **Datos Numéricos Clave:**
    *   **Ventaja:** Uniformidad térmica superior.

## 31. Design of MH reactor with hexagonal honeycomb
**Referencia:** *International Journal of Hydrogen Energy* (2021).

**Resumen:** Diseño y análisis de un sistema de 10 kWh con mejoras de transferencia de calor basadas en panal hexagonal de aluminio.

**Conclusión:** La red de panal mejora el rendimiento de absorción en más del 30%. La condición óptima fue 35 bar y temperatura ambiente (90% en 7200 s). Aumentar el coeficiente de transferencia de calor más allá de cierto punto no mejora la tasa significativamente.
*   **Detalles Técnicos:** Panal hexagonal de aluminio.
*   **Datos Geométricos:**
    *   **Estructura:** Honeycomb.
*   **Datos Numéricos Clave:**
    *   **Mejora:** >30% en absorción.
    *   **Tiempo:** 7200 s (90%).

## 32. Design and performance analysis of an annular metal hydride reactor
**Referencia:** Prasad & Muthukumar, *Renewable Energy*, 181 (2022).

**Resumen:** Diseño modular de un reactor anular de MH refrigerado/calentado en superficies interna y externa. Comparación de tres configuraciones para una relación de peso de 2.

**Conclusión:** La adición de aletas radiales mejoró las tasas de absorción y desorción en un factor de ~2. El tiempo de absorción fue de 283 s (15 bar, 25°C) y desorción 525 s (1 bar, 50°C).
*   **Detalles Técnicos:** Reactor anular.
*   **Datos Geométricos:**
    *   **Refrigeración:** Doble superficie (interna/externa).
*   **Datos Numéricos Clave:**
    *   **Factor de Mejora:** ~2 (con aletas).
    *   **Tiempos:** 283 s (abs), 525 s (des).

## 33. Parametric studies on MmNi4.7Fe0.3 based reactor
**Referencia:** Kumar et al., *Journal of Energy Storage*, 35 (2021).

**Resumen:** Investigación paramétrica en un reactor de 4 kg de MmNi4.7Fe0.3 con 55 tubos de refrigeración embebidos (ECT).

**Conclusión:** La aleación tiene características pobres a baja presión (<50 bar). A 70 bar, la capacidad mejora 11.7 veces respecto a 10 bar. La temperatura de absorción tiene un impacto significativo.
*   **Detalles Técnicos:** Estudio de alta presión.
*   **Datos Geométricos:**
    *   **Reactor:** 55 tubos ECT.
*   **Datos Numéricos Clave:**
    *   **Presión:** Requiere >50 bar para eficiencia.
    *   **Mejora:** 11.7x capacidad a 70 bar vs 10 bar.

## 34. Scaling up Metal Hydrides for Real-Scale Applications
**Referencia:** Jensen et al., *Inorganics* (2021).

**Resumen:** Revisión sobre los efectos del escalado en el rendimiento de hidruros metálicos.

**Conclusión:** El escalado afecta significativamente la capacidad y cinética. La molienda de bolas industrial tiene bajo rendimiento; se necesitan aditivos. El enfriamiento no uniforme en muestras grandes de fusión por inducción afecta las transiciones de fase.
*   **Detalles Técnicos:** Problemas de escalado.
*   **Datos Geométricos:**
    *   **Proceso:** Molienda de bolas vs Fusión por inducción.
*   **Datos Numéricos Clave:**
    *   **Hallazgo:** Propiedades varían con el tamaño del lote.

## 35. Experimental 5kg reactor with conical fins
**Referencia:** *International Journal of Hydrogen Energy* (2022).

**Resumen:** Estudio experimental de un reactor de 5 kg de LaNi5 con aletas cónicas de cobre y tubos de transferencia de calor.

**Conclusión:** Aletas cónicas mejoran la transferencia. Absorción del 90% en ~9.1 min (25 bar). Desorción del 90% en ~20 min (60°C). Se validó un modelo numérico para configuraciones en serie/paralelo de hasta 50 kg.
*   **Detalles Técnicos:** Aletas cónicas de cobre.
*   **Datos Geométricos:**
    *   **Aletas:** Forma cónica.
*   **Datos Numéricos Clave:**
    *   **Tiempos:** 9.1 min (abs), 20 min (des).
    *   **Escalado:** Validado hasta 50 kg.

## 36. Thermal management techniques in MHR (Review)
**Referencia:** *Energies* (2023).

**Resumen:** Revisión exhaustiva de técnicas de gestión térmica: optimización de forma, intercambiadores, PCM, aditivos.

**Conclusión:** El uso de múltiples tubos de refrigeración internos es generalmente superior. El uso de PCM solo no es suficiente para tiempos de reacción rápidos. Las camisas de agua externas son simples pero limitadas por la conductividad radial.
*   **Detalles Técnicos:** Revisión de gestión térmica.
*   **Datos Geométricos:**
    *   **Comparación:** Tubos internos vs Camisa externa vs PCM.
*   **Datos Numéricos Clave:**
    *   **Recomendación:** Tubos internos múltiples.

## 37. Thermal management of MH tank coupled with PEMFC
**Referencia:** Tong et al., *Case Studies in Thermal Engineering* (2023).

**Resumen:** Gestión térmica de tanque MH acoplado con PEMFC. El calor residual de la PEMFC se usa para la desorción.

**Conclusión:** Modelo de parámetros concentrados validado. Un tanque MH puede alimentar una FC de 1 kW durante 2 horas usando el calor residual, con una apertura de válvula de 0.5 y flujo de 15.17 L/min.
*   **Detalles Técnicos:** Acoplamiento PEMFC-MH.
*   **Datos Geométricos:**
    *   **Sistema:** Integrado.
*   **Datos Numéricos Clave:**
    *   **Autonomía:** 2 horas a 1 kW.
    *   **Flujo:** 15.17 L/min.

## 38. State of art heat exchanger geometry
**Referencia:** Kudiiarov et al. (2023).

**Resumen:** Estado del arte en geometría de intercambiadores de calor. Comparación de reactores cilíndricos, esféricos y tubulares.

**Conclusión:** Los reactores tubulares ofrecen mejor densidad gravimétrica que los de cámara. Los filtros porosos aseguran distribución uniforme de hidrógeno. Las espumas metálicas mejoran el calor pero pueden reducir la capacidad volumétrica.
*   **Detalles Técnicos:** Geometría de reactores.
*   **Datos Geométricos:**
    *   **Tipos:** Cilíndrico vs Esférico vs Tubular.
*   **Datos Numéricos Clave:**
    *   **Preferencia:** Tubular por densidad gravimétrica.

## 39. Performance analysis of novel co-generation system (SMR + H2)
**Referencia:** Wu et al., *Energy*, 302 (2024).

**Resumen:** Análisis de un sistema de co-generación que integra un reactor modular pequeño (SMR), gasificación de plasma y producción de hidrógeno (PSA + ciclo Cu-Cl).

**Conclusión:** El sistema híbrido alcanza una eficiencia de conversión de residuos médicos a energía del 63.75%. Facilita la nivelación de carga (peak shaving) desviando vapor para producción de hidrógeno en horas valle.
*   **Detalles Técnicos:** Co-generación Nuclear-Hidrógeno.
*   **Datos Geométricos:**
    *   **Sistema:** SMR + PSA + Cu-Cl.
*   **Datos Numéricos Clave:**
    *   **Eficiencia:** 63.75%.

## 40. The relationship between thermal management methods and performance
**Referencia:** Zhu et al., *Journal of Materials Science & Technology*, 203 (2024).

**Resumen:** Relación entre métodos de gestión térmica y rendimiento. Comparación de convección natural, refrigeración por agua, aletas y espuma metálica.

**Conclusión:** Cambiar de convección natural a agua mejora la absorción en 72.8%. Añadir aletas de cobre reduce el tiempo un 55.6% adicional. La transferencia de calor es más crítica que la de masa.
*   **Detalles Técnicos:** Cuantificación de mejoras térmicas.
*   **Datos Geométricos:**
    *   **Mejoras:** Agua > Aletas > Espuma.
*   **Datos Numéricos Clave:**
    *   **Reducción Tiempo:** 72.8% (Agua), +55.6% (Aletas).

## 41. Design optimization of multi tube metal hydride reactor
**Referencia:** Parashar et al., *Thermal Science and Engineering Progress*, 49 (2024).

**Resumen:** Optimización de diseño y análisis numérico de un reactor multitubular con aletas de disco (DFMTR) para almacenamiento de gran capacidad.

**Conclusión:** El modelo DFMTR ahorra un 38% (absorción) y 31% (desorción) de tiempo comparado con el reactor base. Absorbe 1.37 wt% en 795 s.
*   **Detalles Técnicos:** Reactor multitubular con aletas de disco.
*   **Datos Geométricos:**
    *   **Diseño:** DFMTR.
*   **Datos Numéricos Clave:**
    *   **Ahorro Tiempo:** 38%.
    *   **Capacidad:** 1.37 wt%.

## 42. Experimental investigation on hydrogen transfer in coupled metal hydride reactors
**Referencia:** Kumar & Muthukumar, *Applied Energy*, 363 (2024).

**Resumen:** Investigación experimental sobre transferencia de hidrógeno en reactores acoplados para purificación multietapa. Uso de LaNi4.7Al0.3, LaNi5 y La0.9Ce0.1Ni5.

**Conclusión:** El sistema multietapa purifica hidrógeno de muestras con 80% de impurezas. Capacidad de almacenamiento de 1.3-1.4 wt%. La regeneración de aleaciones envenenadas es posible mediante evacuación a 90-95°C.
*   **Detalles Técnicos:** Purificación de H2.
*   **Datos Geométricos:**
    *   **Configuración:** 3 etapas en cascada.
*   **Datos Numéricos Clave:**
    *   **Pureza:** Separa desde 80% impureza.
    *   **Regeneración:** 90-95°C.

## 43. Solid Hydrogen Carriers (White Paper)
**Referencia:** Fraunhofer IFAM (2024).

**Resumen:** Documento técnico sobre portadores de hidrógeno sólido. Avances en compuestos de hidruro metálico para almacenamiento, purificación y compresión.

**Conclusión:** Los compuestos avanzados permiten ciclos de carga/descarga en minutos. Densidad volumétrica de hasta 150 kg H2/m3 a bajas presiones (1-40 bar). Ventajas significativas sobre polvo convencional en dinámica y densidad del sistema.
*   **Detalles Técnicos:** Compuestos avanzados (PowerPaste/Composites).
*   **Datos Geométricos:**
    *   **Forma:** Compuestos sólidos.
*   **Datos Numéricos Clave:**
    *   **Densidad:** 150 kg H2/m3.
    *   **Ciclos:** Minutos.

## 44. Holding the Invisible: Advanced Materials for Hydrogen Storage
**Referencia:** *Review* (2025).

**Resumen:** Evaluación comparativa de métodos de almacenamiento (físico, químico, hidruros). Análisis tecno-económico y de ciclo de vida.

**Conclusión:** El almacenamiento de gas comprimido es maduro pero requiere alta presión. El hidrógeno líquido es denso pero energéticamente costoso. Los hidruros metálicos son ideales para uso estacionario. Falta un sistema a condiciones ambiente con densidad práctica.
*   **Detalles Técnicos:** Análisis Tecno-económico.
*   **Datos Geométricos:**
    *   **Comparativa:** Gas vs Líquido vs Sólido.
*   **Datos Numéricos Clave:**
    *   **Costo:** $500-700/kg H2 (actual) vs $30-50/kg H2 (meta).

## 45. Numerical analysis of large-scale modular MHR with hybrid heat exchanger
**Referencia:** *International Journal of Hydrogen Energy* (2026).

**Resumen:** Investigación numérica de un reactor modular de 400 kg con intercambiador de calor híbrido (tubo aleteado interno + bobina helicoidal externa).

**Conclusión:** El diseño de doble circuito supera a los sistemas de refrigeración simple. Aumentar la conductividad térmica del lecho de 1.6 a 9.6 W/mK reduce el tiempo de absorción en un 24%. La presión de suministro es el factor dominante (aumentar de 5 a 9 MPa reduce el tiempo a la mitad).
*   **Detalles Técnicos:** Reactor híbrido de 400 kg.
*   **Datos Geométricos:**
    *   **Intercambiador:** Híbrido (Interno + Externo).
*   **Datos Numéricos Clave:**
    *   **Presión:** 9 MPa reduce tiempo a 3600 s.
    *   **Conductividad:** Aumentar a 9.6 W/mK mejora 24%.

## 46. An overview of TiFe alloys for hydrogen storage
**Referencia:** Liu et al., *Journal of Energy Storage*, 68 (2023).

**Resumen:** Revisión sobre aleaciones TiFe: estructura, síntesis, activación y aplicaciones.

**Conclusión:** El TiFe es un candidato principal para almacenamiento estacionario por su bajo costo y condiciones moderadas, a pesar de su difícil activación inicial. Se destacan avances en dopaje y procesamiento mecánico para mejorar la activación.
*   **Detalles Técnicos:** Aleaciones TiFe.
*   **Datos Geométricos:**
    *   **Aplicación:** Estacionaria.
*   **Datos Numéricos Clave:**
    *   **Ventaja:** Bajo costo, abundancia.

## 47. Enhancing absorption performance... Implementation of fins and a water jacket
**Referencia:** Lee et al., *International Journal of Hydrogen Energy*, 116 (2025).

**Resumen:** Estudio CFD de transferencia de calor y masa en dispositivo MH con aletas internas y camisa de agua.

**Conclusión:** Aletas de cobre escalonadas y mayor flujo/presión reducen significativamente el tiempo. Aletas escalonadas reducen tiempo en 30%. Aumentar presión a 20 bar lo reduce en un 61%.
*   **Detalles Técnicos:** Aletas escalonadas.
*   **Datos Geométricos:**
    *   **Aletas:** Cobre, disposición escalonada.
*   **Datos Numéricos Clave:**
    *   **Mejora:** 61% (con 20 bar).

## 48. Development of large MH tank system (1000 Nm3)
**Referencia:** *International Journal of Hydrogen Energy* (2017).

**Resumen:** Desarrollo de un sistema de tanque MH de gran escala (1000 Nm3) usando compuesto MH-resina ("Hydrage") para evitar la pulverización y deformación.

**Conclusión:** El sistema de 9 tanques (7.2 ton de MH) operó exitosamente sin deformación gracias al compuesto. Tasas de 11.2 Nm3/h (desorción) y 5.6 Nm3/h (absorción). Alta densidad de llenado lograda.
*   **Detalles Técnicos:** Compuesto MH-Resina (Hydrage).
*   **Datos Geométricos:**
    *   **Sistema:** 9 tanques, 1000 Nm3 total.
*   **Datos Numéricos Clave:**
    *   **Masa:** 7.2 toneladas.
    *   **Flujo:** 11.2 Nm3/h.

## 49. Experimental studies on novel multi tubular reactor with shell
**Referencia:** Gupta et al., *Journal of Energy Storage*, 67 (2023).

**Resumen:** Estudio experimental de reactor multitubular de 50 kg de LaNi5 con carcasa y deflectores (baffles).

**Conclusión:** Aumentar el flujo de HTF de 15 a 25 LPM reduce el tiempo de absorción de 1451 s a 1154 s. La recuperación de calor por el HTF fue del 69.3% a 25 LPM. Los deflectores mejoran el coeficiente de transferencia de calor.
*   **Detalles Técnicos:** Reactor con deflectores (Baffles).
*   **Datos Geométricos:**
    *   **Carga:** 50 kg LaNi5.
*   **Datos Numéricos Clave:**
    *   **Mejora:** Tiempo reducido a 1154 s con 25 LPM.

## 50. Postprint WASPE Buerger 2017 (Hydralloy C5)
**Referencia:** Buerger et al. (2017).

**Resumen:** Análisis de Hydralloy C5 para aplicaciones estacionarias.

**Conclusión:** Hydralloy C5 es adecuado para condiciones ambiente (4-30 bar, 15-40°C), ofreciendo una solución robusta para almacenamiento buffer.
*   **Detalles Técnicos:** Hydralloy C5.
*   **Datos Geométricos:**
    *   **Aplicación:** Buffer storage.
*   **Datos Numéricos Clave:**
    *   **Rango:** 4-30 bar.

## 51. Honeycomb fin metal hydride reactor integrated with PCM
**Referencia:** *SSRN Preprint* (2023).

**Resumen:** Estudio de integración de estructura de panal (honeycomb) en un reactor de MH con Material de Cambio de Fase (PCM) para mejorar la conductividad térmica del PCM.

**Conclusión:** La integración de estructura de panal mejora la conductividad efectiva del PCM, permitiendo una gestión térmica pasiva más efectiva que el uso de PCM puro, reduciendo los tiempos de ciclo.
*   **Detalles Técnicos:** PCM + Honeycomb.
*   **Datos Geométricos:**
    *   **Estructura:** Panal embebido en PCM.
*   **Datos Numéricos Clave:**
    *   **Ventaja:** Mejora conductividad del PCM.

## 52. Turkia Main (Thermal control and tank arrangement)
**Referencia:** *International Journal of Hydrogen Energy* (2022).

**Resumen:** Diseño de tanque modular con Hydralloy C5 y compuestos de grafito expandido (MHC) para sistemas de respaldo de energía (Power2Gas).

**Conclusión:** El tanque modular de 4 capas garantiza condiciones de operación simples (4-30 bar, 15-40°C). Factor de utilización del 93% del hidrógeno almacenado. Escalable y capaz de soportar cargas variables.
*   **Detalles Técnicos:** Compuestos Grafito-MH.
*   **Datos Geométricos:**
    *   **Diseño:** Modular 4 capas.
*   **Datos Numéricos Clave:**
    *   **Utilización:** 93%.
    *   **Potencia:** 160 Wel por 100 min.


---

# Guía Comparativa y Conclusiones Generales

A partir de la revisión de los 52 artículos, se pueden extraer las siguientes tendencias y recomendaciones para el diseño de reactores de almacenamiento de hidrógeno en estado sólido:

## 1. Estrategias de Gestión Térmica
La gestión térmica es el factor crítico que limita la cinética de absorción/desorción.
*   **Aletas (Fins):** La adición de aletas (longitudinales, transversales, de pin) es la estrategia más común y efectiva para mejorar la transferencia de calor en reactores tubulares [7, 14, 15, 16, 32, 35, 40, 41, 47].
*   **Tubos Helicoidales (Helical Coils):** Ofrecen una mayor área de transferencia de calor por unidad de volumen en comparación con tubos rectos [5, 9, 13, 15, 45].
*   **Materiales de Cambio de Fase (PCM):** Permiten almacenar el calor de la reacción exotérmica (absorción) para usarlo en la reacción endotérmica (desorción). Son ideales para sistemas autónomos, pero requieren mejoras en su propia conductividad térmica (ej. adición de grafito o espumas metálicas) [18, 27, 36, 51].

## 2. Geometría del Reactor
*   **Multitubular (Shell & Tube):** El diseño estándar industrial. Fácil de escalar, pero requiere optimización de deflectores (baffles) para mejorar el flujo del fluido de transferencia de calor (HTF) [21, 24, 33, 36, 41, 49].
*   **Modular:** La tendencia para aplicaciones a gran escala es el diseño modular, donde múltiples unidades pequeñas se conectan, facilitando el mantenimiento y la escalabilidad sin rediseñar todo el sistema [1, 4, 12, 22, 26, 39, 45, 52].

## 3. Materiales de Almacenamiento
*   **LaNi5 y derivados:** Siguen siendo el estándar para temperaturas moderadas debido a su buena cinética y presión de equilibrio adecuada [2, 5, 14, 16, 19, 24, 29, 35, 42, 49].
*   **TiFe:** Ganando popularidad para aplicaciones estacionarias por su bajo costo, aunque requiere procesos de activación inicial [2, 19, 26, 46].
*   **Compuestos (Composites):** El uso de matrices de grafito expandido (ENG) o resinas evita la decrepitación (pulverización) del hidruro y mejora la conductividad térmica y la estabilidad mecánica del lecho [10, 43, 48, 52].

# Análisis Comparativo y Categorización

## Autores y Estudios sobre TiFe (Hierro-Titanio)
El TiFe se destaca en aplicaciones estacionarias por su bajo costo y abundancia, a pesar de requerir procesos de activación inicial exigentes.

| Autor / Estudio | Año | Enfoque Principal | Datos Clave |
| :--- | :---: | :--- | :--- |
| **Endo et al.** | 2017 | Activación y operación a gran escala (55 kg) | 284h activación, mejor intercambio térmico que LaNi5. |
| **Endo et al.** | 2019 | Sistema ZEB (Edificio Cero Emisiones) | 520 kg TiFe, operación 24h, seguridad urbana. |
| **Matsumasa et al.** | 2019 | Propiedades termofísicas (n-FeTi) | Compactación del lecho (reducción de porosidad) vs expansión. |
| **Liu et al.** | 2023 | Revisión General | Métodos de dopaje y síntesis para mejorar activación. |

## Estrategias de Gestión Térmica
Clasificación de los estudios según la arquitectura de intercambio de calor empleada.

### Gestión Térmica Interna (Tubos, Aletas Internas, Matrices)
*Estrategia dominante para reactores de gran diámetro donde la conducción es el limitante.*
*   **Sreeraj et al. (2022):** Heat pipes internos.
*   **Miao et al. (2025):** Estructura de panal (Honeycomb).
*   **Lewis & Chippar (2020):** Placas estampadas (Embossed Plate).
*   **Prasad & Muthukumar (2022):** Reactor anular con aletas radiales.
*   **Parashar et al. (2024):** Multi-tubo con aletas de disco (DFMTR).
*   **Mellouli et al. (2017):** Tubo HTF interno + PCM.
*   **Industrial Scale (2019):** 99 tubos de enfriamiento embebidos (ECT).
*   **Efficient H2 Storage (2016):** Tubos con aletas longitudinales.

### Gestión Térmica Externa (Chaquetas, Aletas Externas, Aire)
*Efectiva para reactores de pequeño diámetro (<50mm) o modulares tubulares.*
*   **Optimization (2008):** Aletas externas y chaquetas.
*   **Turkia (2022):** Convección forzada por aire (banco de tanques).
*   **Air as heating agent (2016):** Uso directo de aire de escape.
*   **Metal Foams (2009):** Espuma + Enfriamiento externo (aunque a veces combinado).

### Gestión Térmica Mixta / Híbrida
*Tendencia para reactores de gran escala (>100 kg) para maximizar homogeneidad.*
*   **Large Scale Modular (2026):** Circuito híbrido (Tubo aleteado interno + Bobina helicoidal externa).
*   **Lee et al. (2025):** Aletas internas escalonadas + Chaqueta de agua externa.
*   **10 kg MHR (2020):** Tubos embebidos (ECT) + Chaqueta de agua.
*   **Prasad & Muthukumar (2022):** Reactor anular enfriado por ambas superficies.

## Aplicaciones Estacionarias
Estudios enfocados explícitamente en almacenamiento fijo (edificios, backup, grid).
*   **Endo et al. (2019):** Edificio Cero Emisiones (ZEB) - 520 kg TiFe.
*   **Buerger et al. (2017):** Sistemas de respaldo (Backup Power) - Hydralloy C5.
*   **THEUS (2011/2017):** Nivelación de carga y cogeneración para edificios comerciales.
*   **Large MH Tank (2017):** Almacenamiento masivo de renovables (1000 Nm3).
*   **Wu et al. (2024):** Integración con reactores nucleares (SMR) para "peak shaving".

## Estudios de Instrumentación y Control
Investigaciones que aportan datos sobre sensores, control y monitoreo.
*   **Precise temperature control (2023):** Uso del reactor como actuador térmico (Control PI de presión).
*   **Endo et al. (2017):** Monitoreo detallado de activación (presión/temperatura) durante 284h.
*   **Kumar & Muthukumar (2024):** Análisis TCD (Detector de Conductividad Térmica) para pureza de H2 en sistemas acoplados.

## Guía de Comparación Directa entre Autores

Para profundizar en temas específicos, se sugiere contrastar los siguientes grupos de autores:

### 1. Rendimiento de Materiales: TiFe vs LaNi5
*   **Comparar:** **Endo et al. (2017/2019)** [TiFe] vs **Sreeraj et al. (2022) / Gupta et al. (2023)** [LaNi5].
*   **Tema:** Evaluar la penalización en cinética de activación del TiFe (requiere alta presión/temperatura inicial) frente a la facilidad de uso pero alto costo del LaNi5. Endo demuestra que una vez activado, el TiFe es viable para gran escala.

### 2. Eficiencia de Intercambiadores de Calor: Interno vs Externo
*   **Comparar:** **Lototskyy et al. (2015)** [Ranking de configuraciones] vs **Zhu et al. (2024)** [Cuantificación de mejoras].
*   **Tema:** Lototskyy establece teóricamente que la configuración externa con aletas es competitiva; Zhu cuantifica esto mostrando que la gestión externa reduce el tiempo en un 72.8%, mientras que añadir mejoras internas aporta un 55.6% extra.

### 3. Escalamiento a Sistemas Masivos (>100 kg)
*   **Comparar:** **Large MH Tank (2017)** [1000 Nm3, 7.2 ton] vs **Endo et al. (2019)** [ZEB, 520 kg].
*   **Tema:** Desafíos de ingeniería en sistemas de toneladas. El estudio de 2017 utiliza un enfoque modular de 9 tanques, similar al enfoque de Endo, validando la modularidad como la ruta clave para el escalamiento.

### 4. Uso de Materiales de Cambio de Fase (PCM)
*   **Comparar:** **Mellouli et al. (2017)** [PCM + Tubo HTF] vs **SSRN Preprint (2023)** [PCM + Panal].
*   **Tema:** Mellouli demuestra que el PCM solo no es suficiente para cargas rápidas y requiere un tubo de fluido activo (reducción 94% vs 72%). El estudio de 2023 intenta mejorar la conductividad del PCM usando una estructura de panal.

