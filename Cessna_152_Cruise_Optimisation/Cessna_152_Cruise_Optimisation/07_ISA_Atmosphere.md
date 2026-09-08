# ISA Atmosphere

## Purpose

The purpose of this section is to establish the atmospheric conditions used in the baseline Cessna 152 cruise calculation using a standard-atmosphere model rather than prescribing air density arbitrarily.

The aircraft baseline condition is:

* Altitude: 8,000 ft
* Equivalent altitude: 2,438.4 m

Atmospheric density is required because it is used to calculate dynamic pressure:

$$
q = \frac{1}{2}\rho V^2
$$

which is then used in the lift equation and the calculation of the lift coefficient.

---

## What is ISA?

ISA stands for **International Standard Atmosphere**.

It is a standard model used to define atmospheric properties as a function of altitude. These properties include:

* Temperature
* Pressure
* Air density
* Speed of sound

Using a standard atmosphere allows the aircraft calculation to be performed using a defined and reproducible atmospheric condition rather than selecting an arbitrary value for air density.

---

## Reference Data

The atmospheric conditions used in this analysis are based on published standard-atmosphere data.

The primary reference used is the NASA Technical Reports Server publication:

**Standard Atmosphere — Tables and Data for Altitudes to 65,800 Feet**

The reference contains tabulated standard-atmosphere properties over a range of altitudes, including atmospheric pressure and density.

**NASA reference:**

[NASA Standard Atmosphere — Tables and Data for Altitudes to 65,800 Feet](https://ntrs.nasa.gov/citations/19930090991)

This source provides the atmospheric reference behind the values used in the present calculation.

---

## Atmospheric Conditions at 8,000 ft

For the baseline cruise condition, the aircraft is assumed to be operating at 8,000 ft under standard-atmosphere conditions.

The corresponding atmospheric conditions are approximately:

| Parameter   |         Value | Basis                         |
| ----------- | ------------: | ----------------------------- |
| Altitude    |      8,000 ft | Selected cruise condition     |
| Altitude    |     2,438.4 m | Unit conversion               |
| Temperature |       272.3 K | Standard atmosphere           |
| Pressure    |    ≈ 75.3 kPa | Standard atmosphere           |
| Density     | ≈ 0.963 kg/m³ | Standard atmosphere / derived |

The density value is therefore not treated as an arbitrary input. It is associated with the defined standard-atmosphere condition at the selected altitude.

---

## Density Calculation

The relationship between pressure, temperature and density for air can be written as:

$$
\rho = \frac{p}{RT}
$$

where:

* \(\rho\) = air density (kg/m³)
* \(p\) = atmospheric pressure (Pa)
* \(R\) = specific gas constant for dry air, approximately 287.05 J/(kg·K)
* \(T\) = absolute temperature (K)

Using the approximate standard-atmosphere conditions at 8,000 ft:

$$
p \approx 75,300\ Pa
$$

$$
T \approx 272.3\ K
$$

Therefore:

$$
\rho =
\frac{75,300}
{287.05(272.3)}
$$

$$
\rho \approx 0.963\ kg/m^3
$$

This value is subsequently used in the dynamic-pressure calculation.

---

## Why Atmospheric Density is Required

Dynamic pressure is calculated using:

$$
q = \frac{1}{2}\rho V^2
$$

Therefore, the atmospheric density directly affects the calculated dynamic pressure.

Dynamic pressure is then used to determine the aerodynamic lift required for the aircraft's cruise condition:

$$
L = qSC_L
$$

Rearranging gives:

$$
C_L = \frac{L}{qS}
$$

This means that the atmospheric condition forms part of the calculation chain rather than being an independently selected coefficient.

---

## Calculation Sequence

The atmospheric calculation forms the following part of the overall engineering methodology:

**Selected altitude**

↓

**Standard-atmosphere reference**

↓

**Pressure and temperature**

↓

**Air density**

$$
\rho = \frac{p}{RT}
$$

↓

**Dynamic pressure**

$$
q = \frac{1}{2}\rho V^2
$$

↓

**Required lift and derived lift coefficient**

$$
L=W
$$

$$
C_L=\frac{L}{qS}
$$

This approach provides a traceable link between the selected aircraft operating condition and the aerodynamic quantities calculated later in the project.

---

## Source

NASA Technical Reports Server.

*Standard Atmosphere — Tables and Data for Altitudes to 65,800 Feet.*

[NASA Standard Atmosphere Reference](https://ntrs.nasa.gov/citations/19930090991)
