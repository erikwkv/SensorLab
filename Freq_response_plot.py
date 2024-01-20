import numpy as np
import scipy as sc
from matplotlib import pyplot as plt

def H(w,L,C_1,C_2):
    return 1/(1+1j*w*C_1*(L+C_2))

x = np.linspace(0,20000,1000000)
y = H(x,400e-3,520e-6,470.1e-6)
# a = 1
# b=2
# z = a+b*1j
# print(z)