# ISA Atmosphere

## Purpose

The purpose of this section is to establish the atmospheric conditions used in the baseline Cessna 152 cruise calculation using a standard-atmosphere model rather than prescribing air density arbitrarily.

The baseline aircraft condition selected for the study is:

- Altitude: 8,000 ft
- Equivalent altitude: 2,438.4 m

Atmospheric density is required because it is used to calculate dynamic pressure:

q = 0.5 ρV²

Dynamic pressure is subsequently used in the lift equation and in the calculation of the lift coefficient.

---

## What is ISA?

ISA stands for **International Standard Atmosphere**.

It is a standard atmospheric model used to define atmospheric properties as a function of altitude. These properties include:

- Temperature
- Pressure
- Air density
- Speed of sound

Using a standard atmosphere provides a defined and reproducible atmospheric condition rather than selecting an arbitrary value for air density.

---

## Reference Data

The atmospheric data used in this analysis are taken from the NASA publication:

**Standard Atmosphere – Tables and Data for Altitudes to 65,800 Feet**

The NASA reference contains tabulated standard-atmosphere properties over a range of altitudes, including temperature, pressure and density.

Source:

NASA Standard Atmosphere – Tables and Data for Altitudes to 65,800 Feet

https://ntrs.nasa.gov/citations/19930090991

The relevant data were extracted from the metric standard-atmosphere table in the NASA reference.

---

## Conversion of Cruise Altitude

The Cessna 152 cruise condition selected from the aircraft performance data is:

h = 8000 ft

The NASA metric table expresses altitude in metres, therefore the altitude is converted using:

h(m) = h(ft) × 0.3048

where:

- h(m) = altitude in metres
- h(ft) = altitude in feet
- 0.3048 = conversion factor from feet to metres

Substituting:

h(m) = 8000 × 0.3048

h = 2438.4 m

The required altitude of 2,438.4 m does not appear directly in the NASA table. The surrounding tabulated values at 2,400 m and 2,450 m are therefore used to determine the atmospheric conditions at the exact cruise altitude.

---

## NASA Atmospheric Data Extraction

The following values were extracted directly from the NASA standard-atmosphere table.

| Altitude H (m) | Temperature t (°C) | Temperature T (K) | Pressure P × 10² (mb) |
|---------------:|-------------------:|------------------:|----------------------:|
| 2400 | -0.600 | 272.560 | 75626 |
| 2450 | -0.925 | 272.235 | 75153 |

These two rows surround the required altitude of 2438.4 m.

---

## Interpreting the NASA Pressure Column

The NASA table labels the pressure column as:

P × 10² (mb)

This means the pressure values have been scaled by a factor of 100.

For example:

75626

corresponds to:

756.26 mb

Since:

1 mb = 100 Pa

Therefore:

756.26 × 100 = 75,626 Pa

The same interpretation is applied to the remaining pressure values used in this analysis.

---

## Linear Interpolation Method

The required altitude lies between the two available NASA table values:

2400 m < 2438.4 m < 2450 m

Because the exact altitude is not tabulated, linear interpolation is used to estimate the atmospheric properties at 2438.4 m.

The general interpolation equation is:

y = y₁ + ((x − x₁)/(x₂ − x₁)) × (y₂ − y₁)

where:

- x = required altitude
- x₁ = lower tabulated altitude
- x₂ = upper tabulated altitude
- y₁ = value at x₁
- y₂ = value at x₂

The same method is applied to pressure and temperature.

---

## Pressure at 8,000 ft

NASA table values:

- P₁ = 75,626 Pa at 2400 m
- P₂ = 75,153 Pa at 2450 m

Interpolation equation:

P = P₁ + ((h − h₁)/(h₂ − h₁)) × (P₂ − P₁)

Substituting:

P = 75626 + ((2438.4 − 2400)/(2450 − 2400)) × (75153 − 75626)

P = 75626 + (38.4 / 50) × (-473)

P = 75626 + 0.768 × (-473)

P = 75,262.7 Pa

Therefore:

P ≈ 75.263 kPa

Pressure decreases with increasing altitude. The interpolated value therefore lies between the two NASA tabulated values, which provides confidence that the result is physically reasonable.

---

## Temperature at 8,000 ft

NASA table values:

- t₁ = -0.600 °C at 2400 m
- t₂ = -0.925 °C at 2450 m

Interpolation equation:

t = t₁ + ((h − h₁)/(h₂ − h₁)) × (t₂ − t₁)

Substituting:

t = -0.600 + ((2438.4 − 2400)/(2450 − 2400)) × (-0.925 − (-0.600))

t = -0.600 + 0.768 × (-0.325)

t = -0.8496 °C

Therefore:

t ≈ -0.850 °C

The interpolated temperature also lies between the two NASA tabulated values and follows the expected reduction in temperature with increasing altitude.

---

## Conversion from Celsius to Kelvin

The ideal gas relationship requires absolute temperature in Kelvin.

T(K) = t(°C) + 273.160

Substituting:

T = -0.8496 + 273.160

T = 272.3104 K

---

## Density Calculation

Air density is calculated using the ideal gas relationship:

ρ = p / (R × T)

where:

- ρ = air density (kg/m³)
- p = atmospheric pressure (Pa)
- R = specific gas constant for dry air (287.05 J/kg·K)
- T = absolute temperature (K)

Substituting:

ρ = 75262.7 / (287.05 × 272.3104)

ρ = 0.96285 kg/m³

Therefore:

ρ ≈ 0.963 kg/m³

This value is derived from the NASA standard-atmosphere pressure and temperature data rather than prescribed as an arbitrary input.

---

## Why Atmospheric Density is Required

Dynamic pressure is calculated using:

q = 0.5 ρV²

The atmospheric density therefore directly affects the calculated dynamic pressure.

Dynamic pressure is then used within the lift equation:

L = qSCL

Rearranging:

CL = L / (qS)

The atmospheric calculation therefore forms an important part of the overall aircraft-performance methodology.

---

## Calculation Sequence

Selected cruise altitude

↓

8,000 ft

↓

Convert to metres

↓

2438.4 m

↓

NASA Standard Atmosphere Table

↓

Extract surrounding atmospheric data

↓

Linear interpolation

↓

Pressure at 2438.4 m

↓

Temperature at 2438.4 m

↓

Density calculation

ρ = p / (R × T)

↓

ρ ≈ 0.963 kg/m³

↓

Dynamic pressure

q = 0.5 ρV²

↓

Lift coefficient

CL = L / (qS)

---

## Source

NASA Technical Reports Server

*Standard Atmosphere – Tables and Data for Altitudes to 65,800 Feet*

https://ntrs.nasa.gov/citations/19930090991
