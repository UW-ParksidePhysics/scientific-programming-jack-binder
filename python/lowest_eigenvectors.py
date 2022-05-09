import numpy as np


def lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    eigenvalues, eigenvectors = np.linalg.eig(square_matrix)
    return eigenvalues, eigenvectors


if __name__ == "__main__":
    test_matrix = np.array([[2, 1], [0, 1]])
    test_values, test_vectors = lowest_eigenvectors(test_matrix)
    print(test_vectors, test_values)

# Module name:
# lowest_eigenvectors
# Parameters:
# square_matrix: ndarray, shape(M, M)
# Matrix to be characterized. Must be a square matrix of M rows and M columns where M is >=1.
# number_of_eigenvectors: int, optional
# Number of eigenvectors K with eigenvalues to return.  Default is 3.
# Returns:
# eigenvalues: ndarray, shape(K,)
# Array of the K lowest-value eigenvalues ordered from lowest to highest.
# eigenvectors: ndarray, shape(K, M)
# Array of K eigenvectors with M components arranged in order corresponding to their eigenvalues. The first index should correspond to the eigenvalue index in the eigenvalues array. The order of the components in the eigenvector remains the same as output by NumPy's eig.
