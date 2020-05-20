import numpy as np
from L1 import *
"""
    合成差值与t检验
"""
rain12 = rain1 - rain2
rain13 = rain1 - rain3
rain23 = rain2 - rain3

if __name__ == '__main__':
    import func
    func.plotmapcolor(rain23[::-1], '23', lat, lon)
