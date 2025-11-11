// Tapa_Superior.scad
// Unidades: milímetros (mm)

// --- Parámetros de Diseño (deben coincidir con Cuerpo_Reactor) ---
D_INT = 150;      // Diámetro Interno del Cuerpo
T_PARED = 15;
D_EXT = D_INT + 2*T_PARED; // Diámetro Exterior (180 mm)

// --- Parámetros de la Tapa y Brida ---
T_BRIDA = 20;     // Espesor de la brida
T_TAPA_TOTAL = 45; // Espesor total de la tapa (incluye brida)
D_BRIDA_EXT = D_EXT + 40; // Diámetro exterior de la brida (220 mm)
N_PERNOS = 8;
D_PERNO = 10.5;
PCD_BRIDA = 195;

// --- Parámetros del Sello (O-ring) ---
D_ORING_PCD = D_INT + 5; // Diámetro del círculo de paso del O-ring (ej. 155 mm)
ANCHO_ORING = 3;         // Ancho de la ranura
PROFUNDIDAD_ORING = 2;   // Profundidad de la ranura

// --- Puertos ---
D_H2_PORT = 15;     // Puerto central H2
D_IC_PORT = 10;     // Puertos In/Out del Intercambiador de Calor (IC)
PCD_IC_PORT = 60;   // PCD de los puertos del IC

// ----------------------------------------------------------------------

module BridaTapa() {
  // Cilindro de la brida
  cylinder(h = T_BRIDA, r = D_BRIDA_EXT / 2, $fn = 60);

  // Perforaciones de la brida para los pernos
  for (i = [0 : 360/N_PERNOS : 360 - 360/N_PERNOS]) {
    rotate([0, 0, i]) {
      translate([PCD_BRIDA / 2, 0, -0.1]) {
        cylinder(h = T_BRIDA + 0.2, r = D_PERNO / 2, $fn = 20);
      }
    }
  }
}

module TapaSuperior() {
  // 1. Base y Brida
  translate([0, 0, T_TAPA_TOTAL - T_BRIDA]) { // La base de la tapa está en Z=0
    BridaTapa();
  }

  // 2. Parte de Acoplamiento y Sello
  cylinder(h = T_TAPA_TOTAL, r = D_EXT / 2, $fn = 60);

  // 3. Ranura del O-Ring (para sello)
  translate([0, 0, T_TAPA_TOTAL - 5]) { // Ranura cerca de la superficie de contacto
    difference() {
      cylinder(h = PROFUNDIDAD_ORING, r = D_ORING_PCD / 2 + ANCHO_ORING / 2, $fn = 60);
      cylinder(h = PROFUNDIDAD_ORING + 0.1, r = D_ORING_PCD / 2 - ANCHO_ORING / 2, $fn = 60);
    }
  }

  // 4. Perforación del Puerto H2 (Central)
  translate([0, 0, -0.1]) {
    cylinder(h = T_TAPA_TOTAL + 1, r = D_H2_PORT / 2, $fn = 20);
  }

  // 5. Perforaciones de los Puertos del IC (Brine In/Out)
  for (i = [0, 180]) { // Dos puertos a 180 grados
    rotate([0, 0, i]) {
      translate([PCD_IC_PORT / 2, 0, -0.1]) {
        cylinder(h = T_TAPA_TOTAL + 1, r = D_IC_PORT / 2, $fn = 20);
      }
    }
  }
}

// Visualización del Módulo
TapaSuperior();