from L1 import *


def ttest(x1, x2):
    x1_ = x1.mean(axis=0)
    x2_ = x2.mean(axis=0)
    N1 = x1.shape[0]
    N2 = x2.shape[0]
    S1 = np.std(x1, axis=0)
    S2 = np.std(x2, axis=0)
    return (x1_ - x2_) / np.sqrt(((N1 - 1) * S1 * S1 + (N2 - 1) * S2 * S2) / (N1 + N2 - 2)) / np.sqrt(1 / N1 + 1 / N2)


if __name__ == '__main__':
    import func
    from data import *
    func.plotmapcolor(ttest(r2, r3)[::-1], 'ttest23', lat, lon)
