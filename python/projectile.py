# Given a projectile of some mass, initial velocity,
# calculates the kinetic energy, potential energy, and total energy of the projectile over time
# one dimension

from python.energy import kinetic_energy, gravitational_potential_energy
import numpy as np
import matplotlib.pyplot as plt

projectile_mass = 2.0  # kg
projectile_initial_velocity = 3.0  # m/s
projectile_initial_height = 5.0  # m
standard_gravity = 9.80665  # m/s

# t_f = v_0 / g + sort(v_0^2 + g y_0) /g
final_time = (projectile_initial_velocity / standard_gravity) \
            + np.sqrt(projectile_initial_velocity**2 + standard_gravity*projectile_initial_height) / standard_gravity

# print(f't_f(y0 = {projectile_initial_height:.0f} m, v0 = {projectile_initial_velocity} m/s) = {final_time:.02f} s')

times = np.linspace(0., final_time)
# print(times)
# print(len(times))
# print(type(times))


def height(time, initial_height, initial_velocity, acceleration):
    final_height = initial_height + initial_velocity*time + 0.5 * acceleration * time**2
    return final_height

# time = 1.0 s, initial_height = 0.0, initial_velocity = 0.0, acceleration = -9.8 m/s^2
# height = 0 + 0*1 + 0.5 (-9.8) * 1^2 = -4.9 m/s^2


test_height = height(1.0, 0.0, 0.0, -9.8)
print(f'h = {test_height:.1f} m')

heights = height(times, projectile_initial_height, projectile_initial_velocity, -standard_gravity)
print(f'h_f = {heights[-1]:.1f} m')


def velocity (time, initial_velocity, acceleration):
    final_velocity = initial_velocity + time * acceleration
    return final_velocity


velocities = velocity(times, projectile_initial_velocity, -standard_gravity)
kinetic_energies = kinetic_energy(projectile_mass, velocities)
potential_energies = gravitational_potential_energy(projectile_mass, heights, gravitational_acceleration=standard_gravity)
total_energies = kinetic_energies + potential_energies

plt.plot(times, kinetic_energies, color='red', label=r'$T$')
plt.plot(times, potential_energies, color='green', label=r'$U$')
plt.plot(times, total_energies, color='black', label=r'$E$')
plt.xlabel(r'$t$ (s)')
plt.ylabel(r'$E, T, U$ (J)')
plt.legend()
plt.show()
