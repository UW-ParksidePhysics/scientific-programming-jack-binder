__author__ = "Jordan Roszko"
import numpy as np
import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format="o", fit_format=""):
    """
    Create a combined scatter and curve plot for the data and the fit polynomial, respectively, using Pyplot's plot
    (Links to an external site.) function
    :param data: ndarray, shape(2, M)
    x-y data that was fit. M is the number of data points.
    :param fit_curve: ndarray, shape(2, N)
    x-y data created by the coeffecients of the fit function. N is the number of function evaluation points
    (usually much greater than M).
    :param data_format: str, optional
    Optional formatting specification for the style of the scatter plot data points.  Default is 'o'.  See Pyplot's plot
    (Links to an external site.) for specifications. (Use Pyplot's plot, not scatter for this.)
    :param fit_format: tr, optional
    Optional formatting specification for the curve of the fit function. Default is '' (empty string). See Pyplot's plot
    (Links to an external site.) for specifications.
    :return: combined_plot
    A list of Line2D (Links to an external site.) objects representing the plotted data. This is the default return type
    from Pyplot's plot.
    """
    fig, combined_plot = plt.subplots()
    combined_plot.plot(fit_curve[0], fit_curve[1], fit_format)
    combined_plot.plot(data[0], data[1], data_format)
    return combined_plot


if __name__ == "__main__":
    test_data = np.array([[0, 0], [1, 1], [2, 4], [4, 16]])
    test_curve = np.empty([2, 50])
    test_curve[0] = np.linspace(0, 5)
    test_curve[1] = np.linspace(0, 5) ** 2
    plot_data_with_fit(test_data.transpose(), test_curve)
    plt.show()
