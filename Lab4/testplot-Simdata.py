import pandas as pd
import numpy as np
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
fig, ax = plt.subplots(1,figsize=(10,10))

ax.axhline(y=1,color='red',linestyle='--', label=data.columns[2])
plt.plot(x, y1, label= labels[0])
plt.plot(x, y2, label= labels[1])
plt.xlabel('Frequency')
plt.ylabel('Amplitude relative to {0}'.format(data.columns[2]))
plt.xscale('log')  # Set x-axis to logarithmic scale
plt.yscale('log')  # Set x-axis to logarithmic scale
plt.title('Simulated Bode Plot')
plt.legend(bbox_to_anchor=(0.5, -0.15), loc="upper center",fancybox=True, ncol=5, borderaxespad=0)
plt.tight_layout(rect=[0,0,1,0.98])

plt.grid(True)

# Add a horizontal line at y=1, representing the input
  
plt.show()
