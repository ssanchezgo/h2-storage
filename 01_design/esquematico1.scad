// ==========================================================
// ESQUEMÁTICO DE MÓDULO DE REACTOR DE HIDRURO METÁLICO (MHR)
// Restricción de Volumen Máximo: 145mm x 250mm
// ==========================================================

// --- 1. DEFINICIÓN DE DIMENSIONES (en mm) ---
// Dimensiones de la Placa Base
PLACA_ANCHO = 135;  // Ancho (X)
PLACA_ALTO = 240;   // Alto (Y)
PLACA_ESP = 5;      // Espesor (Z)

// Dimensiones de los Reactores (Celdas)
D_REACTOR = 12;     // Diámetro
L_REACTOR = 120;    // Longitud del cilindro

// Espaciado de la Matriz (3 columnas x 4 filas)
COLS = 3;
ROWS = 4;
H_ESPACIO = 42;    // Espaciado Horizontal (H)
V_ESPACIO = 50.67; // Espaciado Vertical (V)

// Márgenes y Desplazamientos
// Calculamos el punto de inicio para centrar la matriz 3x4
INICIO_X = PLACA_ANCHO/2 - (COLS - 1) * H_ESPACIO / 2;
INICIO_Y = PLACA_ALTO/2 - (ROWS - 1) * V_ESPACIO / 2;
MANIFOLD_ESP = 20; // Espacio para el colector y las válvulas

// --- 2. MÓDULOS DE COMPONENTES ---

// Módulo para un Reactor (Cilindro + Tapa frontal simplificada)
module reactor_cell() {
    color([0.3, 0.3, 0.3, 1]) // Color gris oscuro para el reactor
    cylinder(h = L_REACTOR, r = D_REACTOR/2, center = false);
    
    // Simplificación de la Válvula/Conexión de Flujo
    translate([0, 0, L_REACTOR])
    color([0.6, 0.6, 0.6, 1]) // Color gris claro para la válvula
    cube([10, 10, MANIFOLD_ESP], center = true);

    // Detalle simplificado de la palanca de la válvula
    translate([0, 0, L_REACTOR + MANIFOLD_ESP/2 + 2.5])
    color([0.8, 0.1, 0.1, 1]) // Color rojo para la palanca
    cube([3, 15, 2], center = true);
}

// --- 3. ENSAMBLAJE PRINCIPAL ---

// 1. Placa Base de Montaje
color([0.4, 0.4, 0.4, 0.8]) // Placa translúcida
cube([PLACA_ANCHO, PLACA_ALTO, PLACA_ESP]);

// 2. Agujeros en la Placa (Sustracción)
for (c = [0 : COLS-1]) {
    for (r = [0 : ROWS-1]) {
        translate([
            INICIO_X + c * H_ESPACIO,
            INICIO_Y + r * V_ESPACIO,
            -0.01 // Pequeño desplazamiento para asegurar el corte
        ]) {
            difference() {
                // Cilindro para perforar el agujero
                cylinder(h = PLACA_ESP + 0.02, r = D_REACTOR/2 + 0.5, center = false); // Agujero ligeramente más grande
            }
        }
    }
}

// 3. Montaje de la Matriz de Reactores (3x4)
translate([0, 0, PLACA_ESP]) // Empezamos después de la placa
for (c = [0 : COLS-1]) { // Columnas (X)
    for (r = [0 : ROWS-1]) { // Filas (Y)
        translate([
            INICIO_X + c * H_ESPACIO,
            INICIO_Y + r * V_ESPACIO,
            0
        ])
        reactor_cell();
    }
}

// 4. Colector Principal (Manifold) - Simplificación
// Tubería que conecta el extremo de las válvulas
translate([PLACA_ANCHO/2, PLACA_ALTO/2, PLACA_ESP + L_REACTOR + MANIFOLD_ESP/2]) {
    color([0.5, 0.5, 0.5, 0.9])
    
    // Tubería de Conexión Horizontal (simplificada)
    cube([(COLS - 1) * H_ESPACIO + D_REACTOR, 5, 5], center=true);

    // Tubería de Conexión Vertical (simplificada)
    cube([5, (ROWS - 1) * V_ESPACIO + D_REACTOR, 5], center=true);
}