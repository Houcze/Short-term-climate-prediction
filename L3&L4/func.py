import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm
import numpy as np
from data import *

"""
    绘图函数
"""
def plotmapcolor(var, name, vlats, vlons):
    map = Basemap(llcrnrlon=vlons.min(), llcrnrlat=vlats.min(), urcrnrlon=vlons.max(), urcrnrlat=vlats.max(),projection='cyl',resolution='h')
    map.drawcoastlines()
    longrid, latgrid = np.meshgrid(vlons,vlats)
    x, y = map(longrid, latgrid)
    """
    map.contourf(x, y, var, 15, cmap=plt.cm.hot_r)
    """
    map.contourf(x, y, var, 40, cmap=cm.GMT_haxby)
    plt.colorbar(extend='both')
    plt.savefig('{}.png'.format(name))

def EU():
    lat1 = np.where(lat==55.)
    lat2 = np.where(lat==40.)
    lon1 = np.where(lon==20.)
    lon2 = np.where(lon==75.)
    lon3 = np.where(lon==145.)
    return -hgt[:, lat1[0], lon1[0]] / 4 + hgt[:, lat1[0], lon2[0]] / 2 - hgt[:, lat2[0], lon3[0]] / 4

def r(x, y):
    return np.sum(T((x-x.mean()), (y-y.mean()))) / np.sqrt(np.sum((x-x.mean())**2)) / np.sqrt(np.sum((y-y.mean())**2))


def T(x, y):
    if x.size != y.size:
        print('error')
        return
    else:
        for xi in range(x.size):
            y[xi] *= x[xi]
    return y


