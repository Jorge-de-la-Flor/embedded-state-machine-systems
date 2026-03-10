[English](README.md) | Español

# Sistemas de Máquinas de Estados Embebidos

Experimentos mínimos que ilustran arquitecturas de estados finitos comúnmente utilizadas en sistemas embebidos y ciberfísicos.

Este repositorio explora patrones deterministas de máquinas de estados que se utilizan frecuentemente para estructurar el comportamiento en robótica, controladores embebidos y sistemas controlados por sensores.

Los ejemplos demuestran cómo se puede organizar el comportamiento del sistema mediante estados explícitos y transiciones para construir una lógica de control predecible e interpretable.

## Contenido

El directorio `src/` contiene tres experimentos mínimos:

* `traffic_light_fsm.py`

    Implementa un controlador de semáforo determinista utilizando una máquina de estados finitos.

* `robot_navigation_fsm.py`

    Simula la navegación reactiva de un robot con detección y evitación de obstáculos.

* `sensor_monitor_fsm.py`

    Demuestra la monitorización basada en umbrales con estados de alerta del sistema progresivos.

## Propósito

Estos experimentos ilustran conceptos de ingeniería relevantes para:

* Arquitectura de sistemas embebidos
* Control del comportamiento robótico
* Diseño de máquinas de estados finitos
* Coordinación de sistemas ciberfísicos

## Motivación

Las máquinas de estados finitos son un patrón de diseño fundamental en sistemas embebidos y robótica.

Muchos sistemas de control del mundo real deben operar bajo estrictas restricciones de tiempo y lógica determinista. Las arquitecturas basadas en estados proporcionan una forma sencilla y fiable de organizar el comportamiento del sistema, facilitando la comprensión, implementación y depuración de flujos de control complejos.

Estos ejemplos exploran cómo los modelos simples de máquinas de estados pueden estructurar la detección, la toma de decisiones y el comportamiento de control en entornos embebidos y robóticos.

## Método

El repositorio implementa máquinas de estados finitos (MSF) deterministas que representan comportamientos típicos de control embebidos.

Los experimentos incluyen:

* Transiciones de estado temporizadas para lógica de control determinista
* Cambios de estado controlados por eventos basados ​​en la entrada simulada de un sensor
* Comportamiento robótico reactivo en respuesta a las condiciones ambientales

Estas implementaciones simplificadas ilustran las ideas centrales de las arquitecturas de control basadas en estados en sistemas ciberfísicos.

Los ejemplos son intencionadamente minimalistas y se centran en demostrar la estructura conceptual de las máquinas de estados finitos, en lugar del firmware embebido de producción.

## Ejecución de los ejemplos

Clonar el repositorio y ejecutar cualquiera de los scripts:

```bash
git clone https://github.com/Jorge-de-la-Flor/embedded-state-machine-systems
cd embedded-state-machine-systems
python src/traffic_light_fsm.py
```

Cada script simula el comportamiento del sistema e imprime las transiciones de estado resultantes en la consola.

## Árbol del proyecto

```bash
embedded-state-machine-systems
├─ .python-version
├─ LICENCIA
├─ README.es.md
├─ README.md
├─ pyproject.toml
├─ src
│ ├─ robot_navigation_fsm.py
│ ├─ sensor_monitor_fsm.py
│ └─ traffic_light_fsm.py
└─ uv.lock
```

## Requisitos

Los ejemplos utilizan:

* Python 3.12+

No se requieren dependencias externas.

## Referencias

* Samek, M. (2008).
*Diagramas de estado UML prácticos en C/C++.*

* Lee, E. A. y Seshia, S. A. (2017).
*Introducción a los sistemas embebidos: Un enfoque de sistemas ciberfísicos.*
