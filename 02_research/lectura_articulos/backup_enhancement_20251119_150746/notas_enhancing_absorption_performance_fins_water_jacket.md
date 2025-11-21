# Enhancing absorption performance in metal hydride hydrogen storage: Implementation of fins and a water jacket (2025)


**Autores:** Dae Yeob Lee, Yasser Mahmoudi, Vincenzo Spallina, Amir Keshmiri
**Institución:** School of Engineering, The University of Manchester, UK
**Año:** 2025

**Revista:** International Journal of Hydrogen Energy

**DOI:** 10.1016/j.ijhydene.2025.03.151

---

## Resumen


Estudio CFD transiente de reactor cilíndrico LaNi5 con aletas internas y chaqueta agua para mejorar transferencia calor durante absorción hidrógeno. Modelo incluye medio poroso, transferencia calor conjugada turbulenta, y zona expansión (19% volumen) para acomodar expansión volumétrica 17% del hidruro. Investiga 4 diseños (0, 5, 10 aletas in-line, 10 aletas staggered), materiales aletas (SS316, cobre), flujos agua (Re=5100-22000), presiones entrada H2 (5-20 bar). Resultados: aletas staggered cobre + Re=5100 reducen tiempo absorción 30%, Re=22000 reducción adicional 27%, presión 20 bar reduce 61% vs 10 bar. Diseño 4 (10 aletas staggered cobre) logra 237.9 W/kg power-to-mass ratio (+55% vs sin aletas), tiempo absorción 602 s para 90% capacidad. Trade-offs: caída presión aumenta 6% (Design 4), masa reactor +4%, pero impactos despreciables comparados con mejora cinética.

---

## Puntos Clave


1. **Modelado avanzado CFD:** Primera aplicación completa transferencia calor conjugada transitoria para MH con turbulencia SST k-ω en chaqueta agua. Modelo acopla simultáneamente transferencia calor en sólidos y fluidos, considerando dependencia local temperatura, concentración H2, presión.

2. **Expansión volumétrica considerada:** Zona expansión 19% volumen total asegura espacio para expansión 17% volumétrica LaNi5 durante absorción, previene deformación reactor. Afecta patrón flujo térmico, aumenta resistencia térmica.

3. **Aletas staggered superiores a in-line:** Diseño 4 (10 aletas staggered) reduce tiempo absorción 3.2% vs Diseño 3 (10 aletas in-line) a pesar mismo número aletas. Configuración escalonada aumenta área superficial efectiva, mejora mixing térmico.

4. **Material aleta crítico:** Aletas cobre (lambda=387.6 W/m*K, ~20* acero) reducen tiempo absorción 38% (Design 1→4) vs 14% con SS316. Reducción promedio 10%, 19%, 25% en Design 2,3,4 con cobre. Efectividad aumenta con área superficial.

5. **Reynolds number impact significativo:** Incremento Re 5100→22000 reduce tiempo absorción 18% (851→699 s Design 1). Mayor velocidad fluido remueve calor más efectivamente que ajustar número aletas. Coeficiente transferencia calor promedio aumenta 20.7%, 34.4%, 18.3% en incrementos sucesivos Re.

6. **Presión entrada no lineal:** Aumento 5→10 bar reduce tiempo 42% (1033→602 s), pero 10→15 bar solo 22%, y 15→20 bar solo 15%. Retornos decrecientes por temperatura lecho elevada que reduce fuerza impulsora (diferencia P_gas - P_eq).

7. **Distribución carga no uniforme:** Capacidad carga mayor en interface zona expansión-lecho y fondo reactor vs centro. Fondo muestra absorción más rápida por zona recirculación en codo 90° chaqueta agua que promueve mixing y transferencia calor.

8. **Power-to-mass ratio optimizado:** Design 4 alcanza 237.9 W/kg (+55% vs Design 1: 153.3 W/kg) a pesar aumento 4% masa reactor. Reducción sustancial tiempo absorción compensa incremento masa, beneficioso para thermal energy storage y heat pumps.

9. **Trade-offs caída presión aceptables:** Design 4 muestra caída presión 372 Pa (+6% vs 350 Pa Design 1), pero representa solo 0.04% presión entrada (10 bar). Impacto en potencia compresión y velocidad reacción despreciable.

10. **Validación modelo robusta:** Temperatura y fracción reacción comparadas con experimentos Jemni et al. y simulaciones Tong et al. Error máximo 2% temperatura, 6% fracción reacción. Curvas PCI LaNi5 concuerdan con experimentos (293K, 313K).

11. **Zona recirculación ventajosa:** Dos codos 90° en chaqueta agua crean zona recirculación lado inferior cilindro. Separación flujo y flujo invertido promueven mixing fluido, mejoran transferencia calor desde pared caliente. Temperatura cerca recirculación menor que parte central inferior.

12. **Streamlines hidrógeno revelan patrones:** A 100 s, H2 converge hacia pared y aletas (menor temperatura). Zona expansión: flujo primario descendente hacia lecho, pero en paredes laterales flujo ascendente por boyancia térmica. A 500 s, gas H2 se mueve hacia interface capacidades alta/baja carga cerca centro reactor.

---

## Características Técnicas


### Hidruro Metálico


#### LaNi5 (Lantano-Níquel)

- **Capacidad almacenamiento:** 1.38 wt% (capacidad máxima alcanzada en simulaciones)

- **Capacidad teórica:** 1.4 wt% (literatura)

- **Reacción:** LaNi5 + 3H2 ↔ LaNi5H6 + 30.8 kJ/mol (exotérmica absorción)

- **Expansión volumétrica:** 17% durante absorción

- **Calor liberado total:** ~183 kJ para ~12 g H2 almacenado

- **Energía activación (E_a):** 21179.6 J/mol

- **Constante velocidad reacción (C_a):** 59.187 s−1

- **Entalpía reacción (dH):** -30800 J/mol (negativa = exotérmica)

- **Entropía reacción (dS):** -108 J/(mol*K)

- **Densidad MH:** 8411 kg/m3

- **Densidad H2 gas:** 2.016 kg/m3 (ley gas ideal)

