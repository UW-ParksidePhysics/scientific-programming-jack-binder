import numpy as np


def two_column_text_read(file_name):
    try:
        data = np.loadtxt(file_name)
        return data
    except OSError:
        print(f"{file_name} cannot be found")


if __name__ == '__main__':
    volume_energies = two_column_text_read("volume_energies.dat")
    print(volume_energies)
