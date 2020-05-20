from netCDF4 import Dataset
import numpy as np
"""
    读取nc文件
"""
nc_obj = Dataset('HadISST_sst.nc')
lon = nc_obj.variables['longitude'][:]
lat = nc_obj.variables['latitude'][:]
time = nc_obj.variables['time'][:]
sst = nc_obj.variables['sst'][:]
time_bnds = nc_obj.variables['time_bnds'][:]
sst[sst < -50] = None
