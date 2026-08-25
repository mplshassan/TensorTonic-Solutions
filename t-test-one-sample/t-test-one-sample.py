import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    n = len(x)
    x_bar = float(np.mean(x))
    
    diffs = np.asarray(x) - x_bar
    total = np.dot(diffs, diffs)

    var = total / (n - 1)
    s = np.sqrt(var)

    t = (x_bar - mu0) / (s / np.sqrt(n))

    return float(t)