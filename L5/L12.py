from L1 import *


"""
    t test
"""

r1s = np.std(r1, axis=0)
r2s = np.std(r2, axis=0)
r3s = np.std(r3, axis=0)
t = {}
t[1] = (r1a - rt) *np.sqrt(r1.shape[0]) / r1s 
t[2] = (r2a - rt) *np.sqrt(r2.shape[0]) / r2s 
t[3] = (r3a - rt) *np.sqrt(r3.shape[0]) / r3s 

if __name__ == '__main__':
    from data import *
    import func
    import sys
    """
        从命令行接收参数的写法
    """
    func.plotmapcolor(abs(t[int(sys.argv[1])]), '{}t'.format(sys.argv[1]), lat, lon)
