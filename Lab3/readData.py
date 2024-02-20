import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the file
data = pd.read_csv('Lab3/tommel2', sep=' ')

# Plot the data
plt.plot(data['x'], data['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data from tommel2')
plt.show()