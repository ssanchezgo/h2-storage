// Cuerpo_Reactor.scad
// Unidades: milímetros (mm). Diseñado para 5 kg de MH.

// --- Parámetros de Diseño ---
D_INT = 150;      // Diámetro Interno (D)
L_INT = 225;      // Longitud Interna (L)
T_PARED = 15;     // Espesor de la pared para alta presión (ej. 30+ bar)
D_EXT = D_INT + 2*T_PARED; // Diámetro Exterior (180 mm)

// --- Parámetros de la Brida (Flange) ---
T_BRIDA = 20;     // Espesor de la brida para rigidez
D_BRIDA_EXT = D_EXT + 40; // Diámetro exterior de la brida (220 mm)
N_PERNOS = 8;     // Número de pernos M10
D_PERNO = 10.5;   // Diámetro del orificio del perno
PCD_BRIDA = 195;  // Diámetro del Círculo de Paso (Pitch Circle Diameter)

// ----------------------------------------------------------------------

module Brida() {
  // Cilindro de la brida
  cylinder(h = T_BRIDA, r = D_BRIDA_EXT / 2, $fn = 60);

  // Perforaciones de la brida para los pernos
  for (i = [0 : 360/N_PERNOS : 360 - (360/N_PERNOS)]) {
    rotate([0, 0, i]) {
      translate([PCD_BRIDA / 2, 0, -0.1]) {
        // El cilindro de la perforación debe atravesar la brida
        cylinder(h = T_BRIDA + 0.2, r = D_PERNO / 2, $fn = 20);
      }
    }
  }
}

module CuerpoReactor() {
  // 1. Cuerpo Principal (Tubo)
  difference() {
    // Cilindro Exterior
    cylinder(h = L_INT, r = D_EXT / 2, $fn = 60);

    // Vaciado Interno
    // NOTA: Se añade +0.1 a la altura para asegurar el vaciado completo en Z=0
    translate([0, 0, 0]) {
      cylinder(h = L_INT + 0.1, r = D_INT / 2, $fn = 60);
    }
  }

  // 2. Brida Superior (unida al cuerpo)
  // La brida se coloca en el extremo superior del cilindro (L_INT - T_BRIDA)
  translate([0, 0, L_INT - T_BRIDA]) { 
      Brida();
  }
}

// Visualización del Módulo
CuerpoReactor();