- **Calor específico MH:** 419 J/(mol*K)

- **Calor específico H2:** 14890 J/(mol*K)

- **Conductividad térmica MH:** 3.18 W/(m*K)

- **Conductividad térmica H2:** 0.1672 W/(m*K)

- **Permeabilidad lecho poroso (K):** 10−8 m2

- **Viscosidad H2:** 8.411 * 10−6 kg/(m*s)

#### Presión Equilibrio (Van't Hoff modificado)

- **Ecuación:** ln(P_eq/P_ref) = (dH/RT) - (dS/R) + (φ_s + φ_0)tan[π(c/c_sat - 1/2 + β/2)]

- **P_ref:** Presión referencia

- **φ_s, φ_0:** Factores plateau flatness

- **β:** Factor hysteresis plateau

- **Validación:** Curvas PCI 293K, 313K concuerdan con experimentos

### Geometría y Diseño


#### Reactor Cilíndrico Base

- **Altura total:** 120 mm

- **Radio exterior (con chaqueta):** 36.5 mm

- **Espesor pared:** 3 mm (todas áreas)

- **Material pared y aletas:** SS316 (acero inoxidable, excepto variante cobre)

- **Diámetro entrada agua:** 10.5 mm

- **Diámetro salida agua:** 5.25 mm

- **Geometría chaqueta:** Dos codos 90°, flujo descendente→fondo→ascendente→salida superior

#### Design 1 (Baseline - Sin Aletas)

- **Volumen expansión:** 45.9 cm3

- **Volumen MH:** 206 cm3

- **Volumen aletas:** 0 cm3

- **Masa MH:** 857 g

- **Área superficial aletas:** 0 cm2

- **Número aletas:** 0

- **Área contacto pared lateral:** 90 mm

#### Design 2 (5 Aletas In-Line)

- **Volumen expansión:** 42.4 cm3

- **Volumen MH:** 207 cm3

- **Volumen aletas:** 2.69 cm3

- **Masa MH:** 861 g

- **Área superficial aletas:** 10.9 cm2

- **Número aletas:** 5

- **Longitud aleta:** 12 mm

- **Espesor aleta:** 0.5 mm

- **Configuración:** In-line (alineadas)

#### Design 3 (10 Aletas In-Line)

- **Volumen expansión:** 39.0 cm3

- **Volumen MH:** 208 cm3

- **Volumen aletas:** 5.37 cm3

- **Masa MH:** 864 g

- **Área superficial aletas:** 21.8 cm2

- **Número aletas:** 10

- **Configuración:** In-line

- **Área contacto pared lateral:** 93 mm (+3.3% vs Design 1)

#### Design 4 (10 Aletas Staggered)

- **Volumen expansión:** 39.0 cm3

- **Volumen MH:** 206 cm3

- **Volumen aletas:** 6.88 cm3

- **Masa MH:** 857 g

- **Área superficial aletas:** 28.0 cm2 (+28% vs Design 3)

- **Número aletas:** 10

- **Configuración:** Staggered (escalonada)

- **Ventaja geométrica:** Mayor área efectiva mismo número aletas

#### Porosity y Expansión

- **Porosidad lecho (ε):** No especificada exactamente, pero modelo aplica equilibrio térmico local

- **Volumen expansión/volumen total:** 19% (previene deformación por expansión 17% volumétrica)

- **Influencia expansión:** Aumenta resistencia térmica, afecta patrón flujo térmico

### Transferencia de Calor


#### Conductividad Térmica Materiales

- **SS316 (acero inoxidable):** 16.3 W/(m*K)

- **Cobre (Cu):** 387.6 W/(m*K) (~23.8* acero)

- **Agua líquida:** 0.6 W/(m*K)

- **MH (LaNi5):** 3.18 W/(m*K)

- **Hidrógeno gas:** 0.1672 W/(m*K)

- **Conductividad efectiva lecho:** lambda_e = ε*lambda_g + (1-ε)*lambda_m

#### Calores Específicos

- **SS316:** 490 J/(mol*K)

- **Agua:** 4182 J/(mol*K)

- **Cobre:** 381 J/(mol*K)

- **MH:** 419 J/(mol*K)

- **H2 gas:** 14890 J/(mol*K)

#### Coeficiente Transferencia Calor (HTC) Pared-Agua

- **Re = 5100:** HTC baseline

- **Re = 7600:** +20.7% vs Re=5100

- **Re = 14000:** +34.4% vs Re=7600 (mayor incremento)

- **Re = 22000:** +18.3% vs Re=14000

- **Relación cuantitativa Re-HTC:** Derivada inversamente de simulaciones (no constante asumida)

#### Transferencia Calor Conjugada

- **Modelo:** Turbulencia SST k-ω para flujo agua chaqueta

- **Acoplamiento:** Simultáneo transferencia calor sólidos (pared, aletas, lecho MH) y fluidos (agua, H2 gas)

- **No-slip:** Condición velocity en pared reactor y chaqueta agua

- **Interface MH-pared:** -lambda_e(∂T_MH/∂n) = -lambda_steel(∂T_w,i/∂n)

- **Interface pared-agua (convección):** -lambda_steel(∂T_w,o/∂n) = h(T_w,o - T_water)

- **Adiabática:** Base y lateral pared exterior chaqueta agua (∂T_water/∂n = 0)

### Condiciones de Operación


#### Condiciones Iniciales

- **Temperatura inicial:** T_initial = T_MH,0 = T_water,0 = 293 K

- **Presión inicial H2:** 1 bar (debe ser >P_eq para absorción)

- **Temperatura entrada H2:** 293 K (constante)

- **Temperatura entrada agua:** 293 K (constante)

#### Presión Entrada Hidrógeno

- **Rampa:** Incremento lineal 0-100 s hasta presión objetivo, luego constante

- **5 bar:** Tiempo absorción 90% = 1033 s

- **10 bar (baseline):** Tiempo = 602 s (reducción 42% vs 5 bar)

- **15 bar:** Tiempo = 470 s (reducción 22% vs 10 bar)

- **20 bar:** Tiempo = 401 s (reducción 15% vs 15 bar)

