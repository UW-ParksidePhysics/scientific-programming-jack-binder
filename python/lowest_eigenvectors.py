import numpy as np


def lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    m, n = square_matrix.shape
    if m != n:
        raise IndexError("Not Square")
    eigenvalues, eigenvectors = np.linalg.eig(square_matrix)
    sorted_values = np.sort(eigenvalues)
    sorted_vectors = eigenvectors[:, eigenvalues.argsort()].transpose()
    return sorted_values[:number_of_eigenvectors], sorted_vectors[:number_of_eigenvectors]


if __name__ == "__main__":
    test_matrix = np.array([[3, 1, 1], [0, 2, 1], [0, 0, 1]])
    test_values, test_vectors = lowest_eigenvectors(test_matrix, number_of_eigenvectors=2)
    print(test_vectors)

