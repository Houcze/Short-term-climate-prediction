import math

def f(x):
    for i in range(163):
        for j in range(283):
            if math.isnan(x[i, j]):
                x[i, j] = 0.
    return x

    