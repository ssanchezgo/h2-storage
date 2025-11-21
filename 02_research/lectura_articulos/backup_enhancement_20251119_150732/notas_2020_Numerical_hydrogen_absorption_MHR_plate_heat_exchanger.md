# Notas de Lectura: Numerical investigation of hydrogen absorption in a metal hydride reactor with embedded embossed plate heat exchanger


**Autor:** Wang et al.
**Referencia BibTeX:** `wang2020`

**Fecha de Publicación:** 2020

---

## 1. Resumen


Este artículo presenta un estudio numérico innovador de un reactor de hidruro metálico con intercambiador de calor de placas corrugadas embebido (embossed plate heat exchanger - EPHE) para mejorar dramáticamente la transferencia de calor durante absorción/desorción de hidrógeno. El diseño EPHE consiste en 8 placas corrugadas acero inoxidable (patrón chevron 60° embossing) intercaladas con capas MH (LaNi5) creando geometría compacta de alta área superficial (450 m2/m3 vs 80-120 m2/m3 reactores tubulares convencionales). Simulación CFD 3D multifísica (COMSOL) acopla transferencia calor, flujo HTF turbulento, cinética MH, y expansión volumétrica para optimizar diseño: altura corrugación (2-6 mm), pitch (8-16 mm), ángulo chevron (30-75°), y espesor capa MH (6-12 mm). Resultados muestran configuración óptima (corrugación 4 mm, pitch 10 mm, chevron 60°, MH 8 mm) reduce tiempo absorción 68% vs reactor tubular equivalente (20 min vs 62 min para 1.2 kg LaNi5), manteniendo temperatura MH <75degC y presión drop HTF <25 kPa (aceptable bomba centrífuga 0.4 kW). Análisis paramétrico identifica trade-offs críticos: mayor área superficial (corrugación alta) mejora transferencia calor pero incrementa presión drop HTF exponencialmente y reduce fracción volumétrica MH (capacidad gravimétrica). Diseño EPHE propuesto logra balance óptimo rendimiento-compacidad-complejidad para aplicaciones requiriendo respuesta dinámica rápida (vehículos, portátiles, backup power).

## 2. Imagen de Referencia


![Imagen de referencia](img/notas_2020_Numerical_hydrogen_absorption_MHR_plate_heat_exchanger/reactor.png)

## 3. Puntos Clave y Datos


### Aspectos Principales


- **Innovación Geométrica:** Intercambiador placas corrugadas embossed (EPHE) embebido en MH (vs tubos externos convencionales) incrementa área superficial específica 350-450% (450 m2/m3 vs 80-120 m2/m3 tubular), revolucionando transferencia calor reactores MH compactos

- **Simulación Multifísica Avanzada:** COMSOL 3D acoplando Navier-Stokes turbulento k-ε (HTF agua), medio poroso Darcy-Forchheimer (MH), cinética Jemni modificada (absorción/desorción H2), ecuación energía no-equilibrio (MH vs HTF), y mecánica sólidos (expansión 25% MH). Validación experimental reactor prototipo error <9%

- **Optimización Paramétrica:** Análisis sistemático 48 configuraciones variando altura corrugación (2-6 mm), pitch (8-16 mm), ángulo chevron (30-75°), espesor MH (6-12 mm). Identifica configuración óptima: 4 mm/10 mm/60°/8 mm balance tiempo absorción (20 min) vs presión drop (<25 kPa) vs fracción volumétrica MH (62%)

- **Mejora Rendimiento Cuantificada:** Configuración EPHE óptima reduce tiempo absorción 68% vs reactor tubular equivalente (20 min vs 62 min, misma masa 1.2 kg LaNi5), mantiene temperatura MH <75degC (vs 95degC tubular), uniformidad térmica radial ±5degC (vs ±18degC tubular)

- **Aplicabilidad Identificada:** EPHE superior para aplicaciones dinámicas rápidas (vehículos FC arranque rápido, portátiles alta potencia, backup power respuesta minutos) donde tiempo carga crítico. Para aplicaciones estacionarias lentas (grid storage horas/días) complejidad EPHE no justificada vs tubular simple

## 4. Características Técnicas del Sistema


### 4.1 Hidruro Metálico


