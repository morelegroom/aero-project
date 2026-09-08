# Engineering Equations

## Purpose

This document defines the equations used to establish the baseline cruise condition for the Cessna 152.

The calculations will use SI units. Aircraft data published in imperial aviation units will therefore be converted before being substituted into the equations.

---

## 1. Mass Conversion

The aircraft mass is initially provided in pounds.

### Equation

$$
m_{kg}=m_{lb}\times0.453592
$$

where:

* \(m_{kg}\) = mass in kilograms (kg)
* \(m_{lb}\) = mass in pounds (lb)

---

## 2. Aircraft Weight

Aircraft weight is calculated from mass using gravitational acceleration.

### Equation

$$
W=mg
$$

where:

* \(W\) = aircraft weight (N)
* \(m\) = aircraft mass (kg)
* \(g\) = gravitational acceleration (9.81 m/s²)

---

## 3. Speed Conversion

The published cruise speed is given in knots.

### Equation

$$
V_{m/s}=V_{kt}\times0.514444
$$

where:

* \(V_{m/s}\) = velocity in metres per second (m/s)
* \(V_{kt}\) = velocity in knots (kt)

---

## 4. Wing Area Conversion

The published wing area is given in square feet.

### Equation

$$
S_{m^2}=S_{ft^2}\times0.092903
$$

where:

* \(S_{m^2}\) = wing area in square metres (m²)
* \(S_{ft^2}\) = wing area in square feet (ft²)

---

## 5. Dynamic Pressure

Dynamic pressure represents the pressure associated with the aircraft's motion through the air.

### Equation

$$
q=\frac{1}{2}\rho V^2
$$

where:

* \(q\) = dynamic pressure (Pa)
* \(\rho\) = air density (kg/m³)
* \(V\) = aircraft velocity (m/s)

---

## 6. Lift Equation

The aerodynamic lift force is described by:

### Equation

$$
L=\frac{1}{2}\rho V^2SC_L
$$

where:

* \(L\) = lift force (N)
* \(\rho\) = air density (kg/m³)
* \(V\) = aircraft velocity (m/s)
* \(S\) = wing reference area (m²)
* \(C_L\) = lift coefficient

For this project, \(C_L\) will not initially be prescribed as an arbitrary input. It will be derived from the defined aircraft and flight condition.

---

## 7. Lift Coefficient

Once the required lift, air density, velocity and wing area have been established, the lift coefficient can be derived.

### Equation

$$
C_L=\frac{L}{\frac{1}{2}\rho V^2S}
$$

or, using dynamic pressure:

$$
C_L=\frac{L}{qS}
$$

where:

* \(C_L\) = lift coefficient
* \(L\) = lift force (N)
* \(q\) = dynamic pressure (Pa)
* \(S\) = wing reference area (m²)

---

## 8. Steady, Level Flight Condition

For the baseline cruise condition, the aircraft is assumed to be in steady, level flight.

Therefore, the vertical forces are approximately balanced:

$$
L=W
$$

This allows the required lift to be established from the calculated aircraft weight.

---

## 9. Horizontal Force Balance

For steady cruise flight, the horizontal forces are approximately balanced:

$$
T=D
$$

where:

* \(T\) = thrust (N)
* \(D\) = drag (N)

A realistic drag value has not yet been prescribed. A suitable method for establishing drag data will be investigated before calculating \(C_D\).

---

## 10. Drag Equation

The standard drag relationship is:

$$
D=\frac{1}{2}\rho V^2SC_D
$$

where:

* \(D\) = drag force (N)
* \(\rho\) = air density (kg/m³)
* \(V\) = aircraft velocity (m/s)
* \(S\) = wing reference area (m²)
* \(C_D\) = drag coefficient

The drag coefficient will only be introduced once a defensible source or method for determining drag has been established.

---

## Calculation Sequence

The baseline calculation will follow this sequence:

$$
\text{Aircraft Data}
$$

$$
\downarrow
$$

$$
\text{Unit Conversions}
$$

$$
\downarrow
$$

$$
\text{Atmospheric Conditions}
$$

$$
\downarrow
$$

$$
\text{Aircraft Weight}
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
\text{Required Lift}
$$

$$
\downarrow
$$

$$
\text{Derived } C_L
$$

This sequence ensures that aerodynamic quantities are derived from the defined aircraft and flight condition rather than being arbitrarily prescribed.
