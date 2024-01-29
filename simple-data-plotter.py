import matplotlib.pyplot as plt
from raspi_import import raspi_import

sample_period, data = raspi_import('out-2024-00-29-13.47.29.bin')

# Plotting the data
plt.plot(data*0.00081)
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Data Plot')
plt.show()

print(data.shape)
# print(sample_period)


