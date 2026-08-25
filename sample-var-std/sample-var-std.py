import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    n = len(x)
    x_bar = float(np.mean(x))
    
    diffs = np.asarray(x) - x_bar
    total = np.dot(diffs, diffs)

    var = float(total / (n - 1))
    sd = float(np.sqrt(var))

    return {"variance": var, "standard_deviation": sd}