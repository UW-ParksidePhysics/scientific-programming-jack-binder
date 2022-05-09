__author__ = "Pancho Rodriquez"
import numpy as np


def fit_curve_array(quadratic_coefficients, min_x, max_x, number_of_points=100):
    """
    Make fit curve using fit polynomial coefficients, NumPy's polyval (Links to an external site.), and minimum and
    maximum x-values
    :param quadratic_coefficients: ndarray, shape (3,)
    Quadratic polynomial coefficients, ordered quadratic term first, then linear term, and constant term last.
    :param min_x: float
    Starting value for the fit_curve array.
    :param max_x: float
    Ending value for the fit curve array.
    :param number_of_points: int, optional
    Number of points N to return for final fit curve. Default is 100.
    :return: fit_curve: ndarray, shape (2, N)
    x-y data created by the coefficients of the fit function. N is the number of function evaluation points.
    """
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
    curve = fit_curve_array(test_coefficients, test_min[0], test_min[1])  # y = x**2
    print(curve)
