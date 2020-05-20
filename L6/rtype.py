import numpy as np

r = np.genfromtxt('ddi')
rtype = np.zeros((r.shape[0], 1))
for year in range(r.shape[0]):
    rtype[year] = np.argwhere(r[year, :]==1.)+1
    