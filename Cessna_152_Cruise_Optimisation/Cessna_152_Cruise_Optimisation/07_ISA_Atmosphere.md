# ISA Atmosphere

## Purpose

The purpose of this section is to establish the atmospheric conditions used in the baseline Cessna 152 cruise calculation using a standard-atmosphere model rather than prescribing air density arbitrarily.

The baseline aircraft condition selected for the study is:

- Altitude: 8,000 ft
- Equivalent altitude: 2,438.4 m

Atmospheric density is required because it is used to calculate dynamic pressure:

\[
q = \frac{1}{2}\rho V^2
\]

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

**Standard Atmosphere — Tables and Data for Altitudes to 65,800 Feet**

The NASA reference contains tabulated standard-atmosphere properties over a range of altitudes, including temperature, pressure and density.

**Source:**

[NASA Standard Atmosphere — Tables and Data for Altitudes to 65,800 Feet](https://ntrs.nasa.gov/citations/19930090991)

The relevant data were extracted from the metric standard-atmosphere table in the NASA reference.

---

## Conversion of Cruise Altitude

The Cessna 152 cruise condition selected from the aircraft performance data is:

\[
h = 8000\ ft
\]

The NASA metric table expresses altitude in metres, therefore the altitude is converted using:

\[
h_{m}=h_{ft}\times0.3048
\]

where:

- \(h_m\) = altitude in metres
- \(h_{ft}\) = altitude in feet
- \(0.3048\) = conversion factor from feet to metres

Substituting:

\[
h_m=8000\times0.3048
\]

\[
\boxed{h=2438.4\ m}
\]

The required altitude of 2,438.4 m does not appear directly in the NASA table. The surrounding tabulated values at 2,400 m and 2,450 m are therefore used to determine the atmospheric conditions at the exact cruise altitude.

---

## NASA Atmospheric Data Extraction

The following values were read directly from the NASA standard-atmosphere table.

| Altitude, H (m) | Temperature, t (°C) | Temperature, T (K) | Pressure, p × 10² (mb) |
|---:|---:|---:|---:|
| 2,400 | -0.600 | 272.560 | 75626 |
| 2,450 | -0.925 | 272.235 | 75153 |

These two rows surround the required altitude of 2,438.4 m.

### Interpreting the NASA Pressure Column

The NASA table labels the pressure column as:

\[
p\times10^2
\]

with the unit shown as mb.

The values therefore contain a \(10^2\) scaling factor.

For example, the 2,400 m table value is:

\[
75626\times10^{-2}\ mb
\]

\[
=756.26\ mb
\]

Since:

\[
1\ mb=100\ Pa
\]

the pressure is:

\[
756.26\times100
\]

\[
=75626\ Pa
\]

Therefore, the NASA table value of 75626 corresponds to:

\[
\boxed{756.26\ mb=75626\ Pa}
\]

The same interpretation is applied to the 2,450 m pressure value.

---

## Linear Interpolation Method

The required altitude of 2,438.4 m lies between the two available NASA table values:

\[
2400<2438.4<2450
\]

Because the exact altitude is not directly tabulated, **linear interpolation** is used to estimate the atmospheric properties at 2,438.4 m.

Linear interpolation is a mathematical method for estimating a value between two known data points.

The general equation is:

\[
y=y_1+\frac{x-x_1}{x_2-x_1}(y_2-y_1)
\]

where:

- \(x\) = required value
- \(x_1\) = lower known value
- \(x_2\) = upper known value
- \(y_1\) = value corresponding to \(x_1\)
- \(y_2\) = value corresponding to \(x_2\)

For this calculation:

\[
x=2438.4\ m
\]

\[
x_1=2400\ m
\]

\[
x_2=2450\ m
\]

The same interpolation method is applied separately to pressure and temperature.

---

## Pressure at 8,000 ft

The NASA table gives:

\[
P_1=75626\ Pa
\]

at:

\[
h_1=2400\ m
\]

and:

\[
P_2=75153\ Pa
\]

at:

\[
h_2=2450\ m
\]

Using the linear interpolation equation:

\[
P=P_1+\frac{h-h_1}{h_2-h_1}(P_2-P_1)
\]

Substituting:

\[
P=75626+
\frac{2438.4-2400}{2450-2400}
(75153-75626)
\]

First, determine the position of 2,438.4 m between the two tabulated altitudes:

\[
\frac{2438.4-2400}{2450-2400}
=
\frac{38.4}{50}
=
0.768
\]

Therefore:

\[
P=75626+0.768(75153-75626)
\]

\[
P=75626+0.768(-473)
\]

\[
P=75262.736\ Pa
\]

Therefore, the interpolated atmospheric pressure at the selected cruise altitude is approximately:

\[
\boxed{P=75263\ Pa}
\]

or:

\[
\boxed{P=75.263\ kPa}
\]

---

## Temperature at 8,000 ft

The NASA table gives:

\[
t_1=-0.600^\circ C
\]

at 2,400 m and:

\[
t_2=-0.925^\circ C
\]

at 2,450 m.

The same linear interpolation method is used:

\[
t=t_1+\frac{h-h_1}{h_2-h_1}(t_2-t_1)
\]

Substituting:

\[
t=-0.600+
\frac{2438.4-2400}{2450-2400}
(-0.925-(-0.600))
\]

\[
t=-0.600+0.768(-0.325)
\]

\[
\boxed{t=-0.8496^\circ C}
\]

The temperature therefore becomes approximately:

\[
\boxed{t=-0.850^\circ C}
\]

---

## Conversion from Celsius to Kelvin

The ideal gas relationship requires absolute temperature in Kelvin.

The conversion is:

\[
T(K)=t(^\circ C)+273.160
\]

Therefore:

\[
T=-0.8496+273.160
\]

\[
\boxed{T=272.3104\ K}
\]

---

## Density Calculation

Air density is calculated from pressure and absolute temperature using the ideal gas relationship:

\[
\boxed{\rho=\frac{p}{RT}}
\]

where:

- \(\rho\) = air density (kg/m³)
- \(p\) = atmospheric pressure (Pa)
- \(R\) = specific gas constant for dry air, \(287.05\ J/(kg\cdot K)\)
- \(T\) = absolute temperature (K)

Using the interpolated NASA atmospheric conditions:

\[
p=75262.736\ Pa
\]

\[
T=272.3104\ K
\]

Therefore:

\[
\rho=
\frac{75262.736}
{287.05(272.3104)}
\]

\[
\boxed{\rho\approx0.96285\ kg/m^3}
\]

For subsequent aircraft calculations, this can be rounded to:

\[
\boxed{\rho=0.963\ kg/m^3}
\]

This value is therefore derived from the standard-atmosphere pressure and temperature rather than prescribed as an arbitrary input.

---

## Why Atmospheric Density is Required

Dynamic pressure is calculated using:

\[
q=\frac{1}{2}\rho V^2
\]

Therefore, the atmospheric density directly affects the calculated dynamic pressure.

Dynamic pressure is then used to determine the aerodynamic lift required for the aircraft's cruise condition:

\[
L=qSC_L
\]

Rearranging gives:

\[
C_L=\frac{L}{qS}
\]

The atmospheric calculation therefore forms an important part of the overall aircraft-performance methodology.

---

## Calculation Sequence

The atmospheric calculation forms the following part of the overall engineering methodology:

**Selected aircraft cruise altitude**

↓

**Convert 8,000 ft to 2,438.4 m**

↓

**NASA standard-atmosphere table**

↓

**Extract surrounding atmospheric data**

↓

**Linear interpolation**

↓

**Pressure and temperature at 2,438.4 m**

↓

**Ideal gas relationship**

\[
\rho=\frac{p}{RT}
\]

↓

**Air density**

\[
\rho\approx0.963\ kg/m^3
\]

↓

**Dynamic pressure**

\[
q=\frac{1}{2}\rho V^2
\]

↓

**Required lift and derived lift coefficient**

\[
L=W
\]

\[
C_L=\frac{L}{qS}
\]

This provides a traceable link between the selected aircraft operating condition, the published standard-atmosphere data and the aerodynamic calculations that follow.

---

## Source

NASA Technical Reports Server.

*Standard Atmosphere — Tables and Data for Altitudes to 65,800 Feet.*

[NASA Standard Atmosphere Reference](https://ntrs.nasa.gov/citations/19930090991)
