# 🚦 Two-Way Traffic Signal System – DLD Semester Project

## 📌 Project Overview

This project is a **Two-Way Traffic Signal System** developed as a semester project for the subject **Digital Logic Design (DLD)**.

The system is designed to automatically control traffic signals for two roads using digital logic components. It uses a NE555 Timer IC, 74HC163 Binary Counter, and logic gates to generate the required traffic light sequence.

The project demonstrates how digital electronic components can be combined to develop an automatic traffic control system.

## 🎯 Project Objectives

- Understand the practical applications of digital logic circuits.
- Design an automatic traffic signal control system for two roads.
- Implement timing and counting operations using digital ICs.
- Apply Boolean expressions and logic gates.
- Simulate and implement the traffic signal circuit.

## 🛠️ Components and Technologies Used

### Hardware Components

- NE555 Timer IC
- 74HC163 4-bit Binary Counter
- 74LS04 NOT Gate IC
- 74LS08 AND Gate IC
- Red LEDs × 2
- Yellow LEDs × 2
- Green LEDs × 2
- Breadboard
- Jumper Wires
- Resistors and Capacitors
- 9V Power Supply

### Software / Simulation

- Proteus (Circuit Simulation)

## ⚙️ Working Principle

The system uses the NE555 Timer IC to generate continuous clock pulses. These pulses are supplied to the 74HC163 binary counter.

The counter changes its binary output with each clock pulse. The logic gates detect different counter states and activate the corresponding traffic signal LEDs.

When one road receives a green signal, the other road remains red. Yellow lights provide a warning before the traffic signals switch between the two roads.

The process repeats automatically.

## 🚦 Traffic Signal Sequence

The system follows this sequence:

| Counter States | Road A | Road B |
|---|---|---|
| 0–5 | Red | Green |
| 6–7 | Red | Yellow |
| 8–13 | Green | Red |
| 14–15 | Yellow | Red |

The designed timing sequence includes:

- Green Light: 6 seconds
- Yellow Light: 2 seconds

## 🧠 Digital Logic Concepts Implemented

- Binary counting using the 74HC163 counter.
- Clock pulse generation using the NE555 timer.
- Boolean expressions.
- Truth tables.
- NOT and AND logic gates.
- Digital state-based signal control.

### Boolean Expressions

The following expressions are used for traffic signal control:

```text
AR = Q3'
AG = Q3 · Q2'
AY = Q3 · Q2

BR = Q3
BG = Q3' · Q2'
BY = Q3' · Q2
```

Where:
- AR = Road A Red
- AG = Road A Green
- AY = Road A Yellow
- BR = Road B Red
- BG = Road B Green
- BY = Road B Yellow

## ✨ Project Features

- Automatic two-road traffic signal control.
- Sequential operation of red, yellow, and green LEDs.
- Timer-based clock pulse generation.
- Binary counter-based signal transitions.
- Logic gate-based control.
- Circuit simulation and hardware implementation.

## 📂 Project Structure

```text
DLD-Semester-Project/
│
├── DLD-Semester-Project.pdf
├── README.md
│
└── Screenshots/
    ├── circuit-simulation.png
    └── hardware-implementation.png
```

## ▶️ How to View the Project

1. Download the project repository.
2. Open the project report PDF.
3. Review the circuit design, truth table, and Boolean expressions.
4. Explore the simulation and hardware implementation screenshots.

For circuit simulation, use the Proteus software and recreate the circuit according to the project documentation.

## 📚 Concepts Learned

Through this project, I gained practical experience in:

- Digital counters and timing circuits.
- Boolean algebra and logic expressions.
- Truth table development.
- Combinational logic design.
- Digital circuit simulation.
- Hardware implementation using ICs.

## 🚀 Future Improvements

- Add pedestrian crossing signals.
- Introduce emergency vehicle priority.
- Implement adjustable signal timing.
- Integrate sensors for traffic density detection.
- Explore AI-based traffic management in a future version.

## 🎓 Academic Information

- **Student:** Umair Shabbir
- **Registration ID:** 2502027
- **University:** Air University Islamabad
- **Degree:** BS Artificial Intelligence
- **Semester:** 2nd Semester
- **Subject:** Digital Logic Design (DLD)
- **Instructor:** Sir Ali Raza
- **Project:** Two-Way Traffic Signal System

---

*Developed as an academic project to understand and implement digital logic concepts through an automatic traffic signal control system.*
