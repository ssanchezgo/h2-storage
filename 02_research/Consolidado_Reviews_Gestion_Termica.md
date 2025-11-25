# Consolidado Técnico: Diseño Integral de Reactores de Hidruros Metálicos

**Contexto:** Desarrollo de Reactor de Hidruro Metálico para Almacenamiento de Hidrógeno  
**Fuentes Principales:**
1.  **Su et al. (2025):** *Review on thermal design and thermal management for metal hydride reactors.*
2.  **Larpruenrudee et al. (2025):** *A Review on the Overall Performance of Metal Hydride-Based Hydrogen Storage Systems.*
3.  **Liu et al. (2024):** *Metal Hydride Storage Systems: Approaches to Improve Their Performances.*
4.  **Usman (2022):** *Hydrogen storage methods: Review and current status.*
5.  **Afzal et al. (2017):** *Heat transfer techniques in metal hydride hydrogen storage: A review.*

---

## 1. Resumen Ejecutivo

El diseño de un reactor de hidruros metálicos (MH) es un problema multidimensional que trasciende la gestión térmica. Si bien la transferencia de calor gobierna la cinética, la viabilidad del sistema depende igualmente de la selección correcta de la aleación (termodinámica), la integridad mecánica del recipiente (hinchamiento y estrés) y la integración eficiente con el balance de planta (BOP). Este documento consolida los criterios técnicos críticos extraídos de 5 revisiones recientes para el desarrollo de un sistema estacionario, seguro y escalable.

---

## 2. Selección de Materiales de Almacenamiento

La elección del hidruro define las condiciones operativas (P, T) y la densidad energética del sistema. Según **Liu et al. (2024)** y **Su et al. (2025)**, las familias principales se comparan a continuación. **Larpruenrudee et al. (2025)** enfatizan que para aplicaciones estacionarias, la capacidad volumétrica y el costo son prioritarios sobre el peso total del sistema.

| Familia | Ejemplo Típico | Capacidad Gravimétrica | T. Operación (Desorción) | Ventajas | Desventajas | Aplicación Recomendada |
| :--- | :--- | :---: | :---: | :--- | :--- | :--- |
| **Intermetálicos AB5** | $LaNi_5$, $La_{0.9}Ce_{0.1}Ni_5$ | Baja (~1.2 - 1.5 wt%) | Ambiente (20 - 60 °C) | Cinética rápida, fácil activación, presión de equilibrio moderada. | Baja capacidad por peso, alto costo del material (Tierras Raras). | **Estacionaria / Buffer / Compresión** |
| **Intermetálicos AB2** | $TiMn_2$, $ZrV_2$ | Media (~1.8 - 2.0 wt%) | Ambiente a Media | Mejor capacidad que AB5, menor costo de materias primas. | Mayor histéresis, activación más difícil, pendientes en el plateau. | **Estacionaria de mayor capacidad** |
| **Base Magnesio** | $MgH_2$ | Alta (7.6 wt%) | Alta (> 300 °C) | Alta densidad energética, bajo costo del Mg. | Cinética lenta, requiere altas temperaturas (difícil gestión térmica). | **Almacenamiento térmico / Largo plazo** |
| **Hidruros Complejos** | $NaAlH_4$ | Media-Alta (~5.0 wt%) | Media (~150 °C) | Buen balance T/Capacidad. | Reversibilidad compleja, degradación con ciclos. | **Aplicaciones específicas** |

**Criterio de Selección:** Para un sistema estacionario donde el peso no es la restricción primaria pero la respuesta rápida y la seguridad sí lo son, los compuestos **tipo AB5 (LaNi5 modificados)** son la opción más madura y fiable, permitiendo operar con calor residual de baja calidad (<60°C) [Su et al., 2025].

---

## 3. Gestión Térmica: Estrategias de Diseño

La naturaleza exotérmica de la absorción y endotérmica de la desorción impone una limitación termodinámica directa. Dado que los lechos de hidruro poseen una conductividad térmica extremadamente baja ($0.1 - 1.5 W/m\cdot K$), se requieren estrategias de ingeniería robustas. **Afzal et al. (2017)** clasifican estas estrategias en pasivas y activas.

### 3.1 Estrategias Pasivas (Optimización del Lecho)
*   **Matrices de Grafito (ENG):** La adición de 5-10% de Grafito Natural Expandido compactado aumenta la conductividad radial significativamente sin penalizar excesivamente el peso. Es más costo-efectiva que las espumas metálicas para grandes volúmenes [Afzal et al., 2017].
*   **Compactación (Pellets):** Mejora la conductividad pero reduce la permeabilidad. Se recomienda solo si se diseñan canales de distribución de gas dedicados.