- **Tendencia:** Retornos decrecientes por temperatura lecho elevada que reduce P_gas - P_eq

#### Reynolds Number Agua (Flujo Turbulento)

- **Re = 5100:** 0.03 kg/s, tiempo absorción 851 s (Design 1), 754 s (Design 4 SS), 577 s (Design 4 Cu)

- **Re = 7600:** 0.05 kg/s, tiempo 793 s (D1), 696 s (D4 SS), 534 s (D4 Cu) → Reducción 7% vs Re=5100

- **Re = 14000:** 0.10 kg/s, tiempo 728 s (D1), 631 s (D4 SS), 485 s (D4 Cu) → Reducción 14% vs Re=5100

- **Re = 22000:** 0.15 kg/s, tiempo 699 s (D1), 602 s (D4 SS), 464 s (D4 Cu) → Reducción 18% vs Re=5100

- **Cálculo Re:** Re = ρuL/μ, donde L = diámetro canal chaqueta agua

- **Límite inferior:** Re ≥5100 para prevenir flujo reverso en salida agua por gravedad

### Rendimiento


#### Tiempo Absorción 90% Capacidad (SS316 Aletas, 10 bar H2)


| Diseño | Re=5100 | Re=7600 | Re=14000 | Re=22000 |
|--------|---------|---------|----------|----------|
| Design 1 (0 aletas) | 851 s | 793 s | 728 s | 699 s |
| Design 2 (5 in-line) | 816 s (-4%) | 757 s | 691 s | 663 s |
| Design 3 (10 in-line) | 777 s (-9%) | 717 s | 651 s | 622 s |
| Design 4 (10 staggered) | 754 s (-11%) | 696 s | 631 s | 602 s (-14%) |

**Reducción vs Design 1:**

- Design 2: -4% (Re=5100)

- Design 3: -9% (Re=5100), -11% (Re=22000)

- Design 4: -11% (Re=5100), -14% (Re=22000)

#### Tiempo Absorción 90% Capacidad (Aletas Cobre, 10 bar H2)


| Diseño | Re=5100 | Re=7600 | Re=14000 | Re=22000 |
|--------|---------|---------|----------|----------|
| Design 1 (0 aletas) | 851 s | 793 s | 728 s | 699 s |
| Design 2 (5 in-line Cu) | 737 s (-13%) | 683 s | 623 s | 596 s |
| Design 3 (10 in-line Cu) | 620 s (-27%) | 571 s | 517 s | 491 s |
| Design 4 (10 staggered Cu) | 527 s (-38%) | 483 s | 433 s | 410 s |

**Reducción aletas cobre vs SS316:**

- Design 2: -10% promedio

- Design 3: -19% promedio

- Design 4: -25% promedio

- **Máxima reducción:** Design 1→4 cobre: -38% (vs -14% SS316)

#### Perfiles Temperatura y Carga


**A t=100 s (fin rampa presión):**

- **Temperatura pico promedio lecho:** ~342-348 K (todos diseños similares)

- **Temperatura máxima:** 348 K en todos casos

- **Temperatura pared y aletas:** Inicio descenso por enfriamiento agua

- **Temperatura agua salida máxima:** 299 K (Re=5100), 295 K (Re=22000)

- **Carga concentrada:** Near pared y aletas (menor temperatura, mayor fuerza impulsora)

**A t=500 s:**

- **Temperatura centro lecho:** Alta aún

- **Temperatura pared/aletas:** Reducida significativamente

- **Temperatura agua:** Variación no claramente visible (pared SS enfriada)

- **Área completamente cargada:** Expande hacia centro lecho

- **Flujo H2:** Hacia interface región alta/baja carga cerca centro reactor

**A t=1000 s:**

- **Temperatura centro lecho:** 339 K (D1), 338 K (D2), 333 K (D3), 330 K (D4)

- **Áreas incompletas:** Permanecen en centro lecho, diferencias entre diseños evidentes

- **Absorción fondo:** Más rápida que centro por zona recirculación

**Temperatura final equilibrio:**

- **Lecho MH:** 293 K (igual temperatura entradas H2 y agua)

#### Caída Presión Lecho MH


| Diseño | Caída Presión [Pa] | Incremento vs Design 1 | % Presión Entrada (10 bar) |
|--------|-------------------|------------------------|----------------------------|
| Design 1 | 350 | 0% | 0.035% |
| Design 2 | 359 | +3% | 0.036% |
| Design 3 | 368 | +5% | 0.037% |
| Design 4 | 372 | +6% | 0.037% |

**Medición:** Interface zona expansión-lecho hasta fondo lecho
**Impacto:** Despreciable en potencia compresión y velocidad reacción

#### Power-to-Mass Ratio (Calor Liberado / Tiempo Absorción / Masa Reactor)


| Diseño | Masa Reactor [kg] | Incremento Masa | P-to-M Ratio [W/kg] | Mejora vs D1 |
|--------|------------------|-----------------|---------------------|--------------|
| Design 1 | Baseline | 0% | 153.3 | 0% |
| Design 2 | +1.6% | +1.6% | 180.3 | +17.6% |
| Design 3 | +3.1% | +3.1% | 216.4 | +41.2% |
| Design 4 | +4.0% | +4.0% | 237.9 | +55.2% |

**Cálculo:** P-to-M = (183 kJ) / (t_absorción) / (m_reactor)
**Significado:** Mayor ratio = más eficiente para thermal energy storage, heat pumps
**Conclusión:** Reducción sustancial tiempo compensa aumento masa

#### Distribución Carga Axial (Línea Central A-A)


**Tendencia general (todos diseños):**

- **Mayor carga:** Interface expansión-lecho y fondo lecho

- **Menor carga:** Centro lecho MH

- **Design 1:** Perfil suave (sin aletas)

- **Designs 2-4:** Picos carga en ubicaciones aletas (menor temperatura local)

**Zona fondo favorecida:**

- Recirculación en codo 90° chaqueta agua

- Separación flujo, flujo invertido promueven mixing

- Transferencia calor más efectiva

