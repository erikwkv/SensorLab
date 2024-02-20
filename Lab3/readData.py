import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file
y = pd.read_csv('tommel2', sep=' ')
print(y)

red = y[:,0]
green = y[:,1]
blue = y[:,2]
time = np.linspace(0,10,len(green))

# Plot the data
plt.plot(time, green, 'o', label='Data from tommel2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data from tommel2')
plt.show()