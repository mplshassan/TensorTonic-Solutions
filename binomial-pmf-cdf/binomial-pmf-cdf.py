import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    exactly_k = math.comb(n, k) * p**k * (1 - p)**(n - k)

    at_most_k = sum([math.comb(n, i) * p**i * (1 - p)**(n - i) for i in range(k + 1)])

    return {"pmf": float(exactly_k), "cdf": float(at_most_k)}