- Presión equilibrio reducida → Mayor fuerza impulsora absorción

#### Hydrogen Streamlines (Pathlines)


**t=100 s:**

- **Zona expansión:** Flujo primario descendente hacia lecho

- **Paredes laterales:** Flujo ascendente por boyancia térmica (temperatura alta)

- **Convergencia:** H2 converge hacia pared y aletas (menor temperatura)

**t=500 s:**

- **Flujo pared:** Ya no fluye por pared

- **Flujo central:** Hacia interface capacidad alta/baja cerca centro reactor

- **Influencia aletas:** Notoria en Designs 2-4

**t=1000 s:**

- **Áreas incompletas:** Permanecen centro lecho

- **Diferencias diseño:** Evidentes especialmente por aletas enfriamiento

---

## Transferencia de Calor


### Mecanismos Térmicos Identificados


1. **Reacción exotérmica absorción:**
 - LaNi5 + 3H2 → LaNi5H6 + 30.8 kJ/mol
 - Temperatura pico 342-348 K a 100 s (fin rampa presión)
 - Sin enfriamiento adecuado: Temperatura elevada reduce P_eq, disminuye fuerza impulsora

2. **Resistencia térmica lecho MH:**
 - Conductividad térmica baja (3.18 W/m*K MH, 0.1672 W/m*K H2)
 - Zona expansión añade resistencia térmica adicional
 - Gradientes térmicos significativos centro vs pared (hasta 45-55 K a t=1000 s)

3. **Cooling aletas internas:**
 - Reducen distancia conducción térmica hacia disipador (pared)
 - Aumento área superficial acelera remoción calor
 - Material crítico: Cobre (387.6 W/m*K) vs SS316 (16.3 W/m*K) → Factor 23.8*
 - Efectividad aumenta con área: Design 2 (10.9 cm2) < Design 3 (21.8 cm2) < Design 4 (28.0 cm2)

4. **Configuración aletas staggered:**
 - Design 4 vs Design 3: Mismo número aletas (10), pero staggered aumenta área efectiva 28% (28.0 vs 21.8 cm2)
 - Mejora mixing térmico, reduce zonas muertas
 - Reducción tiempo 3.2% adicional vs in-line

5. **Flujo turbulento chaqueta agua:**
 - Modelo SST k-ω captura dinámica cerca-pared con precisión
 - HTC aumenta no-linealmente con Re: +20.7% (5100→7600), +34.4% (7600→14000), +18.3% (14000→22000)
 - Mayor incremento HTC en rango medio Reynolds
 - Flujo turbulento superior a ajustar número aletas para remoción calor

6. **Zona recirculación ventajosa:**
 - Codos 90° chaqueta agua crean recirculación lado inferior cilindro
 - Separación flujo y flujo invertido promueven mixing fluido
 - Transferencia calor mejorada en fondo reactor
 - Resulta en absorción más rápida zona fondo vs centro

### Transferencia Calor Conjugada


**Interface MH-Pared:**
```
-lambda_e(∂T_MH/∂n) = -lambda_steel(∂T_w,i/∂n)
```

- lambda_e = ε*lambda_g + (1-ε)*lambda_m (conductividad efectiva lecho)

- Acoplamiento directo flujo calor entre lecho poroso y pared sólida

**Interface Pared-Agua (Convección):**
```
-lambda_steel(∂T_w,o/∂n) = h(T_w,o - T_water)
```

- h = HTC (derivado inversamente, no asumido constante)

- Depende localmente de Re, temperatura, geometría

**Pared Externa Chaqueta:**
```
∂T_water/∂n = 0 (adiabática)
```

- Base y lateral chaqueta agua sin pérdidas calor externas

- Todo calor generado MH debe ser removido por agua

### Cinética Acoplada a Temperatura


**Velocidad absorción:**
```
S_m = C_a*exp(-E_a/RT)*ρ_m(ρ_m,sat - ρ_m)*ln(P_g/P_eq)
```

- Dependencia exponencial temperatura (Arrhenius): exp(-21179.6/RT)

- Fuerza impulsora: ln(P_g/P_eq) → Mayor diferencia presiones = Mayor velocidad

- Temperatura elevada aumenta P_eq → Reduce fuerza impulsora

- Trade-off: Presión alta acelera inicialmente, pero eleva temperatura lecho

**Presión equilibrio:**
```
ln(P_eq/P_ref) = (dH/RT) - (dS/R) + (φ_s + φ_0)*tan[π(c/c_sat - 1/2 + β/2)]
```

- Aumenta con temperatura (endotérmica desorción, exotérmica absorción)

- Término plateau: (φ_s + φ_0)*tan(...) captura comportamiento complejo PCI

- Factor hysteresis β, flatness φ_s, φ_0 ajustados a experimentos

### Impacto Temperatura en Distribución Carga


**Regiones baja temperatura (pared, aletas):**

- P_eq menor → Mayor diferencia P_g - P_eq

- Velocidad absorción aumentada localmente

- Carga H2 concentrada estas zonas (100-500 s)

**Regiones alta temperatura (centro lecho):**

- P_eq elevada → Menor fuerza impulsora

- Absorción retardada, zonas incompletas persisten (hasta 1000 s)

- Gradiente térmico centro-pared determina uniformidad carga

**Zona fondo privilegiada:**

- Recirculación mejora transferencia calor

- Temperatura local reducida vs centro

- Absorción completa más rápida

---

## Importancia de la Gestión Térmica para Diseño Modular


### Desafíos Térmicos Fundamentales en MH Storage


1. **Naturaleza exotérmica absorción:**
 - Liberación 30.8 kJ/mol H2 para LaNi5
 - Sin enfriamiento: Temperatura lecho aumenta 40-55 K (293→342-348 K en 100 s)
 - Temperatura elevada aumenta P_eq, reduce fuerza impulsora (P_g - P_eq)
 - Resultado: Cinética absorción severamente ralentizada o detenida