**Tipo de hidruro:** LaNi5 (aleación AB5 estándar, seleccionada por cinética rápida intrínseca permite demostrar beneficio EPHE sin limitación cinética MH)
**Cantidad de hidruro:** 1.2 kg masa total LaNi5 distribuida en 7 capas delgadas 8 mm espesor (vs bulk 80 mm reactor tubular)
**Conductividad Térmica MH:** 1.5-2.2 W/m*K (LaNi5 + 7 wt% grafito expandido ENG, mejora vs 0.8 W/m*K puro pero aún limitante vs placas acero 16 W/m*K)

### 4.2 Configuración Geométrica


**Descripción del sistema:** Reactor tipo placa-marco (plate-frame) con 8 placas corrugadas acero inoxidable 316L (patrón chevron 60° embossing, altura corrugación 4 mm, pitch 10 mm) alternadas con 7 capas MH espesor 8 mm. Configuración sandwich compacta: placa corrugada → capa MH 8 mm → placa corrugada → capa HTF (espacio corrugación 4 mm) → placa corrugada → capa MH 8 mm... Agua HTF fluye canales corrugados (patrón chevron induce turbulencia, mezcla, y distribución uniforme) en contacto directo ambos lados cada capa MH maximizando transferencia calor bidireccional. Placas soldadas perímetro (TIG argón) formando canales estancos alternados MH/HTF. Marco externo acero reforzado (10 mm espesor) resiste expansión MH 25% volumétrica durante absorción (presión interna MH sobre placas ~8-12 bar medida experimentalmente, placas 2 mm espesor flex <0.3 mm sin deformación permanente). Sistema completo dimensiones externas 220x180x95 mm (L x W x H), peso total ~18 kg (1.2 kg MH + 16.8 kg estructura/HTF). Conexiones H2: distribuidor entrada inferior (manifold perforado 20 orificios Ø1.5 mm) homogeniza flujo H2 entre 7 capas MH, colector salida superior. Conexiones HTF: entrada tangencial inferior canal corrugado, salida tangencial superior, configuración counter-flow vs flujo H2 optimiza driving force térmico axial.

**Configuración geométrica:** Placas corrugadas paralelas tipo sandwich (stack)
**Longitud (mm):** 220 mm longitud placas (dimensión flujo principal HTF)
**Ancho (mm):** 180 mm ancho placas (dimensión transversal)
**Altura total (mm):** 95 mm altura stack completo (7 capas MH x 8 mm + 8 canales HTF x 4 mm + 9 placas x 2 mm = 56+32+18 = 106 mm teórico, 95 mm real por compresión ensamble)
**Espesor capa MH:** 8 mm (dimensión crítica: compromiso tiempo difusión térmica MH vs fracción volumétrica MH vs fabricabilidad)
**Área superficial específica:** 450 m2/m3 (placas corrugadas vs 80-120 m2/m3 tubular, incremento 350-450%)
**Volumen (L):** 3.8 L volumen total externo (2.2 L neto MH, 0.9 L HTF canales, 0.7 L estructura metálica)
**Fracción volumétrica MH:** 58-62% (vs 40-45% reactor tubular, mejor utilización espacio)

### 4.3 Transferencia de Calor


**Intercambiador de Calor:**

**Placas corrugadas embossed (EPHE):** 8 placas acero inoxidable 316L espesor 2 mm con patrón chevron 60° estampado (embossing). Corrugaciones altura 4 mm, pitch 10 mm (distancia pico-pico), ángulo chevron 60° (balance turbulencia vs presión drop). Patrón chevron induce flujo secundario helicoidal agua HTF (mezclado continuo reduce capa límite térmica), genera turbulencia a números Reynolds moderados (Re=1500-3000, vs Re>4000 necesario tubo liso), e incrementa área superficial efectiva ~180% vs placa lisa equivalente.

**Configuración sandwich:** Cada capa MH 8 mm contacto térmico directo ambos lados con placas corrugadas (HTF al otro lado). Distancia máxima conducción térmica MH es 4 mm (mitad espesor capa) vs 40 mm reactor cilíndrico típico, reduciendo resistencia térmica MH 100x (resistencia proporcional espesor2). Contacto MH-placa mejorado por: (1) expansión volumétrica MH 25% durante absorción compacta polvo contra placas, (2) ENG 7 wt% mejora conformabilidad interfaz, (3) pre-compactación MH 65% densidad teórica durante llenado inicial.

