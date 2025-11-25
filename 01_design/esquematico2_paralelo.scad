// --- PARÁMETROS GENERALES DEL SISTEMA ---
diametro_exterior = 60;
radio_exterior = diametro_exterior / 2;
grosor_pared = 5;
radio_interior = radio_exterior - grosor_pared;

// --- PARÁMETROS DEL REACTOR TIPO CÁPSULA ---
longitud_cilindro_recto = 120; 
altura_total_capsula = longitud_cilindro_recto + diametro_exterior; 

// --- PARÁMETROS DEL ARREGLO EN 2D (Cuadrícula) ---
Num_Columnas_X = 4;
Num_Filas_Y = 2;   

Separacion_Reactores = 40; 
Distancia_Entre_Centros = diametro_exterior + Separacion_Reactores; 

// --- PARÁMETROS DEL MANIFOLD (TUBERÍA) ---
Radio_Manifold = 8;
Radio_Conexion_Vertical = Radio_Manifold / 2;
Longitud_Conexion_Vertical = 50; 
Longitud_Saliente_Conexion = 10; 

// ALTURA CLAVE
Altura_Base_Manifold = altura_total_capsula + Longitud_Saliente_Conexion + Longitud_Conexion_Vertical;

$fn = 60; 

// Cálculo de la posición X y Y inicial para centrar el arreglo
posicion_x_base = -((Num_Columnas_X - 1) * Distancia_Entre_Centros) / 2;
posicion_y_base = -((Num_Filas_Y - 1) * Distancia_Entre_Centros) / 2;


// ------------------------------------------------------------------
// --- MÓDULO 1: REACTOR TIPO CÁPSULA ---
// ------------------------------------------------------------------
module Reactor_Capsula() {
    module Solido_Exterior_Capsula() {
        union() {
            translate([0, 0, radio_exterior]) cylinder(r = radio_exterior, h = longitud_cilindro_recto);
            translate([0, 0, longitud_cilindro_recto + radio_exterior]) sphere(r = radio_exterior);
            translate([0, 0, radio_exterior]) intersection() {
                sphere(r = radio_exterior);
                translate([-radio_exterior, -radio_exterior, -radio_exterior]) cube([diametro_exterior, diametro_exterior, radio_exterior]);
            }
        }
    }
    module Solido_Interior_Capsula() {
        union() {
            translate([0, 0, radio_interior]) cylinder(r = radio_interior, h = longitud_cilindro_recto);
            translate([0, 0, longitud_cilindro_recto + radio_interior]) sphere(r = radio_interior);
            translate([0, 0, radio_interior]) intersection() {
                sphere(r = radio_interior);
                translate([-radio_interior, -radio_interior, -radio_interior]) cube([radio_interior * 2, radio_interior * 2, radio_interior]);
            }
        }
    }
    difference() {
        color([0.6, 0.2, 0.0]) Solido_Exterior_Capsula();
        translate([0, 0, grosor_pared]) Solido_Interior_Capsula();
    }
}

// ------------------------------------------------------------------
// --- MÓDULO 2: CONEXIÓN DE SALIDA SUPERIOR DEL TANQUE ---
// ------------------------------------------------------------------
module Conexion_Saliente_Tanque() {
    color([0.5, 0.5, 0.5]) {
        translate([0, 0, altura_total_capsula]) {
             cylinder(r = Radio_Conexion_Vertical, h = Longitud_Saliente_Conexion);
        }
    }
}

// ------------------------------------------------------------------
// --- MÓDULO 3: MANIFOLD CON ROTACIÓN DE DIRECCIÓN (ESTABLE) ---
// ------------------------------------------------------------------
module Manifold_Completo_2D_Rotado() {
    
    // 1. Manifold Principal (Eje Y) - Tubo Colector Central
    longitud_manifold_Y = (Num_Filas_Y - 1) * Distancia_Entre_Centros + diametro_exterior;
    x_pos_manifold_principal = posicion_x_base + (Num_Columnas_X - 1) * Distancia_Entre_Centros + Radio_Manifold * 2;
    
    translate([x_pos_manifold_principal, posicion_y_base - radio_exterior, Altura_Base_Manifold]) { 
        color([0.5, 0.5, 0.5]) {
            rotate([90, 0, 0]) { // Gira 90 grados en X para correr a lo largo del Eje Y
                cylinder(r = Radio_Manifold, h = longitud_manifold_Y);
            }
        }
    }

    // 2. Conexiones Verticales y Manifolds Secundarios (Eje X)
    for (j = [0 : Num_Filas_Y - 1]) { // Línea 105
        y_pos_reactor = posicion_y_base + j * Distancia_Entre_Centros;

        // --- a) Manifold Secundario (Eje X - Conecta las columnas a la tubería Principal)
        longitud_conexion_secundaria = x_pos_manifold_principal - (posicion_x_base - Radio_Manifold) + Radio_Manifold;

        translate([posicion_x_base - Radio_Manifold, y_pos_reactor, Altura_Base_Manifold]) { 
            color([0.5, 0.5, 0.5]) {
                rotate([0, 90, 0]) { // Línea 112 (La línea 109 está por aquí)
                    cylinder(r = Radio_Manifold, h = longitud_conexion_secundaria);
                }
            }
        } // Fin del Manifold Secundario
        
        // --- b) Conexiones Individuales Tanque -> Manifold Secundario (Eje Z)
        for (i = [0 : Num_Columnas_X - 1]) {
            x_pos_reactor = posicion_x_base + i * Distancia_Entre_Centros;
            
            altura_inicio_conn = altura_total_capsula + Longitud_Saliente_Conexion;
            
            translate([x_pos_reactor, y_pos_reactor, altura_inicio_conn]) {
                color([0.5, 0.5, 0.5]) {
                    cylinder(r = Radio_Conexion_Vertical, h = Longitud_Conexion_Vertical); 
                }

                // Válvula de control individual 
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
        } // Fin del for (i)
    } // Fin del for (j)
    
    // 3. Conexión y Válvula Principal
    translate([x_pos_manifold_principal, posicion_y_base + longitud_manifold_Y / 2, Altura_Base_Manifold]) {
        color([0, 0.6, 0.1]) {
            sphere(r = Radio_Manifold * 1.5);
            
            // Tubería de salida
            rotate([0, 90, 0]) { 
                translate([0, 0, Radio_Manifold * 1.5]) { 
                    cylinder(r = Radio_Manifold, h = 50);
                }
            }
        }
    }
}


// ------------------------------------------------------------------
// --- ENSAMBLAJE DEL SISTEMA COMPLETO 2D ---
// ------------------------------------------------------------------

// 1. Colocar los reactores y la conexión de salida individual
for (i = [0 : Num_Columnas_X - 1]) { 
    x_pos_reactor = posicion_x_base + i * Distancia_Entre_Centros;
    
    for (j = [0 : Num_Filas_Y - 1]) { 
        y_pos_reactor = posicion_y_base + j * Distancia_Entre_Centros;

        translate([x_pos_reactor, y_pos_reactor, 0]) {
            Reactor_Capsula();
            Conexion_Saliente_Tanque();
        }
    }
}

// 2. Colocar el Manifold Completo Rotado
Manifold_Completo_2D_Rotado();