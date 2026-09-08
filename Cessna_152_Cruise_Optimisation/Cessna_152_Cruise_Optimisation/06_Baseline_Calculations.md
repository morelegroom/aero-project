# Baseline Cruise Calculations

## Baseline Condition

The following calculations establish a baseline cruise-flight condition for the Cessna 152.

The aircraft data and flight condition are based on the selected 1979 Cessna 152 Pilot's Operating Handbook reference data.

### Given Data

| Parameter                  | Symbol | Value | Unit |
| -------------------------- | -----: | ----: | ---- |
| Maximum takeoff mass       |  \(m\) |  1670 | lb   |
| Cruise speed               |  \(V\) |   107 | kt   |
| Cruise altitude            |  \(h\) |  8000 | ft   |
| Wing area                  |  \(S\) | 159.5 | ft²  |
| Gravitational acceleration |  \(g\) |  9.81 | m/s² |

The maximum takeoff mass is used as the initial conservative baseline condition. It does not imply that the aircraft would necessarily operate at this mass throughout cruise.

---

## 1. Convert Aircraft Mass

The aircraft mass is given as 1670 lb.

### Equation

$$
m_{kg}=m_{lb}\times0.453592
$$

### Substitution

$$
m_{kg}=1670\times0.453592
$$

### Result

$$
\boxed{m=757.50\ kg}
$$

---

## 2. Calculate Aircraft Weight

Weight is calculated from mass using gravitational acceleration.

### Equation

$$
W=mg
$$

### Substitution

$$
W=(757.50)(9.81)
$$

### Result

$$
\boxed{W=7431.08\ N}
$$

---

## 3. Convert Cruise Speed

The published cruise speed is 107 kt.

### Equation

$$
V_{m/s}=V_{kt}\times0.514444
$$

### Substitution

$$
V=107\times0.514444
$$

### Result

$$
\boxed{V=55.05\ m/s}
$$

---

## 4. Convert Wing Area

The published wing area is 159.5 ft².

### Equation

$$
S_{m^2}=S_{ft^2}\times0.092903
$$

### Substitution

$$
S=159.5\times0.092903
$$

### Result

$$
\boxed{S=14.82\ m^2}
$$

---

## 5. Determine Air Density

The baseline cruise altitude is:

$$
h=8000\ ft
$$

The International Standard Atmosphere (ISA) model is used to determine the atmospheric properties at this altitude.

For the baseline calculation:

$$
\boxed{\rho\approx0.963\ kg/m^3}
$$

The derivation of the ISA atmospheric condition is documented separately in `07_ISA_Atmosphere.md`.

---

## 6. Calculate Dynamic Pressure

Dynamic pressure is calculated using:

$$
q=\frac{1}{2}\rho V^2
$$

Using:

$$
\rho=0.963\ kg/m^3
$$

and:

$$
V=55.05\ m/s
$$

### Substitution

$$
q=\frac{1}{2}(0.963)(55.05)^2
$$

### Result

$$
\boxed{q\approx1459.2\ Pa}
$$

---

## 7. Determine Required Lift

The baseline condition assumes steady, level cruise flight.

Therefore:

$$
L=W
$$

From the calculated aircraft weight:

$$
W=7431.08\ N
$$

Therefore:

$$
\boxed{L=7431.08\ N}
$$

The required aerodynamic lift is therefore approximately equal to the aircraft weight under the steady, level flight assumption.

---

## 8. Derive the Lift Coefficient

The lift coefficient is calculated from the required lift and the defined flight condition.

### Equation

$$
C_L=\frac{L}{\frac{1}{2}\rho V^2S}
$$

Using the dynamic pressure calculated above:

$$
C_L=\frac{L}{qS}
$$

### Substitution

$$
C_L=\frac{7431.08}{(1459.2)(14.82)}
$$

### Result

$$
\boxed{C_L\approx0.344}
$$

---

## 9. Baseline Results

| Quantity                 |  Result | Unit  |
| ------------------------ | ------: | ----- |
| Mass                     |  757.50 | kg    |
| Weight                   | 7431.08 | N     |
| Cruise speed             |   55.05 | m/s   |
| Wing area                |   14.82 | m²    |
| Cruise altitude          |    8000 | ft    |
| Air density              |   0.963 | kg/m³ |
| Dynamic pressure         |  1459.2 | Pa    |
| Required lift            | 7431.08 | N     |
| Derived lift coefficient |   0.344 | —     |

---

## 10. Engineering Interpretation

The baseline calculation establishes a physically defined cruise condition before introducing aerodynamic coefficients as model inputs.

The lift coefficient of approximately \(C_L=0.344\) is a **derived quantity**. It results from the aircraft weight, wing area, cruise speed and atmospheric density under the steady, level-flight assumption.

This differs from the original project, where a value of \(C_L=0.6\) was prescribed before calculating lift.

The baseline therefore provides a starting point for investigating how the aircraft's operating condition relates to aerodynamic efficiency and drag.

No drag coefficient has been assumed at this stage. A defensible method for establishing drag data is required before calculating \(C_D\) or carrying out a lift-to-drag optimisation.
