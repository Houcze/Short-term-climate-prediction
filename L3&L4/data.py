from netCDF4 import Dataset
import numpy as np
"""
    读取nc文件
"""

n = 500.
nc_obj = Dataset('hgt.mon.mean.nc')
lon = nc_obj.variables['lon'][:]
lat = nc_obj.variables['lat'][:]
time = nc_obj.variables['time'][:]
H = nc_obj.variables['hgt'][:]
level = nc_obj.variables['level'][:]
hgt = H[::12, np.where(level==500.), :, :].squeeze()
