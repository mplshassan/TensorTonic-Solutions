import numpy as np

def calculate_eigenvalues(matrix: list) -> np.ndarray:
    """
    Returns a sorted NumPy array of real eigenvalues.
    """
    eigen_vals = np.linalg.eigvals(matrix)

    real_vals = np.sort(eigen_vals.real)

    return real_vals