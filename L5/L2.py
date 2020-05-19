from h import *
import numpy as np
from rtype import *

hDec = h500[11::12, :, :]
hJan = h500[12::12, :, :]
hFeb = h500[13::12, :, :]

h12 = hDec[13:63, :, :]
h1 = hJan[13:63, :, :]
h2 = hFeb[13:63, :, :]



rr = rtype[10:60]

"""
    rain of type I
"""
i = np.argwhere(rr==1.)[:, 0]
r1 = (h12[i, :, :] + h1[i, :, :] +h2[i, :, :]) / 3
r1a = r1.mean(axis=0)
"""
    rain of type II
"""
ii = np.argwhere(rr==2.)[:, 0]
r2 = (h12[ii, :, :] + h1[ii, :, :] + h2[ii, :, :]) / 3
r2a = r2.mean(axis=0)
"""
    rain of type III
"""
iii = np.argwhere(rr==3.)[:, 0]
r3 = (h12[iii, :, :] + h1[iii, :, :] + h2[iii, :, :]) / 3
r3a = r3.mean(axis=0)

rt = ((h12 + h1 + h2) / 3.).mean(axis=0)


rt1 = r1a - rt
rt2 = r2a - rt
rt3 = r3a - rt
if __name__ == '__main__':
    from h import *
    import func
    func.plotmapcolor(rt1, 'Ih', lat, lon)
