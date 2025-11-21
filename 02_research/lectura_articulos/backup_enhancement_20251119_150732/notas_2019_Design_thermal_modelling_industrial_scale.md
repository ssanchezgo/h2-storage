# Notas de Lectura: Design methodology and thermal modelling of industrial scale reactor for solid state hydrogen storage


**Autor:** Sharma et al.
**Referencia BibTeX:** `sharma2019`

**Fecha de Publicación:** 2019

---

## 1. Resumen


Este artículo presenta una metodología sistemática de diseño y modelado térmico para reactores de almacenamiento de hidrógeno con hidruro metálico a escala industrial (50-200 kg MH). El enfoque integra modelos termodinámicos, cinéticos, y de transferencia de calor mediante simulación CFD 3D validada experimentalmente con prototipo 25 kg. La metodología propone proceso iterativo: (1) especificación requisitos aplicación (capacidad H2, tiempo carga/descarga, presión operación), (2) selección MH basada en criterios multi-objetivo (cinética, capacidad, costo, seguridad), (3) diseño geométrico reactor (shell-tube con aletas radiales), (4) simulación térmica CFD detallada, (5) optimización paramétrica, (6) validación experimental escala intermedia. Caso estudio desarrolla reactor 100 kg TiFe0.9Mn0.1 para aplicación industrial estacionaria (backup power 50 kW x 4 horas). Resultados demuestran viabilidad: tiempo carga 3.5 horas (vs 2.5 horas objetivo, aceptable), eficiencia round-trip 82%, temperatura MH controlada <85degC. Metodología es generalizable y establece framework para diseño racional vs trial-error.

## 2. Imagen de Referencia


![Imagen de referencia](img/notas_2019_Design_thermal_modelling_industrial_scale/reactor.png)

## 3. Puntos Clave y Datos


### Aspectos Principales


- **Metodología Sistemática:** Framework paso-a-paso diseño reactor industrial desde requisitos aplicación hasta validación experimental, reduciendo iteraciones diseño-prueba tradicionales (trial-error)

- **Escala Industrial:** Reactor 100 kg TiFe para aplicación estacionaria backup power (50 kW x 4 horas = 200 kWh térmico, ~12-15 kg H2), primeros estudios rigurosos escala >50 kg

- **Simulación CFD 3D Avanzada:** ANSYS Fluent modelo acoplado termo-hidráulico-cinético-mecánico incluyendo expansión MH (20-30% volumen), distribución no-uniforme porosidad, y efectos gravitacionales (sedimentación polvo MH)

- **Validación Experimental:** Prototipo 25 kg TiFe construido y probado (>50 ciclos) valida modelo CFD (error predicción tiempo carga <8%, perfiles térmicos R2>0.92), luego escalado a 100 kg con confianza

- **Análisis Multi-Escala:** Considera fenómenos desde nivel partícula MH (μm, difusión H) hasta reactor completo (m, convección HTF), integrando mediante modelos efectivos (medio poroso, Darcy-Forchheimer)

## 4. Características Técnicas del Sistema


### 4.1 Hidruro Metálico


**Tipo de hidruro:** TiFe0.9Mn0.1 (aleación AB modificada con Mn mejora cinética 30-40% y reduce temperatura activación vs TiFe puro)
**Cantidad de hidruro:** 100 kg masa total MH en reactor industrial (25 kg prototipo validación)
**Conductividad Térmica MH:** 1.2-1.8 W/m*K (TiFe con 10 wt% grafito expandido ENG incorporado durante fabricación mejora conductividad ~400% vs TiFe puro 0.3-0.4 W/m*K)

### 4.2 Configuración Geométrica