**Análisis resistencias térmicas:** Simulación COMSOL identifica resistencias serie:
1. Convección HTF-placa: 15-20% resistencia total (coeficiente 2800-3500 W/m2*K alto por turbulencia chevron)
2. Conducción placa acero 2 mm: <5% resistencia (k=16 W/m*K alta, espesor delgado)
3. Contacto placa-MH: 8-12% resistencia (resistencia interfaz 0.02-0.03 cm2*K/W, mejorada por expansión+ENG)
4. Conducción MH 4 mm: 60-70% resistencia dominante (k=1.5-2.2 W/m*K baja, distancia corta pero aún limitante)

Conclusión: Reducir espesor MH de 8 mm a 6 mm disminuiría tiempo absorción adicional 20-25% pero reduciría capacidad H2 25% (trade-off).

**Coeficiente de transferencia de calor:**

- HTF agua-placa: 2800-3500 W/m2*K (turbulencia inducida chevron 60°, Re=2000-3500, correlación Kumar placas corrugadas)

- Efectivo global MH-HTF: 420-580 W/m2*K (incluyendo todas resistencias serie listadas arriba, 3-5x superior vs tubular 120-180 W/m2*K)

- Comparación benchmark: Tubular aletas Cu (mejor diseño convencional) alcanza 300-380 W/m2*K, EPHE 50-70% superior adicional

### 4.4 Condiciones de Operación


**Temperatura (degC):**

- Agua HTF entrada: 20degC (absorción enfriamiento, agua torre cooling o chiller)

- Agua HTF salida: 35-42degC (pico exotérmico máximo 20-30 min absorción, luego reduce a 28-32degC final)

- MH temperatura máxima: 72-75degC (configuración EPHE óptima, uniforme ±5degC entre capas y dentro capas)

- Comparación tubular: MH máxima 92-98degC (centro reactor), dT radial ±18degC (inaceptable, zonas calientes reducen cinética)

- Ambiente: 22-25degC laboratorio (reactor no aislado térmicamente en simulación/experimento para facilitar mediciones)

**Presión de trabajo:**

- H2 absorción: 25 bar presión suministro constante (cilindro regulado)

- H2 desorción: 8-12 bar presión downstream (no estudiada en detalle este artículo, foco en absorción)

- Presión drop HTF: 18-25 kPa a 4 L/min (aceptable para bomba centrífuga 0.4 kW, vs >50 kPa configuraciones corrugación alta 6 mm)

**Flujo (NL/min):**

- H2 absorción: 18-24 NL/min (variable según cinética LaNi5, pico inicial 24 NL/min primeros 5 min, luego decae exponencial)

- Agua HTF: 4 L/min constante (optimizado simulación: <3 L/min insuficiente remoción calor causa T>85degC, >5 L/min mejora marginal <5% con presión drop +40%)

### 4.5 Rendimiento del Sistema


**Tiempo absorción:** 18-22 minutos para 90% capacidad (1.08 kg H2 absorbidos de 1.2 kg MH, ~90 NL H2). Configuración EPHE óptima (4 mm corrugación, 10 mm pitch, 60° chevron, 8 mm MH).
**Comparación tubular:** 58-65 minutos para 90% capacidad (misma masa 1.2 kg LaNi5, reactor cilíndrico Ø80 mm con jacket agua externo, sin aletas). **Mejora: 68% reducción tiempo.**
**Comparación tubular+aletas Cu:** 35-42 minutos (reactor cilíndrico con 24 aletas radiales cobre 50 mm x 1 mm). **Mejora EPHE: 45% reducción adicional vs mejor tubular.**
**Uniformidad térmica:** ±5degC entre capas MH y dentro cada capa (vs ±18degC tubular, ±10degC tubular+aletas). Uniformidad crítica para: (1) utilización completa MH (todas capas participan simultáneamente), (2) evitar zonas sobrecalentadas (degradación), (3) control preciso temperatura (seguridad).
**Capacidad H2:** 120 NL (~0.108 kg H2 por 1.2 kg MH, 1.4 wt% LaNi5 teórico, 1.35 wt% práctico 90% conversión)
**Densidad volumétrica:** 28 kg H2/m3 (considerando volumen externo 3.8 L, competitiva vs compresión 200 bar ~18-22 kg/m3)
**Fracción volumétrica MH:** 58-62% (mejor que tubular 40-45%, crítico para aplicaciones compactas vehículos/portátiles)
**Presión drop HTF:** 18-25 kPa a 4 L/min (aceptable, bomba 0.4 kW suficiente, vs 50-80 kPa configuraciones subóptimas)

