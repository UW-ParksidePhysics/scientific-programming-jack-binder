import numpy as np
import matplotlib.pyplot as plt


def plot_data_with_fit(data, fit_curve, data_format="o", fit_format=""):
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

