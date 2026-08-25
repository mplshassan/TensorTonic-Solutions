import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    N = len(X)
    X = np.asarray(X)
    mean = np.mean(X, axis=0)

    X_c = X - mean

    cov_matrix = (X_c.T @ X_c)  / (N - 1)

    return cov_matrix