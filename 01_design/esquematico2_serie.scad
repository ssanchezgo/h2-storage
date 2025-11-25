// --- 1. PARÁMETROS GENERALES DE DIMENSIÓN ---
diametro_exterior = 60;
radio_exterior = diametro_exterior / 2; // 30 mm
grosor_pared = 5;
radio_interior = radio_exterior - grosor_pared; // 25 mm

// --- PARÁMETROS DEL REACTOR TIPO CÁPSULA (Ambos extremos redondeados) ---
longitud_cilindro_recto = 120; // Altura de la sección recta del cilindro
// Altura total del reactor (de punta a punta): longitud_cilindro_recto + diametro_exterior
altura_total_capsula = longitud_cilindro_recto + diametro_exterior; 

// --- PARÁMETROS DEL ARREGLO EN PARALELO ---
Num_Reactores = 5;
Separacion_Reactores = 40; 
Distancia_Entre_Centros = diametro_exterior + Separacion_Reactores; 

// --- PARÁMETROS DEL MANIFOLD (TUBERÍA) ---
Radio_Manifold = 8;
Radio_Conexion_Vertical = Radio_Manifold / 2;
Longitud_Conexion_Vertical = 50; 
Longitud_Saliente_Conexion = 10; 

// ALTURA DE AJUSTE CLAVE: Base del manifold (tubería horizontal)
Altura_Base_Manifold = altura_total_capsula + Longitud_Saliente_Conexion + Longitud_Conexion_Vertical;

$fn = 60; // Suavidad para todas las curvas

// Cálculo de la posición X inicial para centrar el arreglo
posicion_x_base = -((Num_Reactores - 1) * Distancia_Entre_Centros) / 2;


// ------------------------------------------------------------------
// --- MÓDULO 2: REACTOR TIPO CÁPSULA (GEOMETRÍA CORREGIDA) ---
// ------------------------------------------------------------------
module Reactor_Capsula() {
    // 1. Objeto Sólido Exterior
    module Solido_Exterior_Capsula() {
        union() {
            // Cuerpo cilíndrico central (inicia en Z=radio_exterior)
            translate([0, 0, radio_exterior]) {
                cylinder(r = radio_exterior, h = longitud_cilindro_recto);
            }
            // Tapa semiesférica superior
            translate([0, 0, longitud_cilindro_recto + radio_exterior]) {
                sphere(r = radio_exterior);
            }
            // Base semiesférica inferior (Base Redonda): Centrada en Z=radio_exterior.
            // Esto asegura que la parte inferior de la esfera toque Z=0, y su parte superior (el ecuador)
            // coincida con la base del cilindro recto.
            translate([0, 0, radio_exterior]) { 
                intersection() {
                    sphere(r = radio_exterior);
                    // Cortamos solo la mitad inferior (Z <= radio_exterior)
                    translate([-radio_exterior, -radio_exterior, -radio_exterior]) {
                        cube([diametro_exterior, diametro_exterior, radio_exterior]);
                    }
                }
            }
        }
    }

    // 2. Objeto Hueco Interior
    module Solido_Interior_Capsula() {
        union() {
            // Cuerpo cilíndrico central interior
            translate([0, 0, radio_interior]) {
                cylinder(r = radio_interior, h = longitud_cilindro_recto);
            }
            // Tapa semiesférica superior interior
            translate([0, 0, longitud_cilindro_recto + radio_interior]) {
                sphere(r = radio_interior);
            }
            // Base semiesférica inferior interior
            translate([0, 0, radio_interior]) {
                intersection() {
                    sphere(r = radio_interior);
                    // Cortamos solo la mitad inferior (Z <= radio_interior)
                    translate([-radio_interior, -radio_interior, -radio_interior]) {
                        cube([radio_interior * 2, radio_interior * 2, radio_interior]);
                    }
                }
            }
        }
    }

    // Reactor final (diferencia del exterior y el interior)
    difference() {
        color([0.6, 0.2, 0.0]) Solido_Exterior_Capsula();
        // El interior se traslada hacia arriba por el grosor de pared
        translate([0, 0, grosor_pared]) Solido_Interior_Capsula();
    }
}

// ------------------------------------------------------------------
// --- MÓDULO 3: CONEXIÓN SUPERIOR (Tubo de salida) ---
// ------------------------------------------------------------------
module Conexion_Superior() {
    // Tubo que sale de la tapa superior semiesférica
    color([0.5, 0.5, 0.5]) {
        translate([0, 0, altura_total_capsula]) {
             cylinder(r = Radio_Conexion_Vertical, h = Longitud_Saliente_Conexion);
        }
    }
}

// ------------------------------------------------------------------
// --- MÓDULO 4: MANIFOLD EN PARALELO ---
// ------------------------------------------------------------------
module Manifold_Paralelo() {
    // 1. Tubería Principal Horizontal
    longitud_manifold = (Num_Reactores - 1) * Distancia_Entre_Centros + diametro_exterior;
    
    translate([posicion_x_base - radio_exterior, 0, Altura_Base_Manifold]) { 
        color([0.5, 0.5, 0.5]) {
            rotate([0, 90, 0]) {
                cylinder(r = Radio_Manifold, h = longitud_manifold);
            }
        }
    }

    // 2. Tuberías de Conexión Vertical y Válvulas
    for (i = [0 : Num_Reactores - 1]) {
        x_pos_reactor = posicion_x_base + i * Distancia_Entre_Centros;
        
        // Punto de inicio de la conexión vertical
        altura_inicio_conn = altura_total_capsula + Longitud_Saliente_Conexion;

        // Tubería vertical (Conexión Tanque -> Manifold)
        translate([x_pos_reactor, 0, altura_inicio_conn]) {
            color([0.5, 0.5, 0.5]) {
                cylinder(r = Radio_Conexion_Vertical, h = Longitud_Conexion_Vertical); 
            }

            // Válvula 
            translate([0, 0, Longitud_Conexion_Vertical / 2]) { 
                color([0.8, 0.1, 0.1]) {
                    sphere(r = Radio_Manifold * 0.8);
                    translate([Radio_Manifold * 0.8, 0, 0]) {
                        rotate([0, 90, 0]) {
                            cylinder(r = Radio_Manifold / 4, h = 15);
                        }
                    }
                }
            }
        }
    }
    
    // 3. Válvula Principal de Entrada/Salida
    translate([posicion_x_base + longitud_manifold / 2 + Radio_Manifold * 3, 0, Altura_Base_Manifold]) {
        color([0, 0.6, 0.1]) {
            sphere(r = Radio_Manifold * 1.5);
            translate([Radio_Manifold * 1.5, 0, 0]) {
                rotate([0, 90, 0]) {
                    cylinder(r = Radio_Manifold, h = 50);
                }
            }
        }
    }
}


// ------------------------------------------------------------------
// --- ENSAMBLAJE DEL SISTEMA COMPLETO ---
// ------------------------------------------------------------------

// 1. Colocar los reactores tipo cápsula y la conexión superior
for (i = [0 : Num_Reactores - 1]) {
    x_pos_reactor = posicion_x_base + i * Distancia_Entre_Centros;
    translate([x_pos_reactor, 0, 0]) {
        // El reactor se coloca sin translate adicional ya que se diseñó para empezar en Z=0
        Reactor_Capsula();
        Conexion_Superior();
    }
}

// 2. Colocar el Manifold
Manifold_Paralelo();