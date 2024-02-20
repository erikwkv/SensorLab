import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file
y = pd.read_csv('tommel2', sep=' ')

# Plot the data
# Plot the data
time = np.linspace(0,10,len(y.iloc[:, 1]))
plt.plot(time,y.iloc[:, 1], label='Data from tommel2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data from tommel2')
plt.show()