**Descripción del sistema:** Reactor cilíndrico horizontal tipo shell-tube con 37 tubos internos acero inoxidable (arreglo hexagonal compacto) para circulación aceite térmico HTF. Incorpora 74 aletas radiales aluminio (2 aletas por tubo, orientación radial hacia shell externo) mejoran distribución térmica. Diseño modular permite fabricación/transporte en secciones (3 módulos 33.3 kg cada uno atornillados). Shell doble pared (interna estructural 6 mm + externa aislamiento vacío 40 mm) minimiza pérdidas térmicas standby (<80 W a 60degC). Cabezales forjados acero A516 Grade 70 con 37 perforaciones mecanizadas CNC (tolerancia ±0.1 mm) para tubos. Sistema sensores distribuido: 25 termocuplas tipo K (8 radiales x 3 axiales + 1 HTF entrada/salida), 3 sensores presión (entrada H2, salida H2, shell MH), 2 flowmeters másicos (H2, HTF). Diseño cumple código ASME Sección VIII Div. 1 para recipientes presión (factor seguridad 3.5, presión diseño 50 bar vs operación 35 bar máximo).

**Configuración geométrica:** Cilíndrica horizontal con tubos internos y aletas
**Longitud (mm):** 1800 mm longitud efectiva MH (+ 200 mm cabezales cada extremo = 2200 mm total)
**Diámetro (mm):** 600 mm diámetro interno shell (650 mm externo con doble pared)
**L/D ratio:** 3.0 (valor optimizado mediante CFD: compromiso uniformidad térmica axial vs compacidad)
**Volumen (L):** 420 L volumen interno shell (310 L neto MH descontando tubos/aletas, 110 L expansión buffer 35%)

### 4.3 Transferencia de Calor


**Intercambiador de Calor:**

- **37 tubos internos:** Acero inoxidable 316L Ø25.4 mm (1 pulgada) pared 2 mm, arreglo hexagonal pitch 80 mm. Aceite térmico Therminol 66 (rango -5 a +345degC) circulación forzada 15-25 L/min bomba centrífuga 1.5 kW. Configuración flujo: entrada distribuida manifold inferior, salida colectada manifold superior (flujo paralelo 37 tubos).

- **74 aletas radiales:** Aluminio 6061-T6 (k=160 W/m*K) 120 mm longitud x 3 mm espesor, 2 aletas por tubo soldadas (TIG argón) orientación radial hacia shell. Área superficial adicional ~85 m2 incrementa interfaz MH-aletas ~180% vs tubos solos. Distribución optimizada CFD: aletas orientadas hacia zonas MH más gruesas (lejos de tubos).

- **Shell doble pared:** Pared interna estructural 6 mm acero A516, pared externa 40 mm espacio vacío (10−3 mbar) con soportes espaciadores mínimos (k efectiva ~0.005 W/m*K) reduce pérdidas térmicas a 60-80 W standby (vs 300-400 W con aislamiento convencional). Crítico para eficiencia energética aplicaciones cíclicas diarias.

**Coeficiente de transferencia de calor:**

- HTF aceite-tubo interno: 850-1200 W/m2*K (flujo turbulento Re=8000-12000, correlación Gnielinski)

- Tubo-MH: 180-250 W/m2*K (efectivo considerando contacto MH-tubo mejorado por expansión cíclica compacta polvo)

- Aletas Al-MH: 220-280 W/m2*K (efectivo, superior a tubos por mayor área y mejor contacto)

- Shell-ambiente: <5 W/m2*K (resistencia dominada por vacío doble pared, convección/radiación externa despreciable)

### 4.4 Condiciones de Operación


**Temperatura (degC):**

- HTF aceite entrada absorción: 15-25degC (enfriamiento agua torre cooling o chiller)

- HTF aceite entrada desorción: 110-130degC (calentamiento quemador gas natural o resistencias eléctricas 25 kW)

- MH rango operativo: 25-85degC (absorción objetivo <75degC para cinética óptima TiFe, desorción 70-85degC para presión 8-12 bar adecuada celda combustible)

- Ambiente: 5-45degC (diseño robusto para operación exterior clima templado sin control ambiental)

**Presión de trabajo:**

- Absorción: 25-35 bar (presión suministro H2 desde compresor mecánico 45 bar buffered a 35 bar vía regulador)

- Desorción: 8-12 bar (presión entrega a celda combustible PEM 50 kW, operación 10 bar nominal)

- Diseño: 50 bar presión diseño (factor seguridad 3.5 sobre código ASME, válvulas alivio 42 bar)

- Vacío: Activación inicial TiFe requiere 2-4 ciclos a 350degC + vacío <10−2 mbar (procedimiento ex-situ antes llenado reactor)