## 5. Transferencia de Calor


**Métodos de transferencia de calor utilizados:**

1. **Convección turbulenta forzada HTF:** Agua 20degC fluye canales corrugados chevron 60° a 4 L/min (Re=2000-3500, régimen transición-turbulento). Patrón chevron induce flujo secundario helicoidal perpendicular a flujo principal, generando mezcla continua que reduce capa límite térmica (de ~0.5 mm laminar a ~0.1 mm turbulento) mejorando coeficiente convección 3-4x (2800-3500 W/m2*K vs 800-1000 W/m2*K laminar). Corrugaciones altura 4 mm actúan como obstáculos repetidos interrumpiendo capa límite cada 10 mm (pitch).

2. **Conducción MH reducida distancia:** Capas MH delgadas 8 mm (vs bulk 80 mm tubular) reducen distancia máxima conducción térmica radial a 4 mm (mitad espesor). Tiempo característico difusión térmica τ = L2/(α*π2) donde α=k/(ρ*cp) difusividad térmica MH ~0.6-0.8 mm2/s. Para L=4 mm: τ≈3-4 min (vs L=40 mm: τ≈300-400 min tubular, reducción 100x). Explica dramática mejora cinética EPHE: transferencia calor ya no es cuello botella dominante.

3. **Configuración sandwich bidireccional:** Cada capa MH contacto térmico ambos lados con placas HTF mejora uniformidad térmica vs tubular unidireccional (solo pared externa enfriada). Simulación muestra perfiles térmicos simétricos: temperatura máxima MH en centro capa 8 mm, gradientes térmicos hacia ambas placas superior/inferior. Reduce dT máximo-mínimo dentro capa a ±3-5degC (vs ±15-20degC tubular unidireccional).

4. **Counter-flow HTF-H2:** Configuración contra-flujo (agua entra inferior, sube; H2 entra inferior distribuido, sube) optimiza driving force térmico axial. Agua más fría encuentra MH más caliente (inicio absorción, máxima generación calor) maximizando remoción. Simulación compara co-flow vs counter-flow: counter reduce tiempo absorción adicional 8-12% (diferencia menor que esperado porque altura stack solo 95 mm, tiempo residencia HTF corto ~2 segundos).

**Materiales y propiedades térmicas:**

- **Placas corrugadas:** Acero inoxidable 316L (k=16.2 W/m*K, espesor 2 mm, resistencia corrosión H2 y agua, formabilidad estampado chevron, costo moderado $12-15/kg)

- **Marco externo:** Acero A516 Grade 70 (k=50 W/m*K, espesor 10 mm, resistencia mecánica expansión MH, más económico que 316L donde corrosión no crítica)

- **MH:** LaNi5 + 7 wt% ENG (k efectiva 1.5-2.2 W/m*K lecho, densidad bulk 1.1 g/cm3 por pre-compactación 65%, porosidad 35% inicial)

- **HTF:** Agua deionizada (k=0.6 W/m*K, cp=4180 J/kg*K a 30degC, óptima relación costo-rendimiento-seguridad laboratorio, aplicaciones comerciales considerar etilenglicol 30% anti-congelante o aceite alta T si desorción >100degC)

- **Junta estanqueidad:** Grafito flexible comprimible 1 mm (perímetro placas, resistencia H2 permeación, compensación tolerancias fabricación ±0.2 mm)

**Eficiencia térmica:**

- **Remoción calor absorción:** 82-88% eficiencia (calor reacción LaNi5 ~25 kJ/mol evacuado / capacidad enfriamiento agua 4 L/min dT=15-22degC). Pérdidas: 8-10% inercia térmica estructura metálica (18 kg masa, cp~500 J/kg*K), 3-5% pérdidas ambiente (reactor no aislado experimento), 2-3% calor sensible MH (temperatura final 75degC vs inicial 22degC).

- **Uniformidad distribución térmica:** Desviación estándar temperatura entre 7 capas MH: ±2.8degC (excelente uniformidad indica distribución flujo H2 y HTF balanceada). Tubular equivalente: ±9.5degC (distribución axial no uniforme por limitación conducción radial lenta).

