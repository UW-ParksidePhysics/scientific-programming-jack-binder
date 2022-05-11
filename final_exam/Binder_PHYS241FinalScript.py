from two_column_text_read import two_column_text_read
from bivariate_statistics import bivariate_statistics
from quadratic_fit import quadratic_fit
from fit_curve_array import fit_curve_array
from plot_data_with_fit import plot_data_with_fit
from equations_of_state import fit_eos
from convert_units import convert_units
from generate_matrix import generate_matrix
from lowest_eigenvectors import lowest_eigenvectors
from numpy import linspace
import numpy as np
import matplotlib.pyplot as plt

display_graph = True


def parse_file_name(file_name):
    parse = file_name.split(".")
    symbol = parse[0]
    crystal_symbol = parse[1]
    acronym = parse[2]
    return symbol, crystal_symbol, acronym


data_file = "Sn.Fd-3m.GGA-PBE.volumes_energies.dat"
symbol, crystal_symbol, acronym = parse_file_name(data_file)
array = two_column_text_read(data_file)
statistics = bivariate_statistics(array)
quad_coefficients = quadratic_fit(array)
print(quad_coefficients)

#min_x = statistics[2]
#max_x = statistics[3]
undo_array = zip(*array)
array_2 = list(undo_array)
fit_eos_curve, fit_parameters = fit_eos(array[0], array[1], quad_coefficients,
                                        eos='Birch-Murnaghan', number_of_points=50)
bulk_modulus = fit_parameters[1]
equilibrium_volume = fit_parameters[3]


def annotate_graph(symbol, crystal_symbol):
    ax.annotate(symbol, xy=(130, 0.001))
    ax.annotate(r'$ {}\overline{{{}}} {}$'.format(crystal_symbol[0:2], crystal_symbol[3], crystal_symbol[1]), xy=(115,
                                                                                                                  0))
    ax.annotate('K_0={:.6f}GPa'.format(bulk_modulus_gpa), xy=(115, 0.001))
    ax.annotate('V_0={:.3f}A^3/atom'.format(eq_vol), xy=(115, -0.001))
    plt.axvline(eq_vol - array_2[0][array_2[1].index(min(array_2[1]))] * 0.01, color="black", linestyle='-')
    plt.text(91, -0.0025, "created by Jack Binder May/09/22")
    plt.title("{} Equation of State for {} in DFT {}".format('Birch-Murnaghan', symbol, acronym))
    return ax, plt


fig = plt.figure()
ax = fig.add_subplot(111)

volumes = linspace(min(array_2[0]), max(array_2[0]), len(fit_eos_curve))
line1, = ax.plot(array_2[0], array_2[1], 'o')
line2, = ax.plot(volumes, fit_eos_curve, color="blue")

x_min = (min(array_2[0]) - (min(array_2[0]) * 0.10))
x_max = (max(array_2[0]) + (max(array_2[0]) * 0.10))
y_min = (-0.003)
y_max = 0.003

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xlabel(r'$V$ (Å$^3$/atom)')
plt.ylabel(r'$E$ (eV/atom)')
bulk_modulus_gpa = convert_units(bulk_modulus, "rb/cb")
eq_vol = array_2[0][array_2[1].index(min(array_2[1]))]
annotate_graph(symbol, crystal_symbol)

fit_curve = fit_curve_array(quad_coefficients, x_min, x_max, number_of_points=100)
scatter_plot, curve_plot = plot_data_with_fit(array, fit_curve, data_format="bo", fit_format="k")

if display_graph:
    plt.show()
elif not display_graph:
    plt.savefig("Jack.Sn.Fd-3m.GGA-PBEsol.Birch-MurnaghanEquationOfState.png")


# Visualize Vectors in Space
display_graph = False
potential_name = 'harmonic'
N_dim = 100
potential_parameter = 200

matrix = generate_matrix(-10, 10, N_dim, potential_name, potential_parameter)

eigenvalues, eigenvectors = lowest_eigenvectors(matrix, 3)

x = linspace(-10, 10, N_dim)
line1, = plt.plot(x, eigenvectors[1][0:N_dim])
line2, = plt.plot(x, eigenvectors[2][0:N_dim])
line3, = plt.plot(x, eigenvectors[3][0:N_dim])

plt.xlabel("x [a.u.]")
plt.ylabel("ψ n ( x ) [a.u.]")
plt.legend((line1, line2, line3), ('ψ1, Ε1 =  a.u.', 'ψ2, Ε2 =  a.u.', 'ψ3, Ε3 =  a.u.'))
plt.axis([-10, 10, max(eigenvectors[0]) - 2, max(eigenvectors[0]) + 2])
plt.axhline(color="black")
plt.text(-9.5, -1.75, "Created by Jack Binder 2022/05/09")
plt.title("Select Wave functions for a Harmonic Potential on a Spatial Grid of 1, 2, 3 Points")

if display_graph:
    plt.show()
elif not display_graph:
    plt.savefig("Binder.harmonic.Eigenvector1, 2, 3.png")
