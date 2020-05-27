from M import M_Atm_Nc, NINO3_4, M_Ext
from data import pre, lon, lat
import numpy as np

"""
    准备降水数据, 1961-2010年份1月
"""
pre_Jan = pre[:50*12:12, :, :]
"""
    截取M_Atm_Nc, Nino3_4以使得时间范围一致
"""
M_Atm_Nc_s = M_Atm_Nc[:12 * 50, :]
M_Ext_s = M_Ext[:12 * 50, :]
NINO3_4_s = NINO3_4[12:12 * 51, :]
"""
    仅保留一月数据
"""
M_Atm_Nc_Jan = M_Atm_Nc_s[::12, :]
M_Ext_Jan = M_Ext_s[::12, :]
NINO3_4_Jan = NINO3_4_s[::12, :]
"""
    从中国地区取出华北地区
    此处使用华北地区范围是经纬度 32 °N- 42°N,104 °E-125 °E
"""
latn = np.where((lat <= 42) & (lat >= 32))[0]
lonn = np.where((lon <= 125) & (lon >= 104))[0]
pre_Jan_North_China = pre_Jan[:, int(np.min(latn)):int(
    (np.max(latn)+1)), int(np.min(lonn)):int((np.max(lonn)+1))]

pre_Jan_North_China_ave = pre_Jan_North_China.data.mean(axis=0).data
pre_Jan_North_China_anoma = (pre_Jan_North_China.data - pre_Jan_North_China_ave) / pre_Jan_North_China_ave

pre_Jan_North_China_anoma[pre_Jan_North_China_anoma==-np.inf]=None
X = np.vstack([M_Atm_Nc_Jan[:, 26], M_Atm_Nc_Jan[:, 44], M_Atm_Nc_Jan[:, 45], M_Ext_Jan[:, 4],NINO3_4_Jan[:, 2]]).T
Y = np.zeros((50, ))

"""
    Code like this because I did not find a numpy method
"""
import math
for year in range(50):
    pret = 0
    mn = 0
    for prec in pre_Jan_North_China_anoma[year, :, :].reshape(pre_Jan_North_China_anoma[year, :, :].size):
        if math.isnan(prec):
            pass
        else:
            pret += prec
            mn += 1
    Y[year] = pret / mn

from sklearn.linear_model import LinearRegression                                   
regressor = LinearRegression()                                                      
regressor.fit(X[:40], Y[:40])                                                                 
y_pred = regressor.predict(X[:40])
"""
                                                   
SSR = np.sum((y_pred - Y) * (y_pred - Y))
S = np.sqrt(SSR / Y.size)

"""
np.save('y_pred.npy', y_pred)