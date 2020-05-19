import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm

def show(data, saveName, llon=0, ulon=360, llat=-90, ulat=90):
    map = Basemap(llcrnrlon=llon,llcrnrlat=llat,urcrnrlon=ulon,urcrnrlat=ulat,resolution = 'h')
    map.drawcoastlines()
    x = np.linspace(llon, ulon, data.shape[1])
    y = np.linspace(llat, ulat, data.shape[0])
    xx, yy = np.meshgrid(x, y)

    plt.title('latitude ave of 500hPa(Jan) in 2008')
    c = plt.contour(xx, yy, data, 8, colors='black')
    plt.contourf(xx, yy, data, 8)
    plt.clabel(c, inline=True, fontsize=6)
    plt.savefig('{}.png'.format(saveName))