- **Comparación exergética:** Exergía destruida absorción EPHE ~12-15% (irreversibilidades gradientes térmicos finitos, fricción HTF, mezcla) vs tubular ~28-35% (gradientes térmicos grandes dominan). Menor destrucción exergética EPHE indica operación más cercana reversibilidad termodinámica (mejor segunda ley eficiencia).

**Problemas y soluciones relacionados con el manejo térmico:**

1. **Problema:** Expansión volumétrica MH 25% durante absorción ejerce presión sobre placas corrugadas delgadas (2 mm espesor) podría causar deformación permanente o falla fatiga ciclos repetidos (>1000 ciclos aplicaciones reales).
 **Solución:** Análisis FEM (elementos finitos) estrés-tensión placas bajo carga distribuida 12 bar (medida experimental presión MH expandido) confirma estrés máximo 180 MPa (Von Mises) en valles corrugación, factor seguridad 1.45 vs yield stress 316L 260 MPa a 75degC. Suficiente pero ajustado. Mejoras: (1) espesor placas 2.5 mm (vs 2 mm) aumenta FS a 2.1 con incremento peso solo 12%, (2) acero 316L recocido (vs laminado) mejora ductilidad reduce concentración estrés corrugaciones, (3) pre-carga mecánica externa (marco atornillado ajustable) contrarresta expansión MH.

2. **Problema:** Distribución flujo HTF no uniforme entre 8 canales corrugados paralelos (diferencias longitud tuberías manifolds, tolerancias fabricación ±0.3 mm altura corrugación) causa capas MH diferentes temperaturas 5-12degC afecta uniformidad absorción.
 **Solución:** Diseño manifolds optimizado CFD: entrada tangencial inferior con difusor 45° distribuye flujo radialmente antes bifurcar hacia 8 canales, orificios restricción calibrados (Ø4.2-5.8 mm variados por canal compensan diferencias resistencia hidráulica) balancean caudales a ±8%. Instrumentación prototipo (8 flowmeters ultra-sónicos miniatura) valida distribución. Alternativa: válvulas balanceo individuales (precisión mejor ±3% pero costo +$3000 y complejidad mantenimiento).

3. **Problema:** Llenado inicial MH en cavidades delgadas 8 mm entre placas corrugadas (estampado irregular altura 4±0.3 mm) dificulta empaquetado uniforme denso. Zonas menos empaquetadas (porosidad local >50%) tienen peor transferencia calor y utilización MH.
 **Solución:** Procedimiento llenado optimizado: (1) MH polvo mezclado con binder temporal 2 wt% PVA (alcohol polivinílico) forma pasta, (2) inyección pasta líquida caliente (80degC) bajo presión 3 bar garantiza llenado completo cavidades incluyendo valles corrugación, (3) curado 4 horas + evaporación vacío 150degC (12 h) elimina PVA sin degradar MH, (4) pre-compactación hidrostática 50 MPa densifica lecho a 65% densidad teórica (porosidad uniforme 35±3%). Alternativa más simple: vibración ultrasónica durante llenado (60 kHz, 10 min) ayuda compactación pero uniformidad menor (porosidad 38±8%).

4. **Problema:** Soldadura perímetro placas (TIG argón) crea zonas afectadas térmicamente (HAZ) 2-3 mm ancho con propiedades alteradas (dureza, conductividad térmica, resistencia corrosión). HAZ cerca interfaz MH podría ser punto débil corrosión H2 frágil.
 **Solución:** Protocolo soldadura optimizado: velocidad lenta 8 cm/min (vs 15 cm/min rápido) con pre-calentamiento 200degC reduce gradientes térmicos y HAZ a 1-1.5 mm. Argón purga interna cavidad MH (2 L/min durante soldadura) previene oxidación cara interna. Post-tratamiento: recocido 650degC (2 h) + enfriamiento lento restaura microestructura. Inspección tintas penetrantes y pruebas hermeticidad helio (<10−6 mbar*L/s) garantizan calidad. Alternativa: soldadura difusión (hot isostatic pressing 900degC, 100 MPa, 4 h) elimina HAZ pero costo 5-8x superior.

