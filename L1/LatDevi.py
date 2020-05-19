from data import h
import numpy as np


"""
计算纬偏值
"""
h2008 = h[29, :, :, :].reshape(73, 144)
latAve = np.zeros((73, 144))

for nx in range(73):
    latAve[nx, :] = np.sum(h2008[nx, :]) / 144. 

data = h2008 - latAve

if __name__ == '__main__':
    import func
    func.show(data, 'Q3')