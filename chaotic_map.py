import numpy as np

def logistic_map(x0, r, size):

    seq = []

    x = x0

    for i in range(size):

        x = r * x * (1 - x)

        seq.append(x)

    return np.array(seq)
