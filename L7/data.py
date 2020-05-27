from netCDF4 import Dataset

"""
    1951-2010降水量数据
"""

nc_obj = Dataset('CN05.1_Pre_1961_2017_month_025x025.nc')
lon = nc_obj.variables['lon'][:]
lat = nc_obj.variables['lat'][:]
time = nc_obj.variables['time'][:]
pre = nc_obj.variables['pre'][:]
