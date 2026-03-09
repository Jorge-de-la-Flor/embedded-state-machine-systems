README in [Spanish](README.es.md)

# Embedded State Machines

This repository explores finite-state architectures commonly used in
embedded and cyber-physical systems.

The implementations demonstrate how deterministic state machines can be
used to structure system behaviour in robotics and sensor-driven systems.

## Contents

- traffic_light_fsm.py

    State-based controller for a timed traffic signal.

- robot_navigation_fsm.py

    Reactive navigation behaviour with obstacle detection.

- sensor_monitor_fsm.py

    Sensor threshold monitoring with escalation states.

## Purpose

These examples illustrate architectural patterns relevant to:

- embedded systems design
- robotics behaviour control
- cyber-physical system modelling

## Motivation

State-based system architectures are a fundamental design pattern in
embedded and cyber-physical systems. Many real-world control systems
must operate under strict timing constraints and deterministic logic,
making finite-state models a practical and interpretable way to
structure behaviour.

These implementations explore how simple state machines can be used
to organise sensing, control, and reactive behaviour in embedded
robotics environments.
