from netCDF4 import Dataset
from eofs.standard import Eof
import numpy as np
import matplotlib.pyplot as plt
import sys

filename = 'hgt.mon.mean.nc'
data = Dataset(filename, 'r')
hgt = data.variables['hgt'][:, 5, 8:29, 16:57]
lons = data.variables['lon'][16:57]
lats = data.variables['lat'][8:29]

# dataMean = hgt.mean(axis=0)
# hgt = hgt - dataMean

# 纬度加权
coslat = np.cos(np.deg2rad(lats)).clip(0., 1.)
wgts = np.sqrt(coslat)[..., np.newaxis]

# create a solver class, taking advantage of built-in weighting
solver = Eof(hgt, weights=wgts)

# 选取排序前列的主成分 按照下面的贡献率来说选一个就够了
eof1 = solver.eofs(neofs=3)
# PC时间序列与每个网格点处的输入HGT异常之间的相关性的EOF。（标准化之后就是相关性）
eof1asCorr = solver.eofsAsCorrelation(neofs=3)
# 时间序列与每个网格点处的输入HGT异常之间的协方差的EOF。（简单距平就是协方差）
eof1asCov = solver.eofsAsCovariance(neofs=3)
# PC timeseries
pcs = solver.pcs(npcs=3)

eigenvals=solver.eigenvalues()
variance=solver.varianceFraction() # this is same as eigenvals/sum(eigenvals) 


def plotmapcolor(var, mode, vlats, vlons):
    import matplotlib.pyplot as plt
    import mpl_toolkits
    import mpl_toolkits.basemap
    import numpy as np
    map = mpl_toolkits.basemap.Basemap(llcrnrlon=vlons.min(),llcrnrlat=vlats.min(),urcrnrlon=vlons.max(),urcrnrlat=vlats.max(),projection='cyl',resolution='h')
    map.drawcoastlines()
    longrid,latgrid = np.meshgrid(vlons,vlats)
    x,y=map(longrid,latgrid)
    map.contourf(x,y,var,15,cmap=plt.cm.hot_r)
    map.colorbar(extend='both')
    plt.savefig('{}.png'.format(mode))

mode = int(sys.argv[1])
plotmapcolor(eof1[mode-1, :, :], mode, lats, lons)


