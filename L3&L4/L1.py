import matplotlib.pyplot as plt
from func import EU
import numpy as np

eu = EU()
eu = eu / np.std(eu)
if __name__ == '__main__':
    plt.plot(eu)
    np.save('eu.npy', eu.data)
    plt.title('EU the Correlation Index in Jan(1948-2020)')
    plt.savefig('EU.png')
