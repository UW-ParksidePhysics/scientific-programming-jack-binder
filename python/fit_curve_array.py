import numpy as np


def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100):
    if max_x < min_x:
        raise ArithmeticError
    if number_of_points <= 2:  # need more than 2 points
        raise IndexError

    x_array = np.linspace(min_x, max_x, number_of_points)  # 2 parameters
    y_array = np.polyval(quadratic_coefficients, x_array)  #
    fit_curve = np.array([x_array, y_array])  # np.column_stack((x_array, y_array))

    return fit_curve


if __name__ == "__main__":
    test_coefficients = np.array([1, 0, 0])
    test_min = [-2, 2]
    curve = fit_curve_array(test_coefficients, test_min[0], test_min[1]) # y = x**2
    print(curve)

