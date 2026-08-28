import math

def cyclic_encoding(values: list, period: float) -> list:
    """
    Returns the sine and cosine encoding of every cyclic value.
    """
    encoded = []

    for value in values:
        theta = (2 * math.pi * value) / period
        encoded.append([math.sin(theta), math.cos(theta)])

    return encoded