from data import h
import numpy as np

aveh = np.zeros((73, 144))
for year in range(0, 42):
    aveh += h[year, :, :, :].reshape(73, 144) / 42.

if __name__ == '__main__':
    import func
    func.show(aveh, 'Q1')
