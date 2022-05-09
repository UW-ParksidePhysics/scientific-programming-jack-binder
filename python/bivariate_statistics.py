__author__ = "Pancho Rodriquez"
import numpy as np
from scipy import stats


def bivariate_statistics(data):
    """
    Calculate statistical characteristics of a data set using SciPy's stats.describe function
    :param data:ndarray, shape(2, M)
    x-y data to be characterized. M is the number of data points.
    :return:statistics: ndarray, shape (6,)
    Mean of y, standard deviation of y, minimum x-value, maximum x-value, minimum y-value, maximum y-value
    """
    if len(data) != 2 or len(data[0]) <= 1:
        raise IndexError
    stat = stats.describe(data, axis=1)
    mean_of_y = stat.minmax[0][1]
    standard_deviation_of_y = np.sqrt(stat.variance[1])
    minimum_x_value = stat.minmax[0][0]
    maximum_x_value = stat.minmax[1][0]
    minimum_y_value = stat.minmax[0][1]
    maximum_y_value = stat.minmax[1][1]

    statistics = np.array(
        [mean_of_y, standard_deviation_of_y, minimum_x_value, maximum_x_value, minimum_y_value, maximum_y_value])

    return statistics


if __name__ == '__main__':
    x = [2, 5, 4]
    y = [4, 3, 2]
    data = np.array([x, y])
    print(bivariate_statistics(data))
