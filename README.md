# Proyecto de Almacenamiento de Hidrógeno en Estado Sólido (Metal Hydride)

Este repositorio contiene el desarrollo integral de un sistema de almacenamiento de hidrógeno utilizando hidruros metálicos. El proyecto abarca desde la investigación del estado del arte hasta el diseño CAD, simulación térmica y documentación técnica para la construcción de un prototipo de reactor.

## Estructura del Proyecto

**01_design/**: Contiene los diseños mecánicos y geométricos del reactor.

 Modelos CAD en OpenSCAD (`.scad`) y mallas (`.msh`, `.inp`).
 Planos y esquemas de configuraciones de tanques (cilíndricos, modulares).
 Imágenes de renderizado y prototipos.

**02_research/**: Base de conocimiento y revisión bibliográfica.

 Colección de artículos científicos (2007-2026) sobre gestión térmica, materiales y diseño de reactores.
 `Consolidado_Articulos_Completo.md`: Documento maestro con el análisis detallado de 52 papers y 5 revisiones, incluyendo estrategias de gestión térmica (aletas, PCM, tubos internos) y comparativas de materiales (LaNi5 vs TiFe).
 Notas de lectura y resúmenes extraídos.

**03_code/**: Recursos de modelado y simulación.

 Scripts y modelos para la simulación del comportamiento cinético y térmico del hidruro.

**04_documentation/**: Documentación administrativa y de seguimiento.

Reportes mensuales y semanales de avance.
 Diagramas de Gantt y formatos de informes.

 Hojas de datos de materiales (Acero 316L, Carbon Steel).
 Listas de materiales (BOM).
 Cálculos de recipientes a presión y matrices de información.

## Objetivos del Proyecto

1. **Optimización Térmica**: Diseñar estrategias eficientes de intercambio de calor (aletas internas, tubos helicoidales, chaquetas) para mejorar las tasas de absorción y desorción de hidrógeno.
2. **Selección de Materiales**: Evaluar aleaciones tipo AB5 (LaNi5) y TiFe para aplicaciones estacionarias, considerando costos y cinética de activación.
3. **Escalamiento**: Desarrollar una arquitectura modular que permita escalar el sistema desde prototipos de laboratorio hasta aplicaciones industriales (>100 kg).
4. **Seguridad**: Implementar criterios de diseño que mitiguen problemas de decrepitación y estrés mecánico (swelling) en el reactor.

## Estado Actual

Se ha completado una revisión exhaustiva del estado del arte, consolidando información clave sobre gestión térmica y diseño geométrico. Actualmente se encuentra en la fase de diseño detallado y selección de componentes para el prototipo.

---
Autor: ssanchezgo