### 3.2 Estrategias Activas (Diseño del Reactor)
*   **Intercambiadores Internos:** Para diámetros de reactor >50mm, las camisas externas son ineficaces. Se deben implementar **serpentines helicoidales internos** o tubos aleteados para reducir la distancia de conducción térmica a <10-15mm en cualquier punto del lecho [Su et al., 2025].
*   **Flujo de Fluido (HTF):** El diseño debe asegurar un flujo turbulento en el intercambiador para maximizar el coeficiente convectivo ($h$), compensando la resistencia conductiva del lecho. **Larpruenrudee et al. (2025)** destacan que la temperatura inicial del HTF y la presión de suministro de hidrógeno son los parámetros principales para aumentar la tasa de sorción.

---

## 4. Consideraciones Mecánicas y de Seguridad

El comportamiento físico del polvo de hidruro introduce desafíos mecánicos que a menudo se subestiman en el diseño conceptual. **Usman (2022)** señala que, aunque el almacenamiento sólido es más seguro que el líquido o comprimido, la gestión de la expansión es crítica.

### 4.1 Decrepitación (Pulverización)
*   **Fenómeno:** Tras los primeros ciclos de hidrogenación, las partículas metálicas se fracturan debido a la expansión de la red cristalina, reduciendo su tamaño de ~100 $\mu m$ a <10 $\mu m$.
*   **Impacto:**
    *   *Positivo:* Aumenta el área superficial y mejora la cinética.
    *   *Negativo:* El polvo fino tiende a compactarse en el fondo (autodensificación) y puede migrar hacia las tuberías.
*   **Solución de Ingeniería:** Implementar **filtros sinterizados porosos** (tamaño de poro < 2-5 $\mu m$) en las líneas de gas para evitar la contaminación de válvulas y sensores. Diseñar el reactor con espacio libre (plenum) para permitir la expansión del lecho.

### 4.2 Hinchamiento y Estrés Mecánico (Swelling)
*   **Fenómeno:** La absorción de hidrógeno provoca una expansión volumétrica del material de entre el 15% y el 25%.
*   **Riesgo:** En reactores cilíndricos empacados densamente, esta expansión genera tensiones radiales ("Hoop Stress") que pueden deformar plásticamente o romper el recipiente, especialmente en la base debido a la compactación por gravedad.
*   **Mitigación:**
    *   Limitar la densidad de empaquetamiento inicial (dejar ~30-40% de volumen libre).
    *   Usar arquitectura modular horizontal o compartimentada para reducir la columna hidrostática del polvo.
    *   Considerar recipientes de acero inoxidable austenítico (316L) resistentes a la fragilización por hidrógeno.

---

## 5. Integración de Sistemas (Coupling) y Control

La eficiencia global del sistema depende de su integración con las fuentes y sumideros de energía.

*   **Acoplamiento con Celdas de Combustible (PEMFC):**
    *   El calor residual de una PEMFC (operando a ~60-80°C) es ideal para suministrar la entalpía de desorción de hidruros tipo AB5, cerrando el ciclo energético sin necesidad de fuentes externas de calor [Su et al., 2025].
*   **Control Inteligente:**
    *   El uso de algoritmos predictivos (Machine Learning) permite anticipar los frentes de reacción térmica. Controlar el caudal del HTF basándose en la derivada de la presión y temperatura permite evitar picos térmicos que bloquean la absorción (por contrapresión de equilibrio) o caídas de temperatura que detienen la desorción [Su et al., 2025].

---

## 6. Recomendaciones Finales para el Prototipo

1.  **Material:** Seleccionar una aleación **AB5 ($LaNi_5$ modificado)** por su robustez, facilidad de activación y operación a baja presión/temperatura, ideal para validación segura [Liu et al., 2024].
2.  **Arquitectura:** Diseñar un sistema **modular tubular** (ej. banco de tubos de 3-4 pulgadas) en lugar de un tanque único de gran diámetro para mitigar la autodensificación [Larpruenrudee et al., 2025].
3.  **Gestión Térmica:** Implementar **tubos internos con aletas longitudinales** o serpentines. Es la solución más balanceada entre manufacturabilidad y rendimiento [Afzal et al., 2017].
4.  **Seguridad Mecánica:** Instalar filtros de alta calidad (sinterizados) y llenar los módulos solo al 60-70% de su volumen físico para acomodar el hinchamiento [Usman, 2022].
5.  **Instrumentación:** Incluir termopares multipunto *dentro* del lecho (no solo en la pared) para monitorear la propagación del frente de reacción y validar los modelos térmicos.
