# Análisis: Estudios Experimentales en un Reactor Multi-tubular a Gran Escala (50 kg LaNi5)


**Referencia:** *Experimental studies on novel multi tubular reactor with shell having integrated buffer storage for 50 kg of LaNi5*

**Fecha de Análisis:** 14 de noviembre de 2025

---

## Resumen General


Este artículo detalla el diseño, fabricación y experimentación de un reactor de hidruros metálicos de gran capacidad, diseñado para almacenar **50 kg de LaNi5**. El objetivo principal es desarrollar un sistema de almacenamiento de hidrógeno seguro y eficiente a gran escala, abordando los desafíos de la gestión térmica y la dinámica de los gases durante la operación. El diseño se basa en un intercambiador de calor de tipo carcasa y tubos, una configuración inherentemente modular.

---

## 1. Relevancia para el Diseño Modular y Escalable


Este estudio es un caso práctico de **escalado ("scale-up")** mediante un diseño multi-tubular, que puede considerarse una forma de modularidad interna. En lugar de conectar múltiples reactores pequeños, se construye una única unidad grande que contiene múltiples tubos (módulos de reacción).

- **Diseño Multi-tubular:** El reactor consiste en **19 tubos** de acero inoxidable (SS304) de 25.4 mm de diámetro, cada uno llenado con el hidruro metálico. Estos tubos están encapsulados dentro de una carcasa más grande por donde circula el fluido de transferencia de calor (HTF).

- **Buffer de Almacenamiento Integrado:** Una de las innovaciones clave es la integración de un **tanque buffer de 1 m3**. Este componente es crucial para la fase de desorción, ya que absorbe el pico de presión inicial cuando el hidrógeno se libera a alta velocidad, permitiendo una entrega de gas a un flujo y presión constantes (250 slpm en este caso). Para un sistema modular escalable, un buffer centralizado o buffers distribuidos serían esenciales para la operabilidad.

---

## 2. Estrategias de Gestión Térmica


La gestión térmica es el factor más crítico para el rendimiento de este reactor a gran escala. La naturaleza exotérmica de la absorción y endotérmica de la desorción requiere un sistema de intercambio de calor muy eficiente.

- **Intercambiador de Carcasa y Tubos (Shell-and-Tube):** Este es el corazón del sistema de gestión térmica. El agua, como HTF, fluye por la carcasa, rodeando los 19 tubos que contienen el hidruro. Esto permite una transferencia de calor efectiva hacia o desde el lecho de hidruro.

- **Inclusión de Deflectores (Baffles):** Se instalan **deflectores segmentarios** en la carcasa. Su función es:
 1. **Aumentar la Turbulencia:** Obligan al HTF a seguir un camino en zigzag, aumentando la turbulencia (mayor número de Reynolds).
 2. **Mejorar el Coeficiente de Transferencia de Calor (HTC):** La mayor turbulencia mejora significativamente el HTC en el lado de la carcasa, lo que resulta en una absorción y desorción mucho más rápidas en comparación con un diseño sin deflectores.
 3. **Soporte Estructural:** También sirven como soporte para los tubos.

- **Resultados de la Gestión Térmica:** El diseño con deflectores demostró ser muy superior, logrando una absorción casi completa en un tiempo significativamente menor.

---

## 3. Resultados de Rendimiento y Métricas Clave


Los resultados experimentales validan el diseño y proporcionan métricas de rendimiento cruciales.

- **Capacidad de Almacenamiento:** El reactor almacenó **~49.5 kg de hidrógeno**, alcanzando una capacidad gravimétrica de aproximadamente **1 wt%** (típico para LaNi5).

- **Tiempo de Absorción:** Se logró una absorción del **90% de la capacidad en 1286 segundos (~21.4 minutos)** bajo una presión de suministro de 15 bar y con el HTF a 25 degC.

- **Tiempo de Desorción:** El sistema fue capaz de liberar hidrógeno a un flujo constante de **250 slpm**, gracias al tanque buffer que gestionó la dinámica de presión.

- **Eficiencia del Diseño:** El estudio compara el rendimiento con y sin deflectores, concluyendo que los deflectores son una adición de bajo costo que mejora drásticamente el rendimiento térmico y, por lo tanto, la cinética del sistema.

---

## Conclusiones para el Proyecto ANH951


1. **Validación del Diseño Multi-tubular:** El enfoque de carcasa y tubos es una estrategia de diseño viable y probada para reactores de gran escala. Es una base sólida para un diseño modular.
2. **Importancia Crítica de los Deflectores:** Para cualquier diseño que utilice un HTF circulante en una carcasa, la inclusión de deflectores es una optimización de alto impacto y bajo costo para maximizar la transferencia de calor.
3. **Necesidad de un Sistema Buffer:** Para aplicaciones que requieren un suministro de hidrógeno constante y controlado (como alimentar una celda de combustible), un tanque buffer es un componente indispensable en un sistema a gran escala para gestionar la dinámica de la desorción. El diseño modular debe considerar la integración de esta capacidad.
4. **Base para Modelado CFD:** Los datos experimentales de este reactor (temperaturas, presiones, tiempos) son una excelente referencia para validar modelos CFD de un solo tubo o de un reactor multi-tubular completo.
