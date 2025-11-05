# Notas de Lectura: Effects of heat exchanger design on the performance of a solid state hydrogen storage device

**Autor:** Singh, L., Maiya, M.P., Srinivasa Murthy, S.

**Referencia BibTeX:** `singh2015`

**Fecha de Publicación:** 2015

---

## 1. Resumen

Este estudio presenta una investigación detallada sobre el diseño y optimización de intercambiadores de calor para dispositivos de almacenamiento de hidrógeno en hidruros metálicos, combinando modelado 3D, simulación numérica y validación experimental. Se desarrolla un sistema de aletas radiales optimizado que logra reducción del 45% en tiempos de carga y mejora del 300% en conductividad efectiva.

## 2. Imagen de Referencia

![Intercambiador de calor optimizado](img/notas_2015_effects_of_head_exchanger_desing_on_the_perfomace_of_solid_state_hydrogen_storage.png)

## 3. Puntos Clave y Datos

### Aspectos Principales

- Sistema de aletas radiales optimizado con 30 aletas de 1.5mm espesor
- Reducción tiempo de carga: 45% respecto a diseño sin aletas
- Mejora conductividad efectiva: 300% (de 1.2 a 3.6-4.8 W/m·K)
- Uniformidad térmica: ±3°C en todo el reactor
- Correlación modelo-experimento > 95% (error < 5%)
- Validación en 100 ciclos con reproducibilidad del 95%

## 4. Características Técnicas del Sistema

### 4.1 Hidruro Metálico

- **Tipo de hidruro:** LaNi₅ polvo compactado (>99.9% pureza)
- **Cantidad de hidruro:** 1.0 kg, capacidad máxima 1.4 wt% H₂
- **Conductividad Térmica MH:** 1.2 W/m·K

### 4.2 Configuración Geométrica

- **Descripción del sistema:** Reactor cilíndrico anular con 30 aletas radiales perforadas de cobre, porosidad 0.5, integración tubo-aletas optimizada
- **Configuración geométrica:** Cilíndrica anular con aletas radiales perforadas (3mm diámetro perforaciones)
- **Longitud (mm):** 250
- **Diámetro (mm):** 76 (externo), 25 (interno)
- **L/D ratio:** 3.3
- **Volumen (L):** 1.1

### 4.3 Transferencia de Calor

- **Intercambiador de Calor:** 30 aletas radiales de cobre ETP (C11000), espesor 1.5mm, espaciado 8mm
- **Coeficiente de transferencia de calor:** Conductividad efectiva del sistema: 3.6-4.8 W/m·K con aletas

### 4.4 Condiciones de Operación

- **Temperatura (°C):** 25 (298K) máxima, refrigerante: 15-25 (288-298K)
- **Presión de trabajo:** Absorción: 8-12 bar, Desorción: 1-2 bar
- **Flujo (NL/min):** Refrigerante: 0.2-1.0 m/s

### 4.5 Rendimiento del Sistema

- **Tiempo carga:** 10-15 min (t₉₀ absorción), 15-20 min (desorción)
- **Cantidad H2:** 14g H₂ (1.4 wt%)

## 5. Transferencia de Calor

**Métodos de transferencia de calor utilizados:**

- Conducción térmica dominante en lecho poroso de LaNi₅
- Convección negligible (equilibrio térmico local)
- Conducción en aletas radiales de cobre
- Sistema anular con flujo de refrigerante

**Materiales y propiedades térmicas:**

- Cuerpo: Acero inoxidable 316L
- Aletas: Cobre ETP (C11000), alta conductividad
- LaNi₅: k=1.2 W/m·K, cp=419 J/kg·K, densidad=8400 kg/m³
- Resistencia térmica contacto aleta-MH: 2.5×10⁻⁴ m²·K/W
- Resistencia térmica interfaz tubo-aleta: 1.8×10⁻⁴ m²·K/W

**Eficiencia térmica:**

- Sin aletas: k=1.2 W/m·K
- Con 30 aletas optimizadas: k=3.6-4.8 W/m·K (mejora 300%)
- Uniformidad térmica: ±3°C en todo el volumen
- Reducción tiempo carga: 45%

**Problemas y soluciones relacionados con el manejo térmico:**

- Problema: Baja conductividad térmica del LaNi₅ puro
- Solución: Sistema de 30 aletas radiales perforadas de cobre
- Problema: Resistencias térmicas de contacto
- Solución: Optimización de integración tubo-aletas y compactación
- Problema: Distribución térmica no uniforme
- Solución: Configuración radial con espaciado optimizado de 8mm

## 6. Conclusiones y Observaciones

**Resultados principales:**

- Diseño óptimo: 30 aletas radiales de 1.5mm espesor, espaciado 8mm
- Reducción tiempo de carga: 45% respecto a diseño sin aletas
- Aumento conductividad efectiva: 300% (1.2 a 3.6-4.8 W/m·K)
- Uniformidad térmica mejorada: ±3°C en todo el reactor
- Validación modelo: error < 5%, correlación > 95%
- Reproducibilidad: 95% en 100 ciclos validados
- Cinética: Ea (absorción)=21.17 kJ/mol, Ea (desorción)=16.42 kJ/mol

**Recomendaciones:**

- Optimizar contacto térmico aleta-hidruro para minimizar resistencias
- Reducir resistencias interfaciales en tubo-aleta
- Considerar expansión térmica en diseño mecánico
- Implementar control PID de temperatura para operación estable
- Monitoreo continuo de presión durante ciclos
- Realizar ciclos de activación previos (< 20 ciclos)
- Inspección periódica de aletas y limpieza de superficies de contacto

## 7. Referencias Adicionales

- Muthukumar et al. (2012) "Review on design and development of metal hydride based thermal machines"
- Hardy et al. (2012) "Thermal management of metal hydride systems for hydrogen storage"
- Garrison et al. (2011) "Optimization of internal heat exchangers for hydrogen storage tanks"

---

### Notas Adicionales

Modelo matemático 3D completo con ecuaciones de balance de energía, masa, cinética de reacción y ecuación de van't Hoff. Suposiciones: equilibrio térmico local, lecho poroso homogéneo e isotrópico, propiedades termofísicas constantes, conducción dominante. Parámetros cinéticos validados: Ca=59.2 s⁻¹, Cd=9.6 s⁻¹. ΔH=-30.8 kJ/mol H₂, ΔS=-108 J/mol·K.