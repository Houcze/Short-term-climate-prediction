from data import *
from func import *
import numpy as np
from rtype import *


sstDec = sst[11::12, :, :]
sst12 = sstDec[81:141, :, :]
sst_ = sst12.mean(axis=0)
"""
    rain of type I
"""
i = np.argwhere(rtype == 1.)[:, 0]
r1 = sst12[i, :, :]
rain1 = r1.mean(axis=0)
"""
    rain of type II
"""
ii = np.argwhere(rtype == 2.)[:, 0]
r2 = sst12[ii, :, :]
rain2 = r2.mean(axis=0)
"""
    rain of type III
"""
iii = np.argwhere(rtype == 3.)[:, 0]
r3 = sst12[iii, :, :]
rain3 = r3.mean(axis=0)

rt1 = rain1 - sst_
rt2 = rain2 - sst_
rt3 = rain3 - sst_

if __name__ == '__main__':
    import func
    func.plotmapcolor(rt3[::-1], 'III', lat, lon)