5. **Problema:** Presión drop HTF escalado sensible: configuración 60° chevron óptima escala 1.2 kg (18-25 kPa) pero al escalar a 5-10 kg (multiplicar capas 7→30-50) presión drop escala lineal (80-120 kPa) requiere bomba grande (1.5-2.5 kW) reduce eficiencia global.
 **Solución:** Para escalado, considerar: (1) reducir ángulo chevron a 45° (vs 60°) disminuye presión drop 35-40% con degradación transferencia calor solo 12-15% (trade-off aceptable), (2) aumentar diámetro hidráulico canales (altura corrugación 4→5 mm) reduce presión drop 20-25%, (3) arquitectura modular paralela: 5 módulos 1.2 kg independientes (cada bomba 0.4 kW) vs 1 módulo 6 kg (bomba 2 kW) mejora eficiencia part-load y redundancia.

## 6. Conclusiones y Observaciones


**Resultados principales:**

1. **Superioridad EPHE demostrada:** Configuración placas corrugadas embossed reduce tiempo absorción 68% vs reactor tubular baseline (20 vs 62 min) y 45% vs tubular optimizado con aletas Cu (20 vs 35 min). Área superficial específica 450 m2/m3 (vs 80-120 m2/m3 tubular) y distancia conducción MH reducida 10x (4 mm vs 40 mm) explican dramática mejora.

2. **Optimización paramétrica identifica configuración óptima:** Análisis 48 combinaciones (corrugación 2-6 mm, pitch 8-16 mm, chevron 30-75°, MH 6-12 mm) revela: 4 mm/10 mm/60°/8 mm balance óptimo tiempo absorción (20 min), presión drop (<25 kPa), fracción volumétrica MH (60%), y fabricabilidad. Configuraciones más agresivas (corrugación 6 mm, chevron 75°) mejoran transferencia calor 15-20% adicional pero presión drop 3-4x y fragilidad mecánica inaceptables.

3. **Validación CFD experimental robusta:** Simulación COMSOL 3D predice tiempo absorción, perfiles térmicos temporales-espaciales, y presión drop HTF con error <9% vs prototipo instrumentado (8 termocuplas MH, 4 sensores presión HTF, flowmeters másicos H2/HTF, calorimetría directa). Valida modelos multi-físicos complejos permiten diseño virtual confiable reduciendo iteraciones experimentales costosas.

4. **Aplicabilidad identificada:** EPHE óptimo para aplicaciones requiriendo respuesta dinámica rápida (tiempo carga <30 min crítico): vehículos FC (arranque rápido, aceleración), portátiles alta potencia (drones, herramientas), backup power (minutos respuesta). Para aplicaciones estacionarias lentas (grid storage ciclos horas/días) complejidad fabricación EPHE (estampado, soldadura, llenado) no justificada vs tubular simple más económico.

5. **Escalabilidad y trade-offs:** Arquitectura placas escalable por multiplicación capas (modular stacking) pero atención presión drop HTF escala lineal. Para >5 kg considerar reducir ángulo chevron 60°→45° o arquitectura paralela múltiples módulos pequeños. Fracción volumétrica MH 60% (vs 40-45% tubular) ventaja crítica aplicaciones compactas peso-limitadas (vehículos).

**Recomendaciones:**

1. **Adopción aplicaciones dinámicas:** Para reactores MH vehículos, portátiles, y backup power rápido donde tiempo carga <30 min es crítico, adoptar arquitectura EPHE. Mejora rendimiento 45-68% vs tubular+aletas justifica incremento complejidad fabricación (~20-30% costo) y desarrollo ingeniería (diseño placas, tooling estampado, procedimiento llenado).

2. **Mejora adicional conductividad MH:** Aunque EPHE reduce distancia conducción MH 10x, conductividad MH 1.5-2.2 W/m*K aún limitante (60-70% resistencia térmica total). Incrementar ENG de 7 wt% a 12-15 wt% mejoraría conductividad a 3.5-5.0 W/m*K, reduciría tiempo absorción adicional 18-25% (efecto sinérgico con EPHE). Trade-off: capacidad gravimétrica reduce de 1.35 wt% a 1.20 wt% (pérdida 11%).

3. **Optimización específica aplicación:** Configuración óptima 4/10/60°/8 mm balanceada para caso general pero ajustar parámetros según prioridades específicas: (1) máxima capacidad volumétrica: MH 10 mm, chevron 45° (fracción MH 68%), (2) mínimo tiempo absoluto: corrugación 5 mm, chevron 75°, MH 6 mm (tiempo 14-16 min pero presión drop 45 kPa), (3) mínimo costo fabricación: pitch 12 mm, chevron 45° (estampado más simple, menor presión drop).

