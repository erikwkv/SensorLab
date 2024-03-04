import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('Lab4/simulert-bodeplot.csv')

# Extract the x and y values
x = np.array(data.iloc[:, 0])
y1 = np.array(data.iloc[:, 1]/data.iloc[:, 2])
y2 = np.array(data.iloc[:, 3]/data.iloc[:, 2])

# Fetch labels from the first row
# Fetch labels from the first row
labels = data.columns[[1, 3]]


# Plot the data
plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('Frequency')
plt.ylabel('Amplitude relative to input')
plt.xscale('log')  # Set x-axis to logarithmic scale
plt.yscale('log')  # Set x-axis to logarithmic scale
plt.title('Simulated Bode Plot')
plt.legend(labels)
plt.grid(True)
plt.show()
