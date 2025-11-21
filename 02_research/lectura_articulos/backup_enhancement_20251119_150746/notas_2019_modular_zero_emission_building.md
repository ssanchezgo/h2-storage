# Notas de Lectura: Sistema Modular de Energía de Hidrógeno para un Edificio de Cero Emisiones (ZEB)

**Autor:** VIDOVIC, Marie

**Año:** 2021

**Revista:** energy





Autores: Naruki Endo a,*, Eisuke Shimoda b, Kiyotaka Goshome a,Toshihiro Yamane b, Tsuyoshi Nozu b,Tetsuhiko Maeda
Año: 2019
Revista/Fuente: Endo et al.2019
País/Institución: Japon

---

## Material de Almacenamiento


Material de Hidruro: TiFe
Cantidad de Hidruro: 520 kg

### Sistema de Gestión Térmica


Sistema de Transferencia de Calor: Todos los componentes principales (electrolizador, tanques de MH, celda de combustible y baterías) están instalados dentro de un contenedor de 12 pies. Esto facilita la reubicación, reduce el espacio de instalación y lo convierte en un "módulo de energía" autónomo que puede ser desplegado cerca de edificios.
Tipo de Aletas: No aplica
Fluido Térmico: No aplica

---

## Resumen General


Este artículo presenta un sistema estacionario de energía de hidrógeno a escala de banco, diseñado para lograr un Edificio de Cero Emisiones (ZEB). El sistema completo, que incluye generación, almacenamiento y uso de hidrógeno, está integrado en contenedores, demostrando un enfoque inherentemente modular y compacto para su despliegue en entornos urbanos. La principal innovación es la integración térmica del sistema y la elección estratégica del hidruro metálico para cumplir con regulaciones estrictas.

---

## 1. Relevancia para el Diseño Modular y Escalable


El diseño del sistema es un excelente ejemplo de modularidad para aplicaciones estacionarias.

Sistema Contenedorizado: Todos los componentes principales (electrolizador, tanques de MH, celda de combustible y baterías) están instalados dentro de un contenedor de 12 pies. Esto facilita la reubicación, reduce el espacio de instalación y lo convierte en un "módulo de energía" autónomo que puede ser desplegado cerca de edificios.
Elección del Hidruro para Entornos Urbanos: Se utiliza una aleación de TiFe (tipo AB) en lugar de las más comunes de tipo LaNi5 (AB5).
 Motivación Principal: La aleación de TiFe tiene una alta resistencia a la pulverización. Como resultado, no se clasifica como material peligroso según la Ley del Servicio de Bomberos de Japón.
 Ventaja Modular: Esto elimina la necesidad de distancias de seguridad obligatorias respecto a los edificios, un requisito para los hidruros peligrosos como el LaNi5 pulverizado. Permite una instalación mucho más compacta y flexible en áreas urbanas densas, un factor clave para los sistemas modulares distribuidos.
Componentes del Sistema:
 Producción: Electrolizador PEM (5 Nm3/h).
 Almacenamiento: Tanques de hidruro metálico con 520 kg de aleación TiFe para almacenar 80 Nm3 de H2.
 Uso: Celda de combustible PEM (3.5 kW).
 Energía: Paneles fotovoltaicos de 20 kW y baterías de Li-ion (20 kWh).

---

## 2. Estrategias de Gestión Térmica


La gestión térmica es uno de los pilares del diseño, enfocada en la eficiencia y la autonomía del sistema.

Integración Térmica entre Celda de Combustible (FC) y Tanques de MH: Esta es la característica más destacada.
 Concepto: El calor residual generado por la celda de combustible PEM durante su operación (agua a ~60 degC) se utiliza para suministrar el calor endotérmico necesario para la desorción de hidrógeno del tanque de hidruro metálico.
 Implementación: Un circuito cerrado con un fluido de transferencia de calor (salmuera al 60%) conecta un intercambiador de placas en la salida de la FC con la camisa de los tanques de MH.
 Resultado: El sistema de almacenamiento de hidrógeno puede liberar hidrógeno de forma continua sin necesidad de una fuente de calor externa, lo que aumenta significativamente la eficiencia general del sistema ("round-trip efficiency").
Refrigeración del Sistema: Se utilizan radiadores y ventiladores en lugar de enfriadores (chillers) o torres de refrigeración para disipar el calor del electrolizador y de los tanques durante la absorción. Esta es una solución más simple, económica y que ahorra espacio, alineada con el concepto de un módulo compacto y de fácil mantenimiento.

---

## 3. Resultados de Rendimiento y Métricas Clave


Material de Almacenamiento (TiFe):
 Capacidad Efectiva: 1.4 wt%, superior a la de las aleaciones AB5 (~1 wt%).
 Activación: Se logró una activación exitosa a temperaturas y presiones moderadas (<70 degC, <1 MPa).
Rendimiento del Sistema:
 Operación Start-Stop: Tanto el electrolizador como la celda de combustible demostraron arranques rápidos (5-10 minutos), lo que los hace adecuados para operaciones intermitentes dictadas por la disponibilidad de energía renovable (solar).
 Logro de ZEB: El sistema, gestionado por un BEMS (Building Energy Management System), demostró experimentalmente la capacidad de lograr un consumo neto de energía cero durante una operación de 24 horas.
Eficiencia de la Integración Térmica: El estudio valida que la integración térmica FC-MH es factible y efectiva incluso con aleaciones de TiFe, que tienen una histéresis de presión más grande que las aleaciones AB5.

---

## Conclusiones para el Proyecto ANH951


1. El Enfoque Modular Contenedorizado es Viable: Un sistema completo de H2 puede ser empaquetado en un formato estándar (contenedor) para facilitar su despliegue y escalabilidad.
2. La Elección del Material MH es Clave para la Regulación: El uso de aleaciones no peligrosas como la de TiFe puede ser un factor decisivo para la viabilidad de proyectos en entornos urbanos o regulados, al eliminar restricciones de espacio.
3. La Integración Térmica es Fundamental para la Eficiencia: El diseño de un sistema modular debe, desde el principio, planificar el aprovechamiento del calor residual de la celda de combustible para la desorción del hidruro. Esto reduce la necesidad de componentes auxiliares (calentadores) y mejora la eficiencia global.
4. Sistema de Control (BEMS): Un sistema de gestión inteligente es indispensable para orquestar la producción, almacenamiento y uso de energía en función de la demanda y la generación renovable, maximizando la autosuficiencia.