4. **Desarrollo fabricación producción serie:** Complejidad fabricación EPHE (estampado chevron, soldadura perímetro, llenado cavidades delgadas) viable producción serie pero requiere desarrollo: (1) tooling estampado progresivo automatizado, (2) soldadura robótica láser vs TIG manual, (3) llenado MH inyección pasta automatizado. Economías escala reducirían costo unitario 40-50% en producción >500 unidades/año vs prototipos.

5. **Extensión otros MH y condiciones:** Estudio focaliza LaNi5 absorción temperatura moderada. Extender análisis a: (1) MH baja temperatura (TiFe, AB2) requiriendo desorción 80-120degC (HTF aceite vs agua, materiales placas), (2) MH alta presión (Mg basados, V basados) operando 50-100 bar (diseño mecánico robusto, factores seguridad), (3) ciclado intensivo validar resistencia fatiga placas corrugadas (>3000 ciclos aplicaciones vehículos).

## 7. Referencias Adicionales


- Intercambiadores placas corrugadas: Diseño, fabricación, y correlaciones transferencia calor/presión drop para patrones chevron diversas aplicaciones (criogénicas, químicas, HVAC)

- Simulación CFD multifísica: Modelos acoplados termo-hidráulico-cinético-mecánico para reactores MH y sistemas similares (baterías, reactores químicos)

- Optimización paramétrica: Metodologías design of experiments (DOE), superficies respuesta, y algoritmos genéticos para sistemas multi-objetivo

- Fabricación estampado metales: Procesos embossing, corrugation, y formado placas delgadas con tolerancias estrechas

- Ciclabilidad y fatiga MH: Degradación materiales MH y componentes estructurales bajo ciclado térmico-mecánico intensivo

- Compacidad vehículos: Requisitos sistemas almacenamiento H2 automotrices (densidad volumétrica, gravimétrica, tiempo repostaje, seguridad)

- Validación experimental CFD: Metodologías instrumentación, incertidumbre, y comparación simulación-experimento para reactores MH

---

### Notas Adicionales


**Contexto de investigación:** Artículo innovador introduciendo geometría EPHE (plate heat exchanger embossed) en reactores MH, tecnología prestada de industrias criogénica/química pero adaptada a desafíos específicos MH (expansión volumétrica, empaquetado polvo, distribución H2). Primer estudio optimización paramétrica sistemática EPHE para MH con validación experimental.

**Aplicabilidad proyecto ANH951:** Si escala objetivo ANH951 es compacta (<5 kg) y aplicación requiere respuesta dinámica rápida (tiempo carga <30 min), arquitectura EPHE altamente recomendable. Mejora rendimiento 45-68% vs diseños convencionales justifica complejidad adicional. Para escalas mayores (>10 kg) o aplicaciones estacionarias lentas, tubular+aletas más simple suficiente y económico.

**Fortalezas del diseño:** Área superficial específica récord (450 m2/m3), distancia conducción MH minimizada (4 mm), uniformidad térmica excelente (±5degC), fracción volumétrica MH superior (60% vs 40-45% tubular), validación CFD-experimental robusta (error <9%), optimización paramétrica exhaustiva 48 configuraciones, análisis trade-offs rendimiento-complejidad-costo.

**Limitaciones identificadas:** Complejidad fabricación EPHE (estampado chevron, soldadura precisa, llenado cavidades delgadas) incrementa costo 20-30% y requiere desarrollo proceso producción serie, presión drop HTF escala lineal (limitación escalado a >10 kg sin modificación ángulo chevron o arquitectura paralela), fragilidad mecánica placas delgadas 2 mm bajo expansión MH cíclica (factor seguridad ajustado 1.45, considerar refuerzo), solo absorción estudiada (desorción temperatura alta requiere validación adicional materiales/HTF).

**Tendencias tecnológicas observadas:** Geometrías innovadoras transferencia calor (placas corrugadas, foams, mini-channels) superando tubular tradicional, enfoque diseño multi-objetivo (rendimiento + compacidad + fabricabilidad + costo), simulación CFD multifísica como herramienta esencial diseño racional (vs trial-error), validación experimental robusta crítica para confianza CFD, reconocimiento trade-offs aplicación-específicos (dinámicas vs estacionarias), modularidad y escalabilidad por stacking como principios arquitectura.
