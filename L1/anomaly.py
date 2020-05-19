from data import h
from ave import aveh


"""
2008年应该是第30个数据
"""
anomalies = h[29, :, :, :].reshape(73, 144) - aveh

if __name__ == '__main__':
    import func
    func.show(anomalies, 'Q2')
