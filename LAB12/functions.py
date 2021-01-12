import numpy as np


def fermi(x):
    return 1 / (1 + np.exp(-1 * x))
