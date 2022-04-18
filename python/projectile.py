# Given a projectile of some mass, initial velocity,
# calculates the kinetic energy, potential energy, and total energy of the projectile over time
# one dimension

from python.energy import kinetic_energy, gravitational_potential_energy
import numpy as np
import matplotlib.pyplot as plt
from urllib import request


def calculate_all_energies(initial_velocity, initial_height, gravitational_acceleration, mass):
    # t_f = v_0 / g + sort(v_0^2 + g y_0) /g
    final_time = (initial_velocity / gravitational_acceleration) \
                 + np.sqrt(
        initial_velocity ** 2 + gravitational_acceleration * initial_height) / gravitational_acceleration
    # t = [0, t_f]
    times = np.linspace(0., final_time)
    # h = h(t)
    heights = height(times, initial_height, initial_velocity, -gravitational_acceleration)
    # v = v(t)
    velocities = velocity(times, initial_velocity, -gravitational_acceleration)
    #
    kinetic_energies = kinetic_energy(mass, velocities)
    potential_energies = gravitational_potential_energy(mass, heights,
                                                        gravitational_acceleration=gravitational_acceleration)
    total_energies = kinetic_energies + potential_energies

    return times, [kinetic_energies, potential_energies, total_energies]


def height(time, initial_height, initial_velocity, acceleration):
    final_height = initial_height + initial_velocity * time + 0.5 * acceleration * time ** 2
    return final_height


def velocity(time, initial_velocity, acceleration):
    final_velocity = initial_velocity + time * acceleration
    return final_velocity


def plot_all_energies(all_energies, times, planet=''):
    plt.plot(times, all_energies[0], color='red', label=r'$T$')
    plt.plot(times, all_energies[1], color='green', label=r'$U$')
    plt.plot(times, all_energies[2], color='black', label=r'$E$')
    plt.xlabel(r'$t$ (s)')
    plt.ylabel(r'$E, T, U$ (J)')
    if len(planet) > 0:
        plt.text(np.mean(times), 0.5*np.mean(all_energies[2]), planet, fontsize=18)
    plt.legend()
    plt.show()

    return

# Parameters


projectile_mass = 2.0  # kg
projectile_initial_velocity = 3.0  # m/s
projectile_initial_height = 5.0  # m
standard_gravity = 9.80665  # m/s

planetary_data = {
    'Earth': {'surface acceleration': 9.80665, 'radius': 6.3568e6},
    'Mars': {'surface acceleration': 3.71, 'radius': 3.3962e6},
}

# url = 'https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.htm'
url = 'http://www.python.org'
with request.urlopen(url) as file:
    print(file.read())


# for planet in planetary_data:
#     acceleration = planetary_data[planet]['surface acceleration']
#     times, energies = calculate_all_energies(projectile_initial_velocity, projectile_initial_height,
#                                              acceleration, projectile_mass)
#     plot_all_energies(energies, times, planet=planet)

