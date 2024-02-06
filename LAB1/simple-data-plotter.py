import matplotlib.pyplot as plt
from raspi_import import raspi_import
import numpy as np

sample_period, data = raspi_import('data-sampling\out-2024-00-30-16.54.22.bin')

# Plotting the data
time_axis = 1e3*sample_period*np.arange(len(data))
plt.plot(time_axis,data[:]*0.00081)
plt.xlabel('Time [ms]')
plt.ylabel('Spenning [V]')
plt.title('Time domain plot of the recorded data')
plt.xlim(20,40)
plt.legend()

plt.show()


# print(data.shape)
# print(len(data[:,0]))


Y = np.fft.fft(data[:,0],2**15)
freqs = np.fft.fftfreq(2**15,sample_period)

positive_freqs = freqs[20:len(freqs)//2]
positive_Y = abs(Y)[20:len(Y)//2]

# plt.yscale('log')
# plt.plot(positive_freqs, positive_Y)
# plt.xlabel('Frequency [Hz]')
# plt.ylabel('Amplitude')
# plt.xlim(0,5000)
# plt.show()


#windowed function fft
window = np.hanning(len(data[:,0]))
windowed_data = data[:,0]*window

Y_windowed = np.fft.fft(windowed_data,2**15)
freqs_windowed = np.fft.fftfreq(2**15,sample_period)

positive_freqs_windowed = freqs_windowed[20:len(freqs_windowed)//2]
positive_Y_windowed = abs(Y_windowed)[20:len(Y_windowed)//2]

# plt.yscale('log')
# plt.plot(positive_freqs_windowed, positive_Y_windowed)
# plt.show()

#Power plot
power = abs(Y_windowed)**2

#only positive freqs
power = power[20:len(power)//2]
freqs_windowed = freqs_windowed[20:len(freqs_windowed)//2]

# plt.plot(freqs_windowed,power)
# plt.yscale('log')
# plt.show()



