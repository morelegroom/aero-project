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

# Aerodynamic Optimisation Results

## Purpose

The optimisation approach defined in Section 08 was implemented by varying angle of attack while maintaining the selected baseline flight condition.

The aerodynamic response was evaluated using NASA FoilSim, with the following inputs held constant:

| Parameter |                          Value |
| --------- | -----------------------------: |
| Airspeed  | 123 mph (approximately 107 kt) |
| Altitude  |                       8,000 ft |
| Wing area |                      159.5 ft² |
| Camber    |                             0% |
| Thickness |                            12% |

Angle of attack was varied between 0° and 6°.

The resulting lift, drag, lift coefficient and drag coefficient were recorded for each condition.

The model is a simplified aerodynamic representation and the camber and thickness inputs should therefore be treated as modelling assumptions rather than an exact representation of the Cessna 152 wing geometry.

---

## Angle of Attack Sweep

The results obtained from the aerodynamic model are shown below.

| Angle of Attack | Lift (lb) |     CL | Drag (lb) |     CD |       L/D |
| --------------: | --------: | -----: | --------: | -----: | --------: |
|              0° |         0 | 0.0000 |        67 | 0.0158 |         — |
|              2° |     1,161 | 0.2394 |       110 | 0.0228 |     10.50 |
|              3° |     1,725 | 0.3556 |       144 | 0.0297 |     11.97 |
|              4° |     2,278 | 0.4695 |       189 | 0.0389 | **12.07** |
|              5° |     2,820 | 0.5812 |       244 | 0.0503 |     11.56 |
|              6° |     3,361 | 0.6907 |       311 | 0.0641 |     10.77 |

At 0° angle of attack, the model produces zero lift, so an L/D value is not considered meaningful for the purpose of this comparison.

---

## Lift-to-Drag Ratio

Aerodynamic efficiency was evaluated using:

$$
L/D = \frac{C_L}{C_D}
$$

The calculated values show that aerodynamic efficiency increased between 2° and 4° angle of attack:

* 2° → L/D ≈ 10.50
* 3° → L/D ≈ 11.97
* 4° → L/D ≈ 12.07

Beyond 4°, the lift-to-drag ratio decreased:

* 5° → L/D ≈ 11.56
* 6° → L/D ≈ 10.77

The **highest measured L/D within the tested range was approximately 12.07 at 4° angle of attack**.

This identifies 4° as the highest-efficiency point measured in this particular sweep.

It does not establish 4° as the exact optimum for the real Cessna 152. The result is dependent on the selected flight condition, the simplified aerodynamic model and the discrete angle-of-attack points tested.

---

## Lift Response

Lift increased with angle of attack throughout the tested range.

The model produced:

* 1,161 lb of lift at 2°
* 1,725 lb at 3°
* 2,278 lb at 4°
* 2,820 lb at 5°
* 3,361 lb at 6°

This demonstrates the expected relationship between increasing angle of attack and increasing lift within the range investigated.

However, the increase in lift was accompanied by an increase in drag.

---

## Drag Response

Drag increased progressively as angle of attack increased.

The calculated drag increased from:

* 110 lb at 2°
* 144 lb at 3°
* 189 lb at 4°
* 244 lb at 5°
* 311 lb at 6°

The increase in drag becomes increasingly significant at the higher angles of attack.

This explains why the lift-to-drag ratio does not continue increasing despite the continued increase in lift.

The results therefore demonstrate the trade-off identified in Section 08:

**Increasing angle of attack → increased lift → increased drag → changing aerodynamic efficiency**

---

## Graphical Results

The numerical results were plotted to make the relationships between angle of attack and aerodynamic performance easier to interpret.

### Lift-to-Drag Ratio

The L/D plot is the primary optimisation result because it directly represents the aerodynamic efficiency measure selected in Section 08.

![Lift-to-Drag Ratio against Angle of Attack](results/aoa_vs_ld.png)

The plot shows the increase in aerodynamic efficiency up to the 4° test point, followed by a reduction at higher angles of attack.

### Lift

![Lift against Angle of Attack](results/aoa_vs_lift.png)

The lift plot shows the increase in generated lift as angle of attack increases.

### Drag

![Drag against Angle of Attack](results/aoa_vs_drag.png)

The drag plot shows the corresponding increase in aerodynamic drag.

---

## Reference Weight Comparison

The aerodynamic results can also be compared with the 1,670 lb maximum gross weight reference value used for the aircraft.

The model produces:

* 1,161 lb of lift at 2°
* 1,725 lb of lift at 3°

Therefore, the 1,670 lb reference weight lies between the two measured points.

