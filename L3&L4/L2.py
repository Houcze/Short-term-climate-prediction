from func import *
from L1 import *

h = np.zeros((73, 144))
for mx in range(73):
    for ny in range(144):
        h[mx, ny] = r(hgt[:, mx, ny], eu.reshape(73))

if __name__ == '__main__':
    plotmapcolor(h, 'h-eu corr', lat, lon)