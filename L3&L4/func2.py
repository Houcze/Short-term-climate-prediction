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
        





