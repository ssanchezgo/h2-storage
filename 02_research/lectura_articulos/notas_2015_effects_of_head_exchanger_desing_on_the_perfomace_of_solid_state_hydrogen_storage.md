# Notas de Lectura: Effects of heat exchanger design on the performance of a solid state hydrogen storage device

**Autores:** [LAnurag Singh, M.P. Maiya y S. Srinivasa Murthy]
**Referencia BibTeX:** `[IJHE_2015]`
**Fecha de Publicación:** [2015]

---

## 1. Resumen y Propósito del Artículo

Este estudio se centra en el diseño de un intercambiador de calor para un dispositivo de almacenamiento de hidrógeno de estado sólido. Se desarrolló un modelo matemático tridimensional (3-D) para investigar el rendimiento de sorción de un hidruro metálico (MH) de LaNi₅. Se fabricó y probó un prototipo del dispositivo, validando los resultados de la simulación. El estudio examinó los efectos de varios parámetros operativos, como la presión de suministro de hidrógeno y la temperatura y velocidad del fluido de enfriamiento, así como parámetros geométricos del intercambiador de calor, como el número y grosor de las aletas de cobre. Se concluyó que un diseño de intercambiador de calor efectivo puede reducir significativamente los tiempos de carga y descarga.

---

## 2. Puntos Clave y Datos

### Aspectos Principales

**Material**: El estudio utiliza una aleación de hidruro metálico de 1 kg de LaNi₅.

**Transferencia de calor:** La baja conductividad térmica del hidruro metálico ralentiza los procesos de absorción y desorción, lo que hace que un sistema de gestión de calor efectivo sea crucial.

**Diseño del intercambiador:** El diseño propuesto es un dispositivo cilíndrico con un tubo intercambiador de calor anular incrustado, con aletas circulares de cobre radiales.

**Validación del modelo:** El modelo matemático 3-D desarrollado se validó con datos experimentales obtenidos de un prototipo fabricado, mostrando una buena coincidencia entre los resultados simulados y los experimentales

## Modelo Matemático

El modelo matemático 3-D se desarrolló utilizando el software COMSOL Multiphysics y se simplificó mediante varias suposiciones clave:

Existe equilibrio térmico local entre el sólido y el gas dentro del lecho de hidruro.

El lecho poroso del hidruro es homogéneo e isotrópico.

Las propiedades termofísicas son independientes de la temperatura, presión y concentración.

La transferencia de calor por convección dentro del lecho se desprecia, considerando solo la transferencia por conducción.

El hidrógeno se comporta como un gas perfecto.

Las ecuaciones gobernantes del modelo se basan en balances de energía y masa, y en la cinética de reacción:

Ecuación de balance de energía promediada por volumen:
Esta ecuación (3.1 en el artículo) describe cómo cambia la temperatura del lecho de hidruro con el tiempo, considerando la conducción de calor y la generación/absorción de calor por la reacción.

(ρcp)e * (∂T/∂t) = ∇∙(ke∇T) - (1-e)ṁΔH

Ecuación de balance de masa promediada por volumen:
Esta ecuación (3.4 en el artículo) describe el cambio en la densidad de masa del hidruro y el hidrógeno en el tiempo, en función de la tasa de absorción/generación y la difusión.

(1-e) * (∂ρ/∂t) = ṁ + (1-e)∇(D∇ρ)

Cinética de reacción:
La tasa de absorción de hidrógeno por unidad de volumen (

ṁa) se modela con una ecuación que depende de la diferencia entre la presión de suministro y la presión de equilibrio, así como de la densidad del hidruro.

ṁa = Ca *exp(-Ea/RT)* ln(P/Peq) * (ρsat - ρmh)  

Ecuación de van't Hoff:
La presión de equilibrio se determina mediante la relación de van't Hoff, que la relaciona con la temperatura.

### Tabla de Datos Clave

| Figura | Descripción | Puntos clave |
|---|---|---|
| 1 | Esquema del dispositivo y celda unitaria | Muestra el diseño cilíndrico del dispositivo de almacenamiento con el intercambiador de calor de aletas incrustado. |
| 2 | Vista del intercambiador de calor | Muestra el ensamblaje del intercambiador de calor anular con las aletas de cobre perforadas, un diseño clave para reducir el peso y mejorar el contacto térmico.|
| 3 | Validación del modelo | Gráficos que comparan los resultados de la simulación con los datos experimentales para la concentración y la temperatura del lecho.|
| 4 | Características de absorción | Muestra la evolución de la concentración y la temperatura del lecho del hidruro con respecto al tiempo de carga. |
| 5 | Tasa de absorción experimental | Muestra el gráfico de la tasa de absorción de hidrógeno con el tiempo, dividiendo el proceso en dos etapas principales. |
| Tabla 2 | Propiedades termofísicas | Lista de parámetros importantes para los materiales utilizados en la simulación, incluyendo LaNi₅, hidrógeno, acero y cobre. |