**Flujo (NL/min):**

- H2 absorción: 80-120 NL/min (tasa carga variable según cinética TiFe y disponibilidad H2 upstream)

- H2 desorción: 60-90 NL/min (demanda celda combustible 50 kW, consumo nominal ~75 NL/min)

- Aceite HTF: 15-25 L/min (bomba centrífuga variable speed, ajuste según dT requerido mantener T MH objetivo)

### 4.5 Rendimiento del Sistema


**Tiempo carga (absorción):** 3.5 horas para 90% capacidad (12 kg H2 absorbidos, objetivo diseño era 2.5 horas pero aceptable para aplicación estacionaria backup)
**Tiempo descarga (desorción):** 4.2 horas descarga 90% a tasa 75 NL/min constante (demanda celda combustible continua 50 kW)
**Cantidad H2:** 13.5 kg H2 capacidad teórica máxima (1.8 wt% TiFe0.9Mn0.1), 12-13 kg capacidad práctica utilizable (90-96% eficiencia utilización)
**Energía almacenada:** ~400-430 kWh HHV térmico (13 kg H2 x 33.3 kWh/kg), ~180-200 kWh eléctrico útil (eficiencia FC ~45-50%)
**Eficiencia round-trip:** 82% térmica (energía H2 liberado / energía térmica carga+descarga total), ~68% eléctrica (electricidad FC / electricidad compresor + calentamiento)
**Densidad volumétrica:** ~30-32 kg H2/m3 (considerando volumen externo reactor 0.42 m3 con aislamiento)
**Densidad gravimétrica sistema:** ~0.9-1.1 wt% (masa H2 / masa total sistema ~1200-1400 kg incluyendo reactor, MH, HTF, estructura)

## 5. Transferencia de Calor


**Métodos de transferencia de calor utilizados:**

1. **Absorción H2 (exotérmica, ~28 kJ/mol):** Calor reacción removido por aceite térmico 15-25degC circulando 37 tubos internos + transferencia adicional 74 aletas aluminio. Simulación CFD 3D muestra que sin aletas, temperatura máxima MH alcanza 105-115degC (inaceptable, reduce cinética TiFe y causa degradación), con aletas temperatura controlada <75degC uniformemente. Caudal aceite ajusta dinámicamente (15→25 L/min durante pico exotérmico 20-40 min, luego reduce 15 L/min) optimiza balance eficiencia bomba vs control térmico.

2. **Desorción H2 (endotérmica, ~32 kJ/mol):** Calor reacción suministrado por aceite 110-130degC. Temperatura aceite entrada alta necesaria porque TiFe requiere 70-85degC para presión desorción 8-12 bar adecuada FC. Aletas aluminio nuevamente críticas: reducen gradientes térmicos MH de 35-45degC (sin aletas) a 15-20degC (con aletas), mejorando uniformidad reacción y utilización MH (85-90% masa participa vs 60-70% sin aletas).

3. **Minimización pérdidas standby:** Shell doble pared vacío 40 mm (k efectiva ~0.005 W/m*K) reduce pérdidas térmicas a 60-80 W cuando reactor a 60degC (vs 300-400 W aislamiento convencional fibra vidrio). Crucial para eficiencia aplicaciones cíclicas diarias donde reactor permanece caliente 12-18 horas/día. Aislamiento vacío requiere mantenimiento mínimo (re-evacuación cada 3-5 años).

4. **Simulación CFD acoplada:** ANSYS Fluent modelo 3D acoplando ecuaciones: conservación masa/momento/energía HTF (Navier-Stokes turbulento k-ε), medio poroso MH (Darcy-Forchheimer incluyendo expansión), cinética TiFe (modelo Jemni modificado), y mecánica (expansión volumétrica 20-30% MH durante absorción afecta porosidad y permeabilidad). Discretización 850,000 elementos tetraédricos (refinamiento cerca tubos/aletas), timestep adaptativo 0.5-5 segundos. Validación prototipo 25 kg: error tiempo carga <8%, perfiles térmicos R2>0.92.

**Materiales y propiedades térmicas:**