2. **Conductividad térmica limitada:**
 - MH (LaNi5): 3.18 W/m*K (bajo comparado con metales ~50-400 W/m*K)
 - H2 gas en poros: 0.1672 W/m*K (muy bajo)
 - Conductividad efectiva lecho: lambda_e = ε*lambda_g + (1-ε)*lambda_m → Dominada por componente más bajo
 - Consecuencia: Gradientes térmicos severos en geometrías grandes (45-55 K centro-pared a 1000 s)

3. **Zona expansión como resistencia térmica adicional:**
 - 19% volumen total necesario para expansión 17% volumétrica MH
 - Espacio lleno H2 gas (lambda=0.1672 W/m*K) actúa como aislante
 - Aumenta resistencia térmica total sistema
 - Afecta patrones flujo térmico y convección natural

4. **Acoplamiento cinética-térmica:**
 - Velocidad reacción proporcional a exp(-E_a/RT)*ln(P_g/P_eq)
 - P_eq depende exponencialmente temperatura: exp(dH/RT)
 - Feedback positivo negativo: Absorción → Calor → T↑ → P_eq↑ → Fuerza impulsora↓ → Absorción↓
 - Necesidad imperativa remover calor continuamente para mantener cinética

### Estrategias Térmicas en Diseño Reactor


1. **Aletas internas como extensores térmicos:**
 - Función: Reducir distancia conducción térmica desde centro lecho hacia pared enfriada
 - Efectividad proporcional a área superficial: 10.9 cm2 (D2) < 21.8 cm2 (D3) < 28.0 cm2 (D4)
 - Material crítico: Cobre (lambda=387.6 W/m*K) reduce tiempo 38% vs sin aletas, acero solo 14%
 - Configuración staggered superior: +3.2% mejora vs in-line por mayor área efectiva y mixing

2. **Chaqueta agua con flujo turbulento:**
 - Turbulencia (Re ≥5100) mejora HTC pared-agua significativamente vs laminar
 - HTC aumenta no-linealmente con Re: Mayor ganancia en rango medio (7600→14000)
 - Codos 90° crean zona recirculación beneficial: Mixing mejorado, absorción fondo más rápida
 - Flujo turbulento más efectivo que aumentar número aletas para remoción calor global

3. **Transferencia calor conjugada:**
 - Acoplamiento simultáneo sólidos (pared, aletas, lecho) y fluidos (agua, H2)
 - Permite representación realista dependencia local temperatura, concentración, presión
 - HTC derivado inversamente de simulación (no constante asumida) → Mayor precisión
 - Modelo SST k-ω captura dinámica cerca-pared crucial para predicción térmica

4. **Optimización multi-parámetro:**
 - Número aletas: 0→5→10 reduce tiempo, pero retornos decrecientes (incrementos -4%, -5%, -2% adicional)
 - Material aletas: Cobre vs acero → Factor 1.5-2* mejora tiempo
 - Re agua: Incremento 5100→22000 reduce tiempo 18%, pero costo energético bombeo aumenta
 - Presión H2: 5→10 bar crítico (−42% tiempo), aumentos posteriores retornos decrecientes

### Implicaciones para Modularidad


1. **Escalabilidad térmica NO lineal:**
 - Reactor cilíndrico 120 mm altura, 73 mm diámetro (con chaqueta) muestra gradientes 45-55 K centro-pared
 - Duplicar dimensiones lineales → Cuadruplica volumen pero solo duplica área superficial (ratio área/volumen disminuye)
 - Distancias conducción térmica aumentan → Gradientes térmicos escalan no-linealmente
 - **Conclusión crítica:** Reactores grandes monolíticos INVIABLES sin gestión térmica avanzada

2. **Ventaja módulos pequeños:**
 - Ratio área/volumen mayor en geometrías pequeñas
 - Distancias conducción reducidas (<60 mm en diseños estudiados)
 - Tiempos respuesta térmica más rápidos (pico temperatura a 100 s, descenso significativo a 500 s)
 - Temperatura más uniforme dentro cada módulo (gradientes <50 K vs potencialmente >100 K en escala grande)

3. **Gestión térmica individual por módulo:**
 - Cada módulo con chaqueta agua dedicada
 - Control independiente Re agua según carga térmica local
 - Adaptación a posición en sistema (primer módulo mayor carga térmica por H2 fresco, últimos módulos menor)
 - Sensores temperatura distribuidos (múltiples puntos) vs pocos sensores en reactor grande

4. **Redundancia térmica:**
 - Fallo enfriamiento en un módulo → Aislamiento térmico ese módulo, resto opera
 - Distribución carga térmica entre múltiples chaquetas agua
 - Menor riesgo runaway térmico (temperatura fuera control)
 - Mantenimiento sistema enfriamiento sin parada completa

5. **Optimización geométrica modular:**
 - Configuración aletas (in-line vs staggered) ajustable por módulo según necesidad
 - Material aletas seleccionable (cobre para módulos críticos, acero para secundarios) → Trade-off costo/desempeño
 - Geometría reactor (altura, diámetro, número aletas) optimizable independientemente
 - Posibilidad reactores diferentes en serie/paralelo según etapa proceso

6. **Integración térmica sistema completo:**
 - Calor absorción módulo N puede precalentar agua enfriamiento módulo N+1 (si aplicable)
 - Cascada térmica: Temperatura salida agua módulo anterior = Entrada siguiente (control fino)
 - Recuperación calor residual para aplicaciones externas (calefacción, heat pumps)
 - Power-to-mass ratio optimizado: 237.9 W/kg (D4) beneficia thermal energy storage modular

### Casos de Estudio Relevantes del Artículo


**Diseño Modular Implícito:**

- Aunque no explícitamente multi-reactor, geometría estudiada (120 mm * 73 mm, ~860 g MH) representa **módulo unitario óptimo**

- Capacidad ~12 g H2 por módulo → Escalado a kg/ton H2 mediante réplica módulos

- Design 4 (10 aletas staggered Cu, Re=22000): **Tiempo 602 s para 90% carga** = **Benchmark modular**

- Power-to-mass 237.9 W/kg → Eficiencia térmica superior para integración modular

