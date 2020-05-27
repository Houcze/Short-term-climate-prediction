import numpy as np
header = 1

M_Atm_Nc = np.genfromtxt('M_Atm_Nc.txt', skip_header=header)  # 88 parameters
M_Ext = np.genfromtxt('M_Ext.txt', skip_header=header)  # 16 parameters
NINO3_4 = np.genfromtxt('NINO3.4_index.txt', skip_header=1)

"""
    1951-2020.4的所有指数数据
"""
t = M_Atm_Nc[:, 0]
M_Atm_Nc = M_Atm_Nc[:, 1:]
M_Ext = M_Ext[:, 1:]
