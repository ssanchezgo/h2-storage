# Análisis de Patente: GRZ Hydrogen Storage System (2025)

---

## **1. Datos Generales**

- **Título:** Hydrogen Storage System (Sistema de Almacenamiento de Hidrógeno)
- **Referencia:** Documento técnico de GRZ Technologies (asimilado como patente para este análisis).
- **Autor/Compañía:** GRZ Technologies (spin-off del instituto suizo EMPA).
- **Fecha:** Circa 2025.
- **Tecnología Principal:** Almacenamiento de hidrógeno en estado sólido (hidruros metálicos) con un enfoque en la gestión térmica pasiva y la seguridad intrínseca para aplicaciones comerciales e industriales.

---

## **2. Resumen**

El sistema de GRZ es una solución comercial para el almacenamiento de hidrógeno a baja presión, diseñada para ser segura, compacta y de larga vida útil. La tecnología se centra en el uso de hidruros metálicos de tipo AB₂ (aleaciones base Ti-Zr-Mn) y un diseño de tanque que prioriza la **gestión térmica pasiva**, eliminando la necesidad de sistemas de enfriamiento/calentamiento activos complejos.

El sistema está optimizado para integrarse con electrolizadores y pilas de combustible, ofreciendo una alternativa a los tanques de alta presión (350-700 bar) y al almacenamiento criogénico, especialmente para aplicaciones estacionarias donde la densidad gravimétrica no es el factor más crítico.

---

## **3. Descripción del Diseño y Funcionamiento**

### **Diseño del Reactor (Tanque):**

- **Geometría:** El diseño se basa en un **tanque cilíndrico** que contiene múltiples **tubos concéntricos** o un arreglo de "tubo y carcasa" (shell and tube).
- **Material del Contenedor:** Acero inoxidable (probablemente 316L) para compatibilidad con hidrógeno.
- **Lecho de Hidruro:**
  - El material activo es un hidruro metálico de tipo **AB₂ (aleación de Laves)**, probablemente a base de **Ti-Zr-Mn-Fe**. Estos materiales son conocidos por su buena cinética, resistencia a la desproporción y un costo relativamente bajo.
  - El polvo de hidruro se mezcla con un **agente de mejora de la conductividad térmica**, como **Grafito Natural Expandido (ENG)**, y se compacta en forma de "pellets" o discos.
  - Estos pellets se apilan en el espacio anular entre los tubos concéntricos del reactor.
- **Gestión Térmica (Novedad Clave):**
  - El sistema está diseñado para una **gestión térmica pasiva**. El calor generado durante la absorción (carga) se disipa al ambiente a través de la superficie externa del tanque, a menudo equipada con **aletas de disipación de aluminio**.
  - Durante la desorción (descarga), el calor necesario para la reacción endotérmica se toma del ambiente.
  - Este enfoque elimina la necesidad de bombas, intercambiadores de calor externos y fluidos de transferencia de calor (HTF), simplificando drásticamente el sistema, reduciendo costos y eliminando componentes parásitos que consumen energía.
- **Sistema de Flujo de Gas:**
  - El hidrógeno gaseoso fluye a través de los tubos internos, que actúan como distribuidores y colectores. Estos tubos están hechos de un material poroso o tienen perforaciones finas para permitir que el gas impregne los pellets de hidruro.
  - Se incorporan filtros metálicos sinterizados (micrónicos) para evitar que las finas partículas de hidruro salgan del tanque.

### **Funcionamiento:**

- **Proceso de Carga (Absorción):**
    1. El hidrógeno, proveniente de un electrolizador (típicamente a 15-30 bar), se introduce en el tanque.
    2. La reacción exotérmica comienza. La temperatura del lecho aumenta, pero el calor se disipa de forma natural hacia el exterior a través de las paredes y aletas del tanque.
    3. La presión de carga se mantiene constante. El sistema se "auto-regula": si la disipación de calor es lenta, la temperatura del lecho sube, la presión de equilibrio del hidruro aumenta y la tasa de absorción disminuye hasta que se alcanza un equilibrio con la tasa de disipación de calor.
    4. La carga se completa cuando la presión dentro del tanque se iguala a la presión de suministro.

