import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Generate some sample data
x = np.linspace(0, 10, 100)
y = -0.2 * (x - 5) ** 2 + 2 * np.sin(x) + 5 * np.cos(2 * x)

# Find local maxima using find_peaks
peaks, _ = find_peaks(y)

# Get x-values corresponding to local maxima
x_maxima = x[peaks]

# Plot the graph
plt.plot(x, y, label='Function')
plt.plot(x_maxima, y[peaks], 'ro', label='Local Maxima')
plt.legend()
plt.show()

# Print x-values of local maxima
print("X-values of local maxima:", x_maxima)
