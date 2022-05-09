import numpy as np
from scipy import stats


def bivariate_statistics(data):
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
