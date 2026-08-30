import numpy as np

def hinge_loss(y_true: list, y_score: list, margin: float = 1.0, reduction: str = "mean") -> float:
    """
    Returns the loss as a float.
    """
    y_true = np.asarray(y_true, dtype=float)
    y_score = np.asarray(y_score, dtype=float)

    sample_loss = np.maximum(0, margin - (y_true * y_score))

    mean = float(np.mean(sample_loss))
    sum = float(np.sum(sample_loss))

    return mean if reduction == "mean" else sum