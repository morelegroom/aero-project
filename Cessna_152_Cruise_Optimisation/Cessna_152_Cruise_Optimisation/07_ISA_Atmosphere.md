# ISA Atmospheric Conditions

## Purpose

The baseline cruise calculation requires the air density at the selected cruise altitude.

Rather than prescribing an arbitrary air-density value, the atmospheric condition is established using the **International Standard Atmosphere (ISA)** model.

ISA provides a standardised representation of atmospheric properties, including temperature, pressure and density, as a function of altitude.

---

## Baseline Altitude

The selected cruise altitude is:

$$
h=8000\ ft
$$

Converting to metres:

$$
h=8000\times0.3048
$$

$$
\boxed{h=2438.4\ m}
$$

---

## ISA Air Density

At an altitude of approximately 2438 m under ISA conditions, the air density is approximately:

$$
\boxed{\rho\approx0.963\ kg/m^3}
$$

This value is used in the baseline cruise calculation.

---

## Why Air Density Is Required

Air density is an important variable in the aerodynamic force equations.

The dynamic pressure is given by:

$$
q=\frac{1}{2}\rho V^2
$$

Therefore, for a given aircraft velocity, a change in air density changes the dynamic pressure acting on the aircraft.

Lift is then calculated or related through:

$$
L=qSC_L
$$

or:

$$
L=\frac{1}{2}\rho V^2SC_L
$$

Consequently, establishing the atmospheric condition is necessary before deriving aerodynamic quantities such as the lift coefficient.

---

## Atmospheric Assumption

The baseline calculation assumes:

* International Standard Atmosphere (ISA)
* Altitude = 8000 ft
* No deviation from standard atmospheric conditions
* Constant atmospheric properties for the defined baseline flight condition

This provides a consistent reference condition for the initial analysis.

---

## Relationship to the Baseline Calculation

The calculation sequence is:

$$
\text{Cruise Altitude}
$$

$$
\downarrow
$$

$$
\text{ISA Atmospheric Conditions}
$$

$$
\downarrow
$$

$$
\text{Air Density}
$$

$$
\downarrow
$$

$$
\text{Dynamic Pressure}
$$

$$
\downarrow
$$

$$
\text{Required Lift and Derived }C_L
$$

The air density of approximately \(0.963\ kg/m^3\) was therefore not selected arbitrarily. It is associated with the defined 8000 ft cruise condition under the ISA assumption.