**Comparación Escala:**
| Parámetro | Módulo Unitario | Sistema 10 Módulos (Estimado) | Sistema 100 Módulos (Estimado) |
|-----------|----------------|------------------------------|-------------------------------|
| Masa MH | 0.86 kg | 8.6 kg | 86 kg |
| Capacidad H2 | ~12 g | ~120 g | ~1.2 kg |
| Tiempo 90% | 602 s | 602 s (paralelo) | 602 s (paralelo) |
| Calor total | 183 kJ | 1830 kJ | 18300 kJ |
| P-to-M ratio | 237.9 W/kg | ~237.9 W/kg | ~237.9 W/kg |

**Escalabilidad lineal térmica preservada:**

- Configuración paralelo mantiene tiempos absorción (cada módulo independiente térmicamente)

- Power-to-mass ratio preservado (vs degradación en reactor monolítico grande)

- Gestión térmica no se complica exponencialmente (vs sistemas grandes)

### Lecciones Térmicas para Diseño Modular Escalable


1. **Criterio dimensional módulo:**
 - Distancia máxima centro-pared: <40-50 mm (basado en gradientes 45-55 K observados)
 - Altura módulo: <150 mm (basado en 120 mm estudio, margen zona expansión)
 - Ratio área/volumen: >0.3-0.4 m−1 (estimado de geometrías exitosas)

2. **Especificaciones aletas internas:**
 - Mínimo 5 aletas para mejora térmica notoria (-4% tiempo)
 - Óptimo 10 aletas staggered (-11% tiempo SS, -38% Cu)
 - Material cobre crítico si costo permite (factor 1.5-2* mejora)
 - Longitud aleta ~10-20% radio reactor, espesor 0.5-1 mm

3. **Sistema enfriamiento requerido:**
 - Flujo turbulento: Re ≥5100 (previene flujo reverso, mejora HTC)
 - Rango óptimo Re: 14000-22000 (balance mejora HTC vs costo bombeo)
 - Geometría chaqueta: Codos/bends beneficiosos para recirculación (mejora mixing)
 - Temperatura agua entrada: <30degC (idealmente 20degC = 293 K para máxima fuerza impulsora)

4. **Condiciones operación presión:**
 - Presión mínima efectiva: 10 bar (balance fuerza impulsora vs carga térmica)
 - Presión >15-20 bar: Retornos decrecientes (temperatura lecho limita beneficio)
 - Rampa presión gradual (100 s en estudio) vs step change (reduce choque térmico)

5. **Monitoreo y control:**
 - Sensores temperatura: Mínimo 3 posiciones (entrada/centro/salida lecho) por módulo
 - Sensor presión lecho: Seguimiento P_g y estimación P_eq via temperatura
 - Control Re agua: Modulación según temperatura lecho (PID o MPC)
 - Detección fallo: Temperatura >360 K → Alerta, >380 K → Parada módulo

---

## Relevancia para Diseño Modular Escalable


### Principios Diseño Modular Extrapolables


1. **Módulo unitario óptimo identificado:**
 - **Geometría:** Cilindro 120 mm altura, ~36.5 mm radio exterior (con chaqueta)
 - **Capacidad:** ~860 g LaNi5, ~12 g H2 (1.38 wt%)
 - **Diseño térmico:** 10 aletas staggered cobre, chaqueta agua turbulenta Re=14000-22000
 - **Rendimiento:** 602 s para 90% carga (10 bar, 293 K), 237.9 W/kg power-to-mass
 - **Escalado:** N módulos en paralelo → N*12 g H2, tiempo constante 602 s

2. **Configuración sistema modular:**
 - **Paralelo puro:** N módulos idénticos, carga simultánea, tiempo=602 s, capacidad=N*12 g
 - **Serie-paralelo híbrido:** M líneas paralelas * K módulos serie cada una (Ej: 4*3 = 12 módulos, 144 g H2)
 - **Serie pura:** Desventajoso para absorción (H2 se carga completamente en primer módulo), útil para desorción escalonada

3. **Integración térmica multi-módulo:**
 - **Circuito agua independiente por módulo:** Control individual Re, temperatura entrada
 - **Circuito agua común serie:** Salida módulo N → Entrada módulo N+1 (precalentamiento, si beneficia desorción posterior)
 - **Recuperación calor centralizada:** Todas salidas agua → Intercambiador calor → Aplicación externa (calefacción, agua caliente)
 - **Estimación calor recuperable:** 183 kJ/módulo * N módulos * (T_salida_agua - T_entrada) / tiempo → Potencia térmica disponible

4. **Manufactura y ensamblaje:**
 - **Componentes estandarizados:** Cilindro SS316 3 mm, aletas cobre 0.5 mm * 12 mm, fittings agua 10.5 mm entrada / 5.25 mm salida
 - **Ensamblaje modular:** Cada módulo pre-ensamblado, pre-cargado MH, pre-testeado → Plug-and-play en sistema final
 - **Reemplazo unitario:** Fallo módulo → Aislamiento válvulas, extracción módulo, inserción reemplazo (sin desmontar sistema completo)
 - **Escalado producción:** Módulos idénticos → Producción serie, reducción costo unitario

### Aplicaciones Específicas Diseño Modular


1. **Estacionario residencial/comercial (kW-class):**
 - **Capacidad objetivo:** 1-10 kg H2 → 84-840 módulos (impracticable) → **Mejor escala a módulos mayores 100-500 g H2**
 - **Configuración sugerida:** 10-20 módulos escalados (50-100 g H2 cada uno), paralelo
 - **Gestión térmica:** Circuitos agua individuales, recuperación calor para calefacción espacios
 - **Ventaja modular:** Redundancia (fallo módulo no crítico), mantenimiento rotativo, expansión gradual capacidad

2. **Vehículos pesados (buses, camiones):**
 - **Capacidad objetivo:** 20-50 kg H2 → 1667-4167 módulos 12 g (impracticable) → **Requiere módulos 500-1000 g H2**
 - **Diseño sugerido:** Mantener ratio área/volumen, escalar a cilindros ~200-250 mm altura, 60-80 mm diámetro
 - **Configuración:** 40-100 módulos escalados, paralelo, distribuidos en chasis vehículo
 - **Gestión térmica:** Circuito refrigerante vehículo integrado (motor, AC), control térmico distribuido
 - **Ventaja modular:** Distribución peso equilibrada, menor riesgo single-point failure, packaging flexible

