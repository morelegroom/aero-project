import numpy as np
import matplotlib.pyplot as plt

S = 20
Cl = 0.6
Cd = 0.03
a = 343

rho_sea = 1.225
rho_alt = 0.9

velocities = np.linspace(30, 250, 100)

lift_sea = []
drag_sea = []
lift_alt = []
mach = []

for V in velocities:
    lift_sea.append(0.5 * rho_sea * V**2 * S * Cl)
    drag_sea.append(0.5 * rho_sea * V**2 * S * Cd)
    lift_alt.append(0.5 * rho_alt * V**2 * S * Cl)
    mach.append(V / a)

plt.figure()
plt.plot(velocities, lift_sea)
plt.title("Lift vs Velocity (Sea Level)")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Lift (N)")
plt.grid()
plt.savefig("lift.png")

plt.figure()
plt.plot(velocities, drag_sea)
plt.title("Drag vs Velocity (Sea Level)")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag (N)")
plt.grid()
plt.savefig("drag.png")

plt.figure()
plt.plot(velocities, mach)
plt.axhline(1, linestyle="--")
plt.title("Mach Number vs Velocity")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Mach number")
plt.grid()
plt.savefig("mach.png")

plt.figure()
plt.plot(velocities, lift_sea, label="Sea Level")
plt.plot(velocities, lift_alt, label="Altitude")
plt.title("Lift vs Velocity (Altitude Effect)")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Lift (N)")
plt.legend()
plt.grid()
plt.savefig("altitude.png")

print("Done! Plots created.")
