# Notas de Lectura: Hidrogen Storage: Recent improvements and indrustria perspective

**Autores:** Barthélémy H., Vidovic M., Weber M., Bardoux O., Papin P.
**Referencia BibTeX:** `p.papin-2019`
**Fecha de publicación:** 2019

---

## 1. Resumen y Propósito del Artículo

 El artículo aborda el almacenamiento de hidrógeno, centrándose en tanques de alta presión y los problemas y limitaciones de los materiales y estructuras en condiciones de uso de la energía de hidrógeno. [@p.papin-2019]

---

## 2. Tipos de Almacenamiento y Materiales

### Tecnologías de Tanques y Tabla de Propiedades

Figura 4.

## Esfuerzos principales consideraos para cilindros metalicos

Figura 5.

### Diagrama de Flujo de Tecnologías de Tanques

```mermaid
graph TD
    A[Almacenamiento H2 Comprimido]-->B{Tipo de Tanque};
    B -- Tipo I (Metal) --> C;
    B -- Tipo II (Metal + Composite en cilindro) --> D;
    B -- Tipo III (Liner de Metal + Composite total) --> E;
    B -- Tipo IV (Liner de Polímero + Composite total) --> F;
    F --> G(Liner de polímero: rotomoldeo, moldeo por soplado o soldadura);
    G -- Partes metálicas (boss) pueden insertarse o pegarse --> H;
    E --> I[Liner de metal + bobinado de filamento para el composite];
    D --> J[Liner de metal + bobinado de filamento en el cilindro];
    C --> K[Fabricación: a partir de placas, billetes o tubos];
    