3. **Thermal energy storage (MW-class):**
 - **Capacidad objetivo:** 100-1000 kg H2 → 8333-83333 módulos 12 g (impracticable) → **Escala a módulos 5-10 kg H2**
 - **Diseño sugerido:** Reactores ~500-800 mm altura, 200-300 mm diámetro, aletas cobre múltiples, chaqueta agua turbulenta
 - **Configuración:** 20-200 módulos escalados, paralelo con sub-grupos serie para recuperación calor escalonada
 - **Gestión térmica:** Cascada térmica (calor módulo N → Entrada agua módulo N+1), recuperación centralizada para grid/procesos
 - **Ventaja modular:** Power-to-mass optimizado (237.9 W/kg), operación parcial según demanda, integración renovables

4. **Aerospace/portátil (g-kg H2):**
 - **Capacidad objetivo:** 10-1000 g H2 → 1-84 módulos 12 g (viable escala laboratorio) o módulos escalados 50-200 g H2
 - **Diseño sugerido:** Módulos miniaturizados, aletas cobre, enfriamiento pasivo (aletas externas) o activo (micro-ventiladores)
 - **Configuración:** 2-20 módulos, paralelo, peso mínimo crítico
 - **Gestión térmica:** Trade-off entre enfriamiento activo (peso, energía) vs pasivo (menor desempeño, sin consumo)
 - **Ventaja modular:** Cartuchos intercambiables, redundancia en misiones críticas, packaging compacto

### Métricas Clave Diseño Modular (Extrapoladas del Estudio)


| Parámetro | Módulo Lab (12 g H2) | Módulo Pequeño (100 g H2) | Módulo Medio (500 g H2) | Módulo Grande (5 kg H2) |
|-----------|----------------------|--------------------------|------------------------|------------------------|
| Dimensiones (h*d) | 120*73 mm | 200*120 mm | 350*200 mm | 700*400 mm |
| Masa MH | 0.86 kg | 7.2 kg | 36 kg | 360 kg |
| Número aletas | 10 staggered | 15-20 staggered | 30-40 staggered | 60-80 staggered |
| Área aletas (Cu) | 28 cm2 | 180 cm2 | 900 cm2 | 7200 cm2 |
| Re agua | 14000-22000 | 10000-20000 | 8000-15000 | 5000-12000 |
| Tiempo 90% (est.) | 602 s | 800-1000 s | 1200-1500 s | 1800-2400 s |
| P-to-M ratio (est.) | 237.9 W/kg | 200-220 W/kg | 180-200 W/kg | 150-180 W/kg |
| Masa reactor total | ~4 kg | ~25 kg | ~100 kg | ~900 kg |

**Tendencias escalado:**

- Tiempo absorción aumenta NO linealmente (factor ~1.3-1.5 por cada 5* capacidad)

- Power-to-mass ratio disminuye con escala (ratio área/volumen decrece)

- Número aletas escala linealmente con área superficial interna

- Re agua puede reducirse en módulos grandes (mayor volumen agua, mayor tiempo contacto)

### Trade-Offs Críticos Diseño Modular


1. **Número módulos vs Tamaño módulo:**
 - **Muchos módulos pequeños:** Mayor redundancia, mejor ratio área/volumen, complejidad sistema aumenta (válvulas, sensores, control)
 - **Pocos módulos grandes:** Simplicidad sistema, menor costo infraestructura, peor térmica, mayor riesgo single-point failure
 - **Óptimo:** Balancear según aplicación (estacionario→menos grandes, transporte→muchos medianos)

2. **Material aletas (Cobre vs Acero):**
 - **Cobre:** Reducción tiempo 1.5-2*, costo 3-5* mayor que acero, densidad 8960 kg/m3 vs 7990 kg/m3 acero
 - **Acero:** Menor desempeño térmico, costo bajo, resistencia mecánica superior, más fácil manufactura/soldadura
 - **Óptimo:** Cobre para aplicaciones críticas desempeño (vehículos, aerospace), acero para estacionario costo-sensitivo

3. **Flujo agua (Re):**
 - **Re alto (22000):** Mejor HTC, menor tiempo absorción, mayor potencia bombeo, ruido/vibración aumenta
 - **Re bajo (5100):** Menor consumo energético bombeo, HTC reducida, tiempo absorción +22% vs Re=22000
 - **Óptimo:** Re=14000 (balance mejora HTC vs costo bombeo), ajustable según fase (absorción rápida vs desorción lenta)

4. **Presión operación:**
 - **Presión alta (20 bar):** Absorción muy rápida inicialmente (−61% vs 10 bar), temperatura lecho elevada limita beneficio, costo compresor/tankage aumenta
 - **Presión baja (5 bar):** Cinética lenta (+ 72% tiempo vs 10 bar), menor estrés mecánico, menor costo infraestructura
 - **Óptimo:** 10-15 bar (balance cinética vs carga térmica vs costo)

5. **Configuración módulos (Serie vs Paralelo):**
 - **Paralelo:** Tiempo constante (todos cargan simultáneamente), mayor flujo H2 total requerido, control simple
 - **Serie:** H2 carga secuencialmente (primer módulo rápido, últimos lentos), menor flujo H2 requerido, control complejo
 - **Híbrido:** M líneas paralelo * K módulos serie (Ej: 4*3) → Balance flujo H2 vs tiempo total vs control

---

## Conclusiones


1. **Modelo CFD avanzado establece nuevo estándar:** Primera aplicación completa transferencia calor conjugada transitoria con turbulencia SST k-ω para flujo HTF en reactor MH. Acopla simultáneamente transferencia calor sólidos (pared, aletas, lecho) y fluidos (agua, H2), considerando dependencia local T, concentración, presión. Validación robusta (error <2% T, <6% fracción reacción) vs experimentos y literatura.

