import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file
y = pd.read_csv('tommel2', sep=' ')

# Plot the data
# Plot the data
red = y.iloc[:, 0]
green = y.iloc[:, 1]
blue = y.iloc[:, 2]

videolength = 10
time = np.linspace(0,videolength,len(green))
plt.plot(time,red, label='red', color='red')
plt.plot(time,green, label='green', color='green')
plt.plot(time,blue, label='blue', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data from tommel2')
plt.show()


#plot with normalised data
red = red-np.max(red)
green = green-np.max(green)
blue = blue-np.max(blue)
plt.plot(time,red, label='red', color='red')
plt.plot(time,green, label='green', color='green')
plt.plot(time,blue, label='blue', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data from tommel2')
plt.show()

