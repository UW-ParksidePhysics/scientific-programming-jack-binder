import numpy as np


def bivariate_statistics(data):
    xs = data[:, 0]
    ys = data[:, 1]
    quadratic_coefficients = np.polyfit(xs, ys, 2)
    return quadratic_coefficients


if __name__ == "__main__":
    test_data = np.array([[0, 0], [1, 1], [2, 4]])

    coefficients = bivariate_statistics(test_data)
    print(coefficients)

