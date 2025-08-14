// --- PARAMETROS GLOBALES DEL TANQUE ---
TANK_VOLUME_LITERS = 1;
TANK_INNER_DIAMETER = 60; // Diametro interno del tanque en mm (para 1 litro)
TANK_INNER_RADIUS = TANK_INNER_DIAMETER / 2;

// Calculamos la longitud cilíndrica necesaria para el volumen,
// asumiendo cúpulas semiesféricas.
// Volumen total = Volumen cilindro + Volumen esfera
// 1000 cm^3 = pi * (R^2) * L_cilindrica + (4/3) * pi * R^3
// Despejando L_cilindrica:
// L_cilindrica = (V_total - (4/3) * pi * R^3) / (PI * pow(TANK_INNER_RADIUS, 2));
TANK_CYLINDRICAL_LENGTH = (TANK_VOLUME_LITERS * 1000000 - (4/3) * PI * pow(TANK_INNER_RADIUS, 3)) / (PI * pow(TANK_INNER_RADIUS, 2));

// Espesor nominal de la pared para la visualizacion.
// Esto representa el espesor TOTAL (liner + compuesto)
TANK_WALL_THICKNESS = 9; // mm (basado en nuestro analisis inicial ~7.25-9.25mm)

// --- PARAMETROS PARA EL AGUJERO DE LA BOQUILLA (NECESARIOS AUNQUE LA BOQUILLA NO ESTÉ PRESENTE) ---
// Estos se usan para definir el tamaño y la ubicación del agujero que la boquilla ocuparía.
NOZZLE_OUTER_DIAMETER_FOR_HOLE = 15; // Diámetro del agujero para la boquilla
NOZZLE_TOTAL_LENGTH_FOR_HOLE = 30;   // Longitud de la boquilla, para profundidad del agujero

// --- MODULO DE LA FORMA EXTERNA SOLIDA DEL TANQUE ---
// Este módulo crea la geometría externa del tanque antes de hacer el interior hueco.
module solid_tank_shape(outer_diameter, cylindrical_length) {
    union() {
        // Cuerpo cilíndrico principal
        cylinder(h = cylindrical_length, d = outer_diameter, $fn = 60, center = true);

        // Cúpula superior
        translate([0, 0, cylindrical_length/2]) {
            sphere(r = outer_diameter / 2, $fn = 60);
        }
        // Cúpula inferior
        translate([0, 0, -cylindrical_length/2]) {
            sphere(r = outer_diameter / 2, $fn = 60);
        }
    }
}

// --- MODULO DEL TANQUE DE HIDROGENO ---
// Este módulo construye el tanque completo, con pared y agujero para boquilla.
module hydrogen_tank_only(
    inner_diameter,
    cylindrical_length,
    wall_thickness,
    hole_diameter, // Agujero para la boquilla
    hole_depth   // Profundidad del agujero para la boquilla
) {
    outer_diameter = inner_diameter + 2 * wall_thickness;
    inner_radius = inner_diameter / 2;

    // Creamos el tanque hueco sustrayendo el volumen interno y el agujero de la boquilla
    difference() {
        color("darkgray") {
            // Llamamos al módulo solid_tank_shape para la forma exterior
            solid_tank_shape(outer_diameter, cylindrical_length);
        }

        // Sustraemos el volumen interno para crear el espesor de pared
        union() {
            // Volumen cilíndrico interno
            cylinder(h = cylindrical_length, d = inner_diameter, $fn = 60, center = true);

            // Volumen de la cúpula superior interna
            translate([0, 0, cylindrical_length/2]) {
                sphere(r = inner_radius, $fn = 60);
            }
            // Volumen de la cúpula inferior interna
            translate([0, 0, -cylindrical_length/2]) {
                sphere(r = inner_radius, $fn = 60);
            }
        }

        // Cortamos el agujero para la boquilla
        // Este agujero se ubicará en la cúpula inferior del tanque
        translate([0, 0, -(cylindrical_length/2 + wall_thickness)]) {
            // Cortamos el agujero un poco más profundo para asegurar un corte limpio
            cylinder(h = hole_depth + 2, d = hole_diameter + 1, center = true, $fn = 60);
        }
    }
}

// --- LLAMADA AL MODULO PRINCIPAL DEL TANQUE (SOLO EL TANQUE) ---
hydrogen_tank_only(
    TANK_INNER_DIAMETER,
    TANK_CYLINDRICAL_LENGTH,
    TANK_WALL_THICKNESS,
    NOZZLE_OUTER_DIAMETER_FOR_HOLE, // Usamos el diámetro para el agujero
    NOZZLE_TOTAL_LENGTH_FOR_HOLE   // Usamos la longitud para la profundidad del agujero
);