import numpy as np

def reparameterize(mu: np.ndarray, log_var: np.ndarray, epsilon: np.ndarray) -> np.ndarray:
    """
    Returns the float64 latent sample with the same shape as mu.
    """
    sd = np.exp(0.5 * log_var)
    return (mu + sd * epsilon)