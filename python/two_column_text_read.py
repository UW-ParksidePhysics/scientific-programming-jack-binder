__author__ = "Jack Binder"
import numpy as np


def two_column_text_read(file_name):
    """
    Read in two columns of data from a text file of arbitrary length
    :param file_name:str
    Name of file to be read in.
    :return:data: ndarray, shape (2, M)
    x-y data read in from file. M is the number of data points.
    """
    try:
        data = np.loadtxt(file_name)
        return data.transpose()
    except OSError:
        print(f"{file_name} cannot be found")


if __name__ == '__main__':
    volume_energies = two_column_text_read("volume_energies.dat")
    print(volume_energies)