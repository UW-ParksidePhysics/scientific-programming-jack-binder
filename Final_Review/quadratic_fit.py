__author__ = "Jack Binder"
import numpy as np


def quadratic_fit(data):
    """
    Fit a quadratic polynomial to a two row NumPy array of x-y data using NumPy's polyfit (Links to an external site.)
    function
    :param data: ndarray, shape (2, M)
    x-y data to be fit. M is the number of data points.
    :return:quadratic_coefficients: ndarray, shape (3,)
    Quadratic polynomial coefficients, ordered quadratic term first, then linear term, and constant term last.
    """
    xs = data[:, 0]
    ys = data[:, 1]
    quadratic_coefficients = np.polyfit(xs, ys, 2)
    return quadratic_coefficients


if __name__ == "__main__":
    test_data = np.array([[0, 0], [1, 1], [2, 4]])
    coefficients = quadratic_fit(test_data)
    print(coefficients)

