__author__ = "Pancho Rodriquez"
import numpy as np
from scipy import stats


def bivariate_statistics(data):
    """
    Calculate statistical characteristics of a data set using SciPy's stats.describe function
    :param data:ndarray, shape(2, M)
    x-y data to be characterized. M is the number of data points.
    :return: statistics: ndarray, shape (6,)
    Mean of y, standard deviation of y, minimum x-value, maximum x-value, minimum y-value, maximum y-value
    """
    if len(data) != 2 or len(data[0]) <= 1:
        raise IndexError("Inappropriate Dimensions")
    stat = stats.describe(data)
    mean_y = stat.minmax[0][1]
    x_min, x_max = stat.minmax[0][0], stat.minmax[1][0]
    y_min, y_max = stat.minmax[0][1], stat.minmax[1][1]
    standard_deviation = np.sqrt(stat.variance[1])
    statistics = np.array([mean_y, standard_deviation, x_min, x_max, y_min, y_max])
    return statistics


if __name__ == "__main__":
    x = [1, 2, 3]
    y = [2, 4, 6]
    test_array = np.array([x, y])
    print(bivariate_statistics(test_array))
