from netCDF4 import Dataset
import numpy as np


"""
    读取nc文件
"""
nc_obj = Dataset('hgt.mon.mean.nc')
level = nc_obj.variables['level'][:]
lon = nc_obj.variables['lon'][:]
lat = nc_obj.variables['lat'][:]
time = nc_obj.variables['time'][:]
hgt = nc_obj.variables['hgt'][:]
"""
    500hPa高度场
"""
h500 = hgt.data[:, np.argwhere(level.data==500.)[0][0], :, :]