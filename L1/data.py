import netCDF4
import numpy as np
from netCDF4 import Dataset

"""
读取nc文件
"""

n = 500.
nc_obj = Dataset('hgt_monthly.nc')
longitude = nc_obj.variables['longitude'][:]
latitude = nc_obj.variables['latitude'][:]
level = nc_obj.variables['level'][:]
time = nc_obj.variables['time'][:]
time_bnds = nc_obj.variables['time_bnds'][:]
z = nc_obj.variables['z'][:]

n500 = np.where(level == n)
h = z[::12, n500[0], ::-1, :]
h = h / 100