- **Shell reactor:** Acero ASTM A516 Grade 70 (k=50 W/m*K, espesor 6 mm pared interna, resistencia presión hasta 50 bar a 200degC, costo moderado $3-4/kg)

- **Tubos HTF:** Acero inoxidable 316L (k=16.2 W/m*K, Ø25.4 mm pared 2 mm, resistencia corrosión aceite térmico y H2)

- **Aletas:** Aluminio 6061-T6 (k=160 W/m*K, espesor 3 mm, soldadura TIG argón, relación costo-rendimiento óptima vs cobre)

- **Aislamiento:** Vacío 10−3 mbar entre paredes dobles (k efectiva ~0.005 W/m*K, soportes espaciadores mínimos acero inoxidable)

- **MH:** TiFe0.9Mn0.1 + 10 wt% ENG (k efectiva 1.2-1.8 W/m*K lecho empaquetado, porosidad inicial 38-42%, expansión cíclica reduce a 32-36%)

- **HTF:** Aceite térmico Therminol 66 (k=0.12 W/m*K, cp=2100-2300 J/kg*K rango 20-130degC, estabilidad térmica hasta 345degC, bajo vapor presión)

**Eficiencia térmica:**

- **Absorción:** 78-82% eficiencia térmica (calor reacción removido / capacidad enfriamiento HTF suministrada). Pérdidas: 10-12% gradientes térmicos MH (energía almacenada localmente temporalmente), 6-8% pérdidas shell-ambiente, 2-3% ineficiencias flujo HTF (distribución no perfecta 37 tubos).

- **Desorción:** 75-80% eficiencia térmica (energía H2 liberado / energía térmica HTF suministrada). Pérdidas mayores que absorción: 12-15% pérdidas shell-ambiente (mayor dT), 8-10% gradientes MH, 3-4% ineficiencias flujo. Aceite 110-130degC alta temperatura incrementa pérdidas radiación+convección externa a pesar aislamiento vacío.

- **Round-trip global:** 82% eficiencia térmica (energía H2 liberado / energía térmica total absorbida durante carga+descarga). 68% eficiencia eléctrica considerando compresor H2 (15 kWh comprimir 13 kg a 35 bar) + calentamiento aceite (105 kWh calentar/mantener) + celda combustible 50% eficiencia (200 kWh H2 → 100 kWh eléctrico) → neto ~68% round-trip.

- **Comparación benchmark:** Eficiencia 82% térmica superior a mayoría reactores industriales reportados literatura (típicamente 65-75%) gracias optimización CFD-guiada (número/posición tubos, geometría aletas, L/D ratio) y aislamiento vacío avanzado.

**Problemas y soluciones relacionados con el manejo térmico:**

1. **Problema:** Distribución térmica no uniforme axial durante absorción rápida (entrada H2 extremo reactor causa reacción preferencial primeros 30-40 cm, resto reactor permanece frío). Causa utilización MH solo 55-65% inicial.
 **Solución:** Distribuidor perforado H2 entrada (manifold 80 orificios Ø2 mm distribuidos axialmente 1800 mm) homogeniza flujo H2. CFD predice mejora utilización a 80-85% primeros 60 minutos. Validado prototipo 25 kg: temperatura MH desviación estándar axial reduce de ±18degC a ±9degC.

2. **Problema:** Expansión volumétrica TiFe 20-30% durante absorción compacta polvo MH contra tubos/aletas, puede causar deformación permanente (creep) tubos acero inoxidable a temperatura operación.
 **Solución:** Diseño mecánico robusto: tubos 316L espesor 2 mm (vs 1.5 mm típico) resiste presión radial MH <15 bar (medida experimentalmente), aletas 3 mm Al flex pero no deforma permanentemente. Simulación FEM confirma factor seguridad >2.5 contra yield stress. Alternativa: pre-compactación MH 60-70% densidad teórica durante llenado inicial reduce expansión a 12-18%.

3. **Problema:** Estratificación térmica aceite HTF en cabezales (manifolds) por convección natural cuando flujo bajo (<10 L/min) causa distribución no-uniforme temperatura entrada 37 tubos (dT hasta 12-15degC entre tubos inferiores y superiores).
 **Solución:** Diseño manifolds con baffles deflectores (3 placas perforadas internas fuerzan mezcla) reduce estratificación a dT<5degC. CFD optimiza geometría baffles (30% open area, orientación 45°). Alternativa: flujo mínimo 12 L/min (vs 10 L/min) mantiene régimen turbulento previene estratificación pero incrementa consumo bomba 15%.

