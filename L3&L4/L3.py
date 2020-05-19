from func2 import r, plotmapcolor
from tm import *
import numpy as np

eu = np.load('eu.npy')
eu2 = eu[13:70]

h2 = np.zeros((163, 283))
for mx in range(163):
    for ny in range(283):
        if (tm[:, mx, ny]==-9999.).all():
            h2[mx, ny] = np.nan
        else:
            h2[mx, ny] = r(tm[:, mx, ny], eu2)

plotmapcolor(h2, 't-eu China corr', lat, lon)