import numpy as np


def two_column_text_read(file_name):
    data = np.loadtxt(file_name)
    return data


if __name__ == '__main__':
    volume_energies = two_column_text_read("volume_energies.dat")
    print(volume_energies)