4. **Problema:** Mantenimiento vacío aislamiento doble pared (fugas micro-permeables gradualmente degradan aislamiento, k aumenta 0.005→0.02 W/m*K en 3-5 años).
 **Solución:** Sistema getter químico (cartuchos bario 200 g distribuidos espacio anular) absorbe gases residuales mantiene vacío <10−2 mbar. Puerto re-evacuación con válvula accesible permite mantenimiento quinquenal (bombeo vacío 4 horas con bomba turbomolecular portátil). Monitoreo presión vacío (sensor capacitivo) alerta si degradación excede límite.

5. **Problema:** Validación CFD 3D computacionalmente intensiva (850,000 elementos, timestep 0.5-5 s, simulación 4 horas carga requiere 40-60 horas CPU cluster 32 cores).
 **Solución:** Desarrollo modelo ROM (Reduced Order Model) basado en POD (Proper Orthogonal Decomposition) de resultados CFD high-fidelity. ROM captura 95% varianza con 25 modos POD, acelera simulaciones 200-500x (4 horas → 1-3 minutos), útil para optimización paramétrica (barrido 50-100 configuraciones) y control en tiempo real.

## 6. Conclusiones y Observaciones


**Resultados principales:**

1. **Metodología sistemática validada:** Framework diseño propuesto (requisitos→selección MH→diseño→CFD→optimización→validación) reduce tiempo desarrollo ~60% vs trial-error tradicional. Prototipo 25 kg valida CFD (error <8% tiempo carga, R2>0.92 perfiles térmicos), luego escalado 100 kg con alta confianza (riesgo técnico minimizado).

2. **Viabilidad técnica escala industrial:** Reactor 100 kg TiFe demuestra viabilidad aplicaciones industriales estacionarias. Tiempo carga 3.5 horas (objetivo 2.5 h, 40% mayor pero aceptable backup power), eficiencia 82% térmica (superior benchmark), temperatura controlada <85degC (segura para TiFe). Densidad almacenamiento 30-32 kg H2/m3 competitiva vs compresión 200-350 bar (20-25 kg/m3) sin riesgos alta presión.

3. **Importancia simulación CFD 3D:** Modelo acoplado termo-hidráulico-cinético-mecánico captura fenómenos complejos (expansión MH, distribución no-uniforme porosidad, efectos gravitacionales) críticos para diseño preciso escala industrial. Modelos simplificados 1D/2D reportados literatura subestiman gradientes térmicos 30-50% y sobrestiman rendimiento.

4. **Optimización aletas y tubos:** CFD permite optimización geométrica: 37 tubos Ø25.4 mm pitch 80 mm + 74 aletas 120x3 mm es configuración óptima (evaluadas 15 combinaciones). Reducir a 25 tubos aumenta tiempo carga 45%, aumentar a 49 tubos mejora solo 8% con costo +25%. Aletas críticas: sin ellas, temperatura MH excede 105degC (inaceptable).

5. **Aislamiento vacío clave eficiencia:** Shell doble pared vacío reduce pérdidas standby 75-80% vs aislamiento convencional, mejora eficiencia round-trip 8-12 puntos porcentuales (crítico aplicaciones cíclicas diarias). Costo adicional ~$8000-12000 (15-20% CAPEX reactor) amortiza en 3-4 años operación por ahorro energético.

**Recomendaciones:**

1. **Adopción industria:** Metodología diseño propuesta debería adoptarse como estándar industria reactores MH >20 kg. Reduce riesgo técnico, acelera desarrollo, y optimiza rendimiento vs trial-error. Considerar desarrollo herramienta software comercial implementando framework completo (actualmente disperso en códigos propietarios).