Assuming a locally linear relationship between these two points, the corresponding angle of attack can be estimated by interpolation:

$$
\alpha =
2 +
\frac{1670-1161}{1725-1161}
(3-2)
$$

which gives:

$$
\alpha \approx 2.9^\circ
$$

The corresponding interpolated aerodynamic coefficients are approximately:

$$
C_L \approx 0.344
$$

$$
C_D \approx 0.029
$$

giving:

$$
L/D \approx 11.86
$$

This is an interpolation between the 2° and 3° model results rather than a directly simulated FoilSim result.

The calculation provides a useful connection between the aerodynamic sweep and the aircraft weight constraint.

It is important to distinguish this result from the 4° efficiency result:

* **Approximately 2.9°** is the interpolated angle at which the model produces approximately the 1,670 lb reference lift.
* **4°** is the point with the highest measured L/D within the tested angle-of-attack range.

These represent two different aspects of the optimisation problem.

---

## Interpretation

The results demonstrate that maximising lift alone does not maximise aerodynamic efficiency.

As angle of attack increases, the model produces progressively more lift, but it also produces progressively more drag.

The highest measured L/D occurs at 4°, after which the increase in drag causes aerodynamic efficiency to decrease.

The weight comparison provides a separate operating constraint. Using the 1,670 lb maximum gross weight as a reference, the model reaches the required lift between the 2° and 3° test points, with linear interpolation giving approximately 2.9°.

The analysis therefore demonstrates the interaction between:

**Aircraft weight → required lift → angle of attack → drag → aerodynamic efficiency**

Rather than defining a single optimum in advance, the study uses the model results to identify how the competing requirements change across the tested operating range.

# Discussion

## Interpretation of the Results

The aerodynamic sweep demonstrates the trade-off between lift generation and drag production as angle of attack is increased.

Across the tested range, lift increased continuously with angle of attack. However, drag also increased, meaning that additional lift was accompanied by an increasing aerodynamic penalty.

The lift-to-drag ratio provides a way of considering these competing effects simultaneously.

Within the discrete points tested, the highest measured L/D was approximately 12.07 at 4° angle of attack. At higher angles of attack, L/D decreased despite the continued increase in lift.

This demonstrates that the angle producing the greatest lift is not necessarily the angle producing the greatest aerodynamic efficiency.

## Relationship Between Required Lift and Efficiency

The reference weight comparison provides a second constraint on the optimisation problem.

Using the 1,670 lb maximum gross weight as a reference, the aerodynamic model produces less than the reference weight at 2° and slightly more than the reference weight at 3°.

Linear interpolation between these points gives an estimated angle of attack of approximately 2.9° for 1,670 lb of lift.

This result should not be interpreted as the actual cruise angle of attack of the Cessna 152. It is an interpolated result from the simplified aerodynamic model under the selected test conditions.

The comparison nevertheless demonstrates how an aerodynamic model can be combined with an aircraft-level constraint such as weight.

## Optimisation as a Trade-off

The results show why the optimisation problem cannot be reduced to simply maximising lift.

At higher angles of attack:

**Angle of attack increases → lift increases → drag increases → L/D eventually decreases**

The analysis therefore considers aerodynamic performance as a trade-off between competing quantities.

For the sampled conditions, the 4° test point produced the highest measured L/D, while approximately 2.9° represented the interpolated point associated with the selected 1,670 lb reference lift.

These are different engineering conditions and should not be treated as a single optimum.

## Engineering Significance

The study demonstrates a simplified example of how an aircraft performance problem can be approached using a defined baseline condition, physical constraints and a parameter sweep.

The process can be represented as:

**Aircraft reference data → Flight condition → Atmospheric conditions → Aerodynamic model → Parameter sweep → Performance comparison**

This approach is more representative of an engineering analysis than simply selecting aerodynamic coefficients and plotting their mathematical relationships.

The project also demonstrates the importance of distinguishing between a model result and a real-world aircraft characteristic. The calculated results are meaningful within the assumptions and operating conditions used, but they should not be treated as direct measurements of the Cessna 152.

## Relevance to Further Modelling

The current analysis provides a baseline for more detailed aerodynamic modelling.

A future model could replace the simplified FoilSim representation with aircraft-specific aerodynamic data or a more detailed aerodynamic method.

This could allow the effect of additional variables to be investigated, such as:

* Aircraft weight
* Altitude
* Airspeed
* Wing geometry
* Reynolds number
* Mach number
* Angle of attack
* Aircraft configuration

The same general methodology could then be extended from a simple parameter sweep towards a more detailed aircraft performance or modelling-and-simulation study.

 
