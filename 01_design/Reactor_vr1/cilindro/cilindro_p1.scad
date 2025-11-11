// Definir los parámetros
r = 100;    // Radio interno en mm
h = 500;    // Altura del cilindro en mm
e = 10;     // Espesor de la pared en mm

// Crear el cilindro exterior e interior
cylinder(h = h, r = r + e, $fn = 64);
cylinder(h = h, r = r, $fn = 64);

// Booleanas para crear el tanque hueco
difference() {
    cylinder(h = h, r = r + e, $fn = 64);
    cylinder(h = h, r = r, $fn = 64);
}