- **Proceso de Descarga (Desorción):**
    1. Se abre una válvula para suministrar hidrógeno a una pila de combustible o a un punto de uso (a una presión de 1-5 bar).
    2. La reacción endotérmica enfría el lecho. El tanque comienza a absorber calor del ambiente.
    3. Al igual que en la carga, el sistema es pasivo. La tasa de desorción está limitada por la tasa a la que el tanque puede absorber calor del entorno. Para climas fríos, esto puede ser una limitación.
    4. El sistema puede suministrar hidrógeno de forma continua siempre que la tasa de extracción no supere la capacidad de absorción de calor.

---

## **4. Instrumentación y Control**

La instrumentación es minimalista, en línea con la filosofía de diseño pasivo y seguro:

- **Sensores de Temperatura:** Uno o varios termopares o RTDs colocados en la pared del tanque o dentro de un termopozo para monitorear la temperatura general del sistema. No se requiere un mapeo detallado del campo de temperaturas interno para la operación.
- **Sensor de Presión:** Un transductor de presión en la salida del tanque para monitorear la presión interna, que es el indicador principal del estado de carga (State of Charge - SoC).
- **Válvulas:**
  - Una válvula de entrada manual o de solenoide.
  - Una válvula de salida (regulador de presión) para ajustar la presión de suministro.
  - Una **válvula de alivio de presión** por seguridad.
- **Sistema de Control:** No se requiere un PLC complejo. El control se limita a la apertura/cierre de válvulas y al monitoreo de la presión. La gestión térmica es totalmente pasiva y no controlada.

---

## **5. Condiciones de Operación**

- **Hidruro Metálico:** Aleación tipo AB₂ (Ti-Zr-Mn-Fe).
- **Presión de Carga:** Típicamente **10 - 30 bar**. El sistema está diseñado para funcionar con la salida directa de un electrolizador PEM.
- **Presión de Descarga:** Típicamente **1 - 10 bar**, adecuada para la entrada a una pila de combustible.
- **Temperatura de Operación:** Temperatura ambiente (ej. 0 °C a 40 °C). El rendimiento depende de la temperatura ambiente.
- **Capacidad de Almacenamiento:** Los sistemas son modulares, desde ~1 kWh (equivalente a ~30 g de H₂) hasta MWh (cientos de kg).
- **Ciclos de Vida:** > 10,000 ciclos, gracias a la estabilidad del hidruro y la ausencia de estrés térmico por ciclos rápidos.
- **Tiempos Característicos:**
  - **Tiempo de Carga/Descarga:** Depende del tamaño del tanque y la temperatura ambiente. Típicamente **varias horas (ej. 4-8 horas)**. No está diseñado para un reabastecimiento rápido.

---

## **6. Reivindicaciones Clave y Novedad**

- **Seguridad Intrínseca:** El almacenamiento a baja presión (< 30 bar) elimina los riesgos asociados a la alta presión. El tanque puede ser perforado y solo liberará hidrógeno lentamente.
- **Gestión Térmica Pasiva:** La principal novedad es la eliminación de sistemas activos de gestión térmica. Esto reduce el costo, la complejidad, el mantenimiento y aumenta la eficiencia general del sistema (sin consumo parásito).
- **Larga Vida Útil:** La operación a temperatura y presión moderadas, junto con la estabilidad del material, permite una vida útil muy larga, ideal para aplicaciones de almacenamiento de energía estacionario.
- **Integración Directa:** Diseñado para acoplarse directamente a electrolizadores y pilas de combustible sin necesidad de compresores o reguladores complejos, creando un ciclo de energía de hidrógeno simple y robusto.
