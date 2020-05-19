from data import *
import numpy as np
from rtype import *


nt, lat, lon = pre.shape
R = np.zeros((lat, lon)) 
for t in range(nt):
    R += pre[t, :, :]

R /= nt
Ri = pre


Ri[Ri<0]=None
Ri21 = Ri[5:50*12:12, :, :]
Ri22 = Ri[6:50*12:12, :, :]
Ri23 = Ri[7:50*12:12, :, :]
rr = rtype[10:60]

"""
    rain of type I
"""
i = np.argwhere(rr==1.)[:, 0]
r1 = (Ri21[i, :, :] + Ri22[i, :, :] + Ri23[i, :, :])
r1a = r1.mean(axis=0)
"""
    rain of type II
"""
ii = np.argwhere(rr==2.)[:, 0]
r2 = (Ri21[ii, :, :] + Ri22[ii, :, :] + Ri23[ii, :, :])
r2a = r2.mean(axis=0)
"""
    rain of type III
"""
iii = np.argwhere(rr==3.)[:, 0]
r3 = (Ri21[iii, :, :] + Ri22[iii, :, :] + Ri23[iii, :, :])
r3a = r3.mean(axis=0)

rt = (Ri21[9:39, :, :] + Ri22[9:39, :, :] + Ri23[9:39, :, :]).mean(axis=0)


rt1 = (r1a - rt) / rt
rt2 = (r2a - rt) / rt
rt3 = (r3a - rt) / rt
if __name__ == '__main__':
    from data import *
    import func
    func.plotmapcolor(rt3, 'III', lat, lon)
