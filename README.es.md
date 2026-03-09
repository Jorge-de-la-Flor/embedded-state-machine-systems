README en [inglés](README.md)

# Máquinas de Estados Embebidas

Este repositorio explora las arquitecturas de estados finitos comúnmente utilizadas en sistemas embebidos y ciberfísicos.

Las implementaciones demuestran cómo se pueden utilizar las máquinas de estados deterministas para estructurar el comportamiento de sistemas en robótica y sistemas controlados por sensores.

## Contenido

- traffic_light_fsm.py

Controlador basado en estados para un semáforo temporizado.

- robot_navigation_fsm.py

Comportamiento de navegación reactiva con detección de obstáculos.

- sensor_monitor_fsm.py

Monitorización del umbral del sensor con estados de escalada.

## Objetivo

Estos ejemplos ilustran patrones arquitectónicos relevantes para:

- Diseño de sistemas embebidos
- Control del comportamiento robótico
- Modelado de sistemas ciberfísicos

## Motivación

Las arquitecturas de sistemas basadas en estados son un patrón de diseño fundamental en sistemas embebidos y ciberfísicos. Muchos sistemas de control del mundo real deben operar bajo estrictas restricciones de tiempo y lógica determinista, lo que convierte a los modelos de estados finitos en una forma práctica e interpretable de estructurar el comportamiento.

Estas implementaciones exploran cómo se pueden utilizar máquinas de estados simples para organizar la detección, el control y el comportamiento reactivo en entornos robóticos embebidos.
