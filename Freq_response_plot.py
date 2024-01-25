import numpy as np
import scipy as sc
from matplotlib import pyplot as plt

def H(w,L,C):
    return 1/(1-w*L*C)


w = np.linspace(0,20000,1000000)
y = H(w,400e-3,470.1e-6)

plt.plot(w,np.abs(y))
plt.show()