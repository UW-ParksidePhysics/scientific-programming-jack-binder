# Calculate kinetic energy and potential energies
# (one-dimensional, one particle)

import numpy as np


def kinetic_energy(mass, velocity):
    """
    T = (1/2)m/^2
    :return: T (float)
    """
    kinetic = 0.5 * mass * velocity**2
    return kinetic


def gravitational_potential_energy(mass, height, gravitational_acceleration=9.80665):
    """
    U_g = m g h
    :param mass: (float) Mass of object in kilograms
    :param height: (float) Height of object above ground in meters
    :param gravitational_acceleration: (float) Acceleration due to gravity in meters per second_square
    :return: U_g (float) Gravitational potential energy (near surface of a large body
    """
    potential_energy = mass * gravitational_acceleration * height
    return potential_energy


if __name__ == '__main__':
    print('Running energy.py as its own script...')
    test_mass = 2.0  # kg
    test_speed = 3.0  # m/s
    test_kinetic_energy = kinetic_energy(test_mass, test_speed)
    # 0.5 * 2.0 * 3.0^2 = 9 J
    print(f'T({test_mass:.0f} kg, {test_speed:.0f} m/s) = {test_kinetic_energy:.1f} J')

    test_height = 5.0  # m
    test_potential_energy = gravitational_potential_energy(test_mass, test_height)
    # 2.0 * 9.80665 * 5.0 = 98.0665 J
    print(f'U({test_mass:.0f} kg, {test_height:.0f} m) = {test_potential_energy:.1f} J')

