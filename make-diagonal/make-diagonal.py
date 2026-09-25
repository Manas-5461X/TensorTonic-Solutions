import numpy as np

def make_diagonal(v: list) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, N).
    """
    # Write code here
    v = np.asarray(v)

    return np.diag(v)
    pass