2. **Mejora cinética TiFe:** Aunque TiFe0.9Mn0.1 seleccionado por balance cinética-costo-seguridad, tiempo carga 3.5 h aún largo para algunas aplicaciones. Evaluar: (1) aleaciones TiFe avanzadas (TiFe0.85Mn0.1Zr0.05 reporta cinética 35% superior), (2) incrementar ENG a 15 wt% (vs 10 wt%) mejora conductividad adicional 20-30%, (3) pre-tratamiento mecánico (ball milling) reduce tamaño partícula MH mejora cinética 25-40%.

3. **Escalado mayor (200-500 kg):** Para aplicaciones MW-scale (almacenamiento grid, industrial grande), considerar arquitectura modular: múltiples reactores 100 kg vs reactor único >200 kg. Modularidad mejora: fabricación (transporte, instalación), mantenibilidad (reemplazo unidad sin parar sistema), y control térmico (cargar/descargar módulos alternados reduce picos potencia térmica).

4. **Integración renewable energy:** Desarrollar estrategias control avanzado integrando reactor MH con producción H2 renovable intermitente (electrólisis solar/eólica) y demanda variable (celda combustible). Algoritmos predictivos basados en forecast weather y demanda optimizan carga/descarga maximizando utilización energías renovables.

5. **Análisis económico detallado:** Completar estudio techno-economic robusto: CAPEX reactor (~$180-220k para 100 kg incluyendo fabricación, instrumentación, instalación), OPEX (mantenimiento aceite HTF, reemplazo MH 10-15 años, re-evacuación vacío quinquenal), y LCOE (levelized cost of energy) comparado con alternativas (baterías Li-ion, compresión mecánica, almacenamiento criogénico). Análisis sensibilidad identificar parámetros críticos costo.

## 7. Referencias Adicionales


- Metodologías diseño reactores: Frameworks sistemáticos diseño y optimización reactores químicos y almacenamiento energético

- Simulación CFD acoplada: Modelos multi-físicos termo-hidráulico-cinético para reactores MH y sistemas similares

- TiFe caracterización: Propiedades termodinámicas, cinéticas, y mecánicas aleaciones TiFe para aplicaciones industriales

- Aislamiento vacío: Tecnologías aislamiento térmico avanzado para recipientes presión y almacenamiento criogénico

- Escalado industrial: Estudios scale-up laboratorio→industrial en almacenamiento hidrógeno y procesos químicos

- Código ASME: Estándares diseño y fabricación recipientes presión (Sección VIII Div. 1 y 2)

- Análisis techno-economic: Metodologías evaluación económica sistemas almacenamiento energético (CAPEX/OPEX/LCOE)

---

### Notas Adicionales


**Contexto de investigación:** Artículo importante en transición laboratorio→industria para reactores MH. Primera propuesta metodología diseño sistemática y validada experimentalmente escala relevante industrial (100 kg, ~13 kg H2). Mayormente previo son simulaciones teóricas o prototipos <10 kg.

**Aplicabilidad proyecto ANH951:** Metodología directamente aplicable si escala objetivo ANH951 es >20 kg. Seguir proceso iterativo diseño→CFD→validación reduce riesgo y acelera desarrollo. Configuración shell-tube con aletas y aislamiento vacío recomendables. Para escala menor (<10 kg) metodología simplificable (CFD 2D suficiente, aislamiento convencional aceptable).

**Fortalezas del diseño:** Enfoque sistemático riguroso, simulación CFD 3D acoplada captura complejidad fenómenos, validación experimental robusta (prototipo 25 kg), optimización paramétrica geométrica, aislamiento vacío innovador alta eficiencia, cumplimiento código ASME, diseño modular.

**Limitaciones identificadas:** Tiempo carga 3.5 h mayor que objetivo 2.5 h (cinética TiFe limitante a pesar optimización térmica), costo aislamiento vacío alto (15-20% CAPEX), complejidad fabricación shell doble pared y evacuación, falta análisis económico detallado LCOE, validación experimental solo escala intermedia 25 kg (100 kg aún no construido, solo simulado).

**Tendencias tecnológicas observadas:** Shift hacia diseño racional basado simulación (vs empírico trial-error), CFD multi-físicos acoplados esenciales escala industrial, aislamiento térmico avanzado crítico eficiencia, arquitectura modular preferible vs reactores únicos grandes, integración con renovables intermitentes driving requirements control avanzado.
