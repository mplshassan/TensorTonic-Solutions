import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    n = len(x)
    x_bar = float(np.mean(x))
    sum = 0
    
    for i in range(n):
        sum += (x[i] - x_bar)**2

    var = sum / (n - 1)
    sd = float(np.sqrt(var))

    return {"variance": var, "standard_deviation": sd}