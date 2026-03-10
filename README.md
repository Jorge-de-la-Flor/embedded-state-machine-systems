English | [Español](README.es.md)

# Embedded State Machine Systems

Minimal experiments illustrating finite-state architectures commonly used in embedded and cyber-physical systems.

This repository explores deterministic state-machine patterns that are frequently used to structure behaviour in robotics, embedded controllers, and sensor-driven systems.

The examples demonstrate how system behaviour can be organised using explicit states and transitions to build predictable and interpretable control logic.

## Contents

The `src/` directory contains three minimal experiments:

* `traffic_light_fsm.py`

  Implements a deterministic traffic light controller using a finite state machine.

* `robot_navigation_fsm.py`

  Simulates reactive robot navigation with obstacle detection and avoidance behaviour.

* `sensor_monitor_fsm.py`

  Demonstrates threshold-based monitoring with escalating system alert states.

## Purpose

These experiments illustrate engineering concepts relevant to:

* embedded systems architecture
* robotics behaviour control
* finite state machine design
* cyber-physical system coordination

## Motivation

Finite state machines are a fundamental design pattern in embedded systems and robotics.

Many real-world control systems must operate under strict timing constraints and deterministic logic. State-based architectures provide a simple and reliable way to organise system behaviour, making complex control flows easier to understand, implement, and debug.

These examples explore how simple state-machine models can structure sensing, decision-making, and control behaviour in embedded and robotics environments.

## Method

The repository implements deterministic finite-state machines (FSMs) representing typical embedded control behaviours.

The experiments include:

* timed state transitions for deterministic control logic
* event-driven state changes based on simulated sensor input
* reactive robotic behaviour responding to environmental conditions

These simplified implementations illustrate the core ideas behind state-based control architectures in cyber-physical systems.

The examples are intentionally minimal and focus on demonstrating the conceptual structure of finite state machines rather than production embedded firmware.

## Running the examples

Clone the repository and run any of the scripts:

```bash
git clone https://github.com/Jorge-de-la-Flor/embedded-state-machine-systems
cd embedded-state-machine-systems
python src/traffic_light_fsm.py
```

Each script simulates system behaviour and prints the resulting state transitions in the console.

## Project tree

```bash
embedded-state-machine-systems
├─ .python-version
├─ LICENSE
├─ README.es.md
├─ README.md
├─ pyproject.toml
├─ src
│  ├─ robot_navigation_fsm.py
│  ├─ sensor_monitor_fsm.py
│  └─ traffic_light_fsm.py
└─ uv.lock
```

## Requirements

The examples use:

* Python 3.12+

No external dependencies are required.

## References

* Samek, M. (2008).
  *Practical UML Statecharts in C/C++.*

* Lee, E. A., & Seshia, S. A. (2017).
  *Introduction to Embedded Systems: A Cyber-Physical Systems Approach.*
