import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    probabilities = [
        (math.e**(-lam) * lam**i) / math.factorial(i) for i in range(k + 1)
    ]

    return {
        "pmf": float(probabilities[k]),
        "cdf": float(sum(probabilities))
    }