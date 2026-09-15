# Optimisation Approach

## Purpose

The purpose of this section is to define the optimisation problem for the Cessna 152 cruise-performance study.

The previous sections established a physically defined baseline condition using published aircraft data, a defined cruise altitude and speed, and atmospheric conditions derived from the NASA Standard Atmosphere.

The next stage is to investigate how changes in aerodynamic operating conditions affect aircraft efficiency.

The primary focus is the relationship between:

- Lift generation
- Drag production
- Aerodynamic efficiency
- Angle of attack

The objective is not simply to maximise lift. Increasing lift can also be associated with increased drag, meaning that the condition producing more lift is not necessarily the condition producing the most efficient flight.

---

## Engineering Problem

For steady, level cruise flight:

L = W

where:

L = lift force  
W = aircraft weight

The aircraft must therefore generate sufficient lift to support its weight.

However, the aircraft also experiences aerodynamic drag:

D = 0.5 ρV²SCD

where:

D = drag force  
ρ = air density  
V = airspeed  
S = wing area  
CD = drag coefficient

The optimisation problem therefore becomes a trade-off between generating the required lift and minimising the drag associated with producing that lift.

---

## Primary Research Question

The central question for the optimisation study is:

**What aerodynamic operating condition provides an efficient level of lift while avoiding an excessive drag penalty during Cessna 152 cruise flight?**

A secondary question is:

**How does angle of attack influence lift, drag and aerodynamic efficiency within the selected cruise condition?**

---

## Why Angle of Attack is Important

Angle of attack is the angle between the aircraft wing's reference chord line and the relative airflow.

Changing angle of attack changes the aerodynamic forces produced by the wing.

Within the normal operating range, increasing angle of attack generally increases lift.

However, increasing angle of attack also affects drag. At sufficiently high angles of attack, drag can increase significantly and aerodynamic efficiency can decrease.

This creates a potential optimisation problem rather than a simple maximum-lift problem.

The study will therefore investigate the relationship between angle of attack, lift and drag rather than considering lift independently.

---

## Aerodynamic Efficiency

A useful measure of aerodynamic efficiency is the lift-to-drag ratio:

L/D = L / D

where:

L = lift  
D = drag

A higher L/D ratio indicates that the aircraft is producing more lift relative to the drag penalty.

For the cruise study, L/D will therefore be considered as a potential measure of aerodynamic efficiency.

The optimisation objective can be expressed conceptually as:

**Identify the operating region where aerodynamic efficiency is high while the aircraft continues to satisfy the requirements of steady, level cruise flight.**

---

## Baseline Condition

The optimisation will initially use the baseline cruise condition established in the previous sections:

| Parameter | Baseline value |
|---|---:|
| Aircraft | Cessna 152 |
| Altitude | 8,000 ft |
| Altitude | 2,438.4 m |
| Airspeed | 107 kt |
| Airspeed | approximately 55.05 m/s |
| Aircraft mass | approximately 757.50 kg |
| Aircraft weight | approximately 7,431 N |
| Wing area | approximately 14.82 m² |
| Air density | approximately 0.963 kg/m³ |
| Required lift | approximately 7,431 N |
| Derived lift coefficient | approximately 0.344 |

This baseline provides the reference condition against which changes in aerodynamic operating conditions can be assessed.

---

## Proposed Optimisation Variable

The initial variable selected for investigation is:

**Angle of attack (α)**

The purpose of varying angle of attack is to investigate how the aerodynamic response changes while maintaining a physically meaningful aircraft condition.

The study will seek to establish a relationship between:

**Angle of attack → lift → drag → aerodynamic efficiency**

---

## Required Aerodynamic Data

A valid angle-of-attack optimisation requires an aerodynamic relationship between angle of attack and the corresponding lift and drag behaviour.

The study will therefore require a defensible source or method for establishing:

- Lift coefficient as a function of angle of attack
- Drag coefficient as a function of angle of attack
- The applicable range of angle of attack
- The assumptions and limitations associated with the aerodynamic model

These quantities will not be arbitrarily prescribed.

Where possible, the data will be obtained from an appropriate published aerodynamic source or derived using a documented aerodynamic methodology.

---

## Planned Analysis

Once a defensible aerodynamic dataset or model has been established, the analysis will investigate:

1. Angle of attack against lift coefficient
2. Angle of attack against drag coefficient
3. Angle of attack against lift-to-drag ratio
4. The corresponding lift and drag forces under the baseline cruise conditions
5. The region providing high aerodynamic efficiency
6. The limitations of the simplified model

The resulting relationships will be used to identify an efficient operating region rather than claiming a single universally optimal angle of attack.

---

## Important Methodological Constraint

The optimisation analysis will not introduce arbitrary values for CL or CD simply to produce a desired graph.

This is a deliberate change from the original project.

The original project prescribed aerodynamic coefficients as numerical inputs in order to demonstrate mathematical relationships.

The current study instead requires the aerodynamic quantities to be connected to:

**Aircraft → Flight condition → Atmospheric condition → Aerodynamic behaviour → Performance**

This provides a more physically representative engineering methodology.

---

## Current Status

The baseline aircraft and atmospheric conditions have been established.

The derived baseline lift coefficient is:

CL ≈ 0.344

The next stage is to establish a defensible aerodynamic relationship between angle of attack, lift and drag before calculating the optimisation results.

No drag coefficient or optimum angle of attack is assumed at this stage.
