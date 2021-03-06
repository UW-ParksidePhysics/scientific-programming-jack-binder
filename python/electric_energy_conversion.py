import numpy as np
import matplotlib.pyplot as plt
# I propose to solve the problem of determining how much electrical energy
# is converted into thermal energy inside a variety of wire sizes under a
# certain time period. The reason why this problem interests me is that
# I'm fascinated by energy conversion and the idea of using it to create a
# more sustainable and practical world. In energy conversion, the variables
# needed are current density, radius of the wire, potential, and time. The
# main physical principle in this problem is energy conversion. The
# function needed for this program to operate correctly is an equation that
# can pull and use at least one input value from a table and then
# correctly calculate the equation. The vector quantity in this problem
# would be the current density. I will read in a data table that has many
# difference radii values of wires, and I  will have to pull each one into
# the formula. I can visualize this problem through a graph of energy
# converted vs radius.


def initialize_parameters():
    # Parameters
    current_density = 10.0
    voltage = 2  # volts
    time = 120.0  # sec
    return current_density, voltage, time


def read_wire_date():
    # Pulls table from website
    # Pulls column from table and coverts it to an array
    diameter_mm = []
    with open("wireGauges.txt") as file:
        for line in file:
            if len(line.split()) > 2:
                diam = float(line.split()[2])
                diameter_mm.append(diam)
    diameter_mm = np.array(diameter_mm)
    # Finds radius
    radii_mm = diameter_mm / 2
    # Converts radii from mm to m
    radii_m = radii_mm * 0.001
    return radii_m


def calculate_energy(radii_m, time=120, voltage=2.0, current_density=10.0):
    # Equation to find current
    # i = int(J*dA)
    # i = int(J*2*pi*r)
    # i = J*2*pi*int(r)
    # i = J*2*pi*((r^2)/2)
    # i = [(J*2*pi)/2]*(r^2)

    # Finding the constant value
    # The constant = (J*2*pi)/2
    constant = (current_density * 2 * np.pi) / 2

    # Creates matrix of radii^2
    radii_squared = radii_m ** 2

    # Creates matrix of current values
    current = constant * radii_squared

    # Creates matrix of energy values
    # energy converted = voltage * time * current
    converted_energy = (voltage * time) * current
    return converted_energy


def plot_data(radii_m, converted_energy):
    # creates graph
    plt.scatter(radii_m, converted_energy, label='Radii')
    plt.plot(radii_m, converted_energy)
    plt.title("Amount of Electrical Energy Converted to Thermal Energy")
    plt.xlabel('Radii(m)')
    plt.ylabel('Thermal Energy Converted (J)')
    plt.legend(loc="upper left")
    plt.show()
    return


if __name__ == "__main__":
    radii = read_wire_date()
    parameters = initialize_parameters()
    energy = calculate_energy(radii)
    plot_data(radii, energy)
else:
    print("Something went wrong")
