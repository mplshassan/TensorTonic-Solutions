import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    numerator = a @ b

    mag_a = np.sqrt(np.dot(a, a))
    mag_b = np.sqrt(np.dot(b, b))

    denominator = mag_a * mag_b

    if mag_a == 0 or mag_b == 0:
        return 0.0
        
    return float(numerator / denominator)
    