2. **Aletas internas críticas para gestión térmica:** Incremento área superficial 0→28 cm2 (Design 1→4) reduce tiempo absorción 11-38% según material. Configuración staggered superior (+3.2% vs in-line) por mayor área efectiva. Material aleta determinante: Cobre (lambda=387.6 W/m*K) logra 38% reducción vs acero inoxidable 14%, factor mejora 1.5-2*.

3. **Reynolds number más efectivo que número aletas:** Aumento Re 5100→22000 reduce tiempo 18% (mayor que Design 1→3 con SS aletas: 9%). HTC aumenta no-linealmente: +20.7%, +34.4%, +18.3% en incrementos sucesivos, con mayor ganancia en rango medio (7600→14000). Flujo turbulento remueve calor más efectivamente que ajustar geometría aletas.

4. **Presión entrada H2 presenta retornos decrecientes:** 5→10 bar reduce tiempo 42% (efecto dramático), pero 10→15 bar solo 22%, y 15→20 bar solo 15%. Temperatura lecho elevada con presiones altas (348 K) aumenta P_eq, reduce fuerza impulsora (P_g - P_eq), limita beneficio presiones >15 bar.

5. **Zona recirculación beneficia uniformidad carga:** Codos 90° chaqueta agua crean zona recirculación lado inferior cilindro. Separación flujo y flujo invertido promueven mixing, mejoran transferencia calor. Resultado: Absorción fondo reactor más rápida que centro (temperatura local reducida, P_eq menor, mayor fuerza impulsora).

6. **Zona expansión 19% volumen es resistencia térmica significativa:** Espacio necesario para expansión volumétrica 17% LaNi5 lleno H2 gas (lambda=0.1672 W/m*K) actúa como aislante térmico. Aumenta resistencia térmica total, afecta patrones flujo térmico y convección natural. Gradientes térmicos centro-pared 45-55 K a 1000 s demuestran impacto.

7. **Power-to-mass ratio optimizado con aletas:** Design 4 alcanza 237.9 W/kg (+55% vs Design 1: 153.3 W/kg) a pesar aumento 4% masa reactor. Reducción sustancial tiempo absorción (602 s vs 851 s) compensa incremento masa. Beneficia aplicaciones thermal energy storage y heat pumps.

8. **Trade-offs caída presión y masa aceptables:** Design 4 caída presión +6% (372 Pa vs 350 Pa), representa solo 0.04% presión entrada 10 bar. Impacto en potencia compresión y cinética reacción despreciable. Aumento masa reactor 4% largamente compensado por mejora desempeño.

9. **Distribución carga no uniforme revela limitaciones térmicas:** Carga mayor en interface expansión-lecho y fondo reactor, menor en centro. Gradientes temperatura determinan distribución: Zonas baja T (pared, aletas) cargan primero, centro alta T permanece incompleto hasta 1000 s. Aletas reducen pero no eliminan gradientes.

10. **Modelado acoplamiento cinética-térmica esencial:** Velocidad absorción S_m ∝ exp(-E_a/RT)*ln(P_g/P_eq) muestra feedback temperatura-presión equilibrio-fuerza impulsora. Absorción → Calor → T↑ → P_eq↑ → (P_g - P_eq)↓ → Absorción↓. Gestión térmica continua imperativa para mantener cinética.

11. **Diseño óptimo identificado (Design 4 con Cu):**
 - **Geometría:** 10 aletas staggered cobre, cilindro 120 mm * 36.5 mm radio exterior
 - **Operación:** Re agua 14000-22000 (balance HTC vs bombeo), presión H2 10-15 bar (balance cinética vs térmica)
 - **Rendimiento:** 602 s para 90% carga (10 bar, Re=22000, SS aletas), 410-464 s (aletas Cu)
 - **Aplicabilidad:** Módulo unitario óptimo para escalado sistema modular

12. **Implicaciones modularidad desde perspectiva térmica:**
 - **Escalabilidad NO lineal:** Reactor estudiado (120 mm * 73 mm) muestra gradientes 45-55 K. Duplicar dimensiones → 4* volumen, 2* área, ratio área/volumen disminuye → Gradientes escalan no-linealmente, reactores grandes monolíticos INVIABLES sin gestión térmica avanzada.
 - **Ventaja módulos pequeños:** Mayor ratio área/volumen, distancias conducción reducidas (<60 mm), tiempos respuesta rápidos, temperatura uniforme (gradientes <50 K vs >100 K en escala grande).
 - **Gestión térmica individual:** Cada módulo con chaqueta dedicada, control Re independiente, adaptación posición sistema, sensores distribuidos, redundancia térmica (fallo módulo aislado).
 - **Módulo unitario 12 g H2:** Escalado lineal N módulos paralelo → N*12 g H2, tiempo constante 602 s, power-to-mass preservado 237.9 W/kg (vs degradación reactor monolítico).

13. **Direcciones futuras investigación:**
 - Optimización geometría aletas (forma, thickness gradient, materiales compuestos metal-carbono)
 - Flujo HTF pulsante vs constante (mejora mixing, reduce consumo bombeo)
 - Integración phase change materials (PCMs) en aletas para buffering térmico
 - Control adaptativo Re agua basado en temperatura lecho real-time (PID, MPC)
 - Escalado experimental módulos 100-500 g H2 validando modelos CFD
 - Configuraciones multi-módulo (serie-paralelo) con recuperación calor cascada

---

## Referencias Clave


- Jemni et al.: Experimentos validación temperatura y fracción reacción LaNi5

- Tong et al.: Comparación diseños intercambiadores calor (straight, coiled-tube), reducción 34-73% tiempo

- Prasad & Muthukumar: Outer cooling channel + internal fins, mejora 51.8% tiempo absorción

- MacDonald & Rowe: External fins reducen resistencia térmica, mejoran desorción

- Askri et al.: Comparación internal vs external fins absorción

- Chung et al.: Heat pipe central con external fins, reducción 50% tiempo

- Chibani et al.: External fins + PCM para large-scale storage

- Bai et al.: Longitudinal tree-shaped fin design, 21% reducción absorción vs radial fins

- ANSYS Fluent 2022R1: Software CFD, UDF para source terms masa/energía
