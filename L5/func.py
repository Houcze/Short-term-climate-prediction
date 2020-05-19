import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm


"""
    绘图函数
"""
def plotmapcolor(var, name, vlats, vlons):
    map = Basemap(llcrnrlon=vlons.min(), llcrnrlat=vlats.min(), urcrnrlon=vlons.max(), urcrnrlat=vlats.max(), projection='cyl', resolution='h')
    map.drawcoastlines()
    longrid, latgrid = np.meshgrid(vlons, vlats)
    x, y = map(longrid, latgrid)
    """
    以下语句是另一种绘图选择, 但是这种方式会导致colorbar的extend设置失效, 原因未知
    map.contourf(x, y, var, 15, cmap=cm.GMT_haxby)
    """
    map.imshow(var, cmap=cm.GMT_haxby)
    map.colorbar(extend='both')
    plt.savefig('{}.png'.format(name))
