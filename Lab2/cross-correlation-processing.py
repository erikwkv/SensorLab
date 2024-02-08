import matplotlib.pyplot as plt
from raspi_import import raspi_import
import numpy as np

sample_period, data = raspi_import('Lab2/angle-measurements/90out-2024-01-08-09.57.28.bin')

# Plotting the data
time_axis = 1e3*sample_period*np.arange(len(data))

mic_1_ac = (data[1:,0] - np.mean(data[:,0]))*0.00081
mic_2_ac = (data[1:,1] - np.mean(data[:,1]))*0.00081
mic_3_ac = (data[1:,2] - np.mean(data[:,2]))*0.00081


time_axis = 1e3*sample_period*np.arange(len(data)-1)
# plt.plot(time_axis,mic_1_ac,label='Mic 1')
# plt.plot(time_axis,mic_2_ac,label='Mic 2')
# plt.plot(time_axis,mic_3_ac,label='Mic 3')
# plt.legend()
# plt.show()

#new time axis for the autocorrelation




x_vals = np.linspace(-len(mic_1_ac)/2,len(mic_1_ac)/2,len(mic_1_ac)*16)
x_in = np.linspace(-len(mic_1_ac)/2,len(mic_1_ac)/2,len(mic_1_ac))

mic_1_interp = np.interp(x_vals,x_in,mic_1_ac)

plt.plot(x_vals,mic_1_interp,'-x',label='Interpolated')
plt.plot(x_in,mic_1_ac,'o',label='Original')
plt.legend()
plt.grid()
plt.show()

auto_corr_1 = np.correlate(mic_1_interp,mic_1_interp,mode='same')
time_axis2 = 1e3*sample_period*np.linspace(-len(data)/2,len(data)/2,len(auto_corr_1))

plt.plot(time_axis2,auto_corr_1)
plt.xlabel('Time [ms]')
plt.ylabel('Amplitude')
plt.show()




