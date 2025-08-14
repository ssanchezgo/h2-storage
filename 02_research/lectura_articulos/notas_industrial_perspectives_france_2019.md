# Notas de Lectura: Hidrogen Storage: Recent improvements and indrustria perspective

**Autores:** Barthélémy H., Vidovic M., Weber M., Bardoux O., Papin P.
**Referencia BibTeX:** `p.papin-2019`
**Fecha de publicación:** 2019

---

## 1. Resumen y Propósito del Artículo

[Escribe aquí tu propio resumen del artículo. El objetivo es proporcionar una visión general de lo que se trata el documento y por qué es relevante para tu proyecto. El artículo aborda el almacenamiento de hidrógeno, centrándose en tanques de alta presión y los problemas y limitaciones de los materiales y estructuras en condiciones de uso de la energía de hidrógeno.] [@p.papin-2019]

---

## 2. Tipos de Almacenamiento y Materiales

### Diagrama de Flujo de Tecnologías de Tanques y Tabla de Propiedades

[Este diagrama te ayudará a visualizar los diferentes tipos de tanques y sus características. Puedes utilizar la información de la Figura 4 del artículo para crear este diagrama.] [@p.papin-2019]

### Diagrama de Flujo de Tecnologías de Tanques

```mermaid
graph TD
    A[Almacenamiento H2 Comprimido] --> B{Tipo de Tanque};
    B --> C[Tipo I (Metal)];
    B --> D[Tipo II (Metal + Composite en cilindro)];
    B --> E[Tipo III (Liner de Metal + Composite total)];
    B --> F[Tipo IV (Liner de Polímero + Composite total)];
    F --> G(Liner de polímero: rotomoldeo, moldeo por soplado o soldadura);
    G --> H[Partes metálicas (boss) pueden insertarse o pegarse];
    E --> I[Liner de metal + bobinado de filamento para el composite];
    D --> J[Liner de metal + bobinado de filamento en el cilindro];
    C --> K[Fabricación: a partir de placas, billetes o tubos];
