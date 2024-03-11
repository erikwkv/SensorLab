import matplotlib.pyplot as plt
from raspi_import import raspi_import
import numpy as np
from scipy.signal import find_peaks

sample_period, data = raspi_import('Lab4\out-2024-02-11-12.48.24.bin')

# Plotting the data
time_axis = 1e3*sample_period*np.arange(len(data))

radar_IF_I = (data[1:,4] - np.mean(data[:,1]))*0.00081


time_axis = 1e3*sample_period*np.arange(len(data)-1)


#remove dc offset
radar_IF_I = radar_IF_I - np.mean(radar_IF_I)

plt.plot(radar_IF_I,label='IF_I',color='b')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude (V)')
plt.legend()
plt.show()

print(len(radar_IF_I))
radar_IF_I = radar_IF_I[10_000:25_000]


plt.plot(radar_IF_I,label='IF_I',color='b')
plt.xlabel('Time (ms)')
plt.ylabel('Amplitude (V)')
plt.legend()
plt.show()


#windowing
window = np.hanning(len(radar_IF_I))
radar_IF_I = radar_IF_I*window
#fft
fft_radar_IF_I = np.fft.fft(radar_IF_I,n=len(radar_IF_I))
freq = np.fft.fftfreq(len(radar_IF_I),sample_period)


plt.plot(freq,20*np.log10(np.abs(fft_radar_IF_I)),label='IF_I',color='b')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
# plt.xlim(-200,200)
plt.grid()
plt.legend()
plt.show()

#find peaks between -15hz to -5hz
peaks_I, _ = find_peaks(20*np.log10(np.abs(fft_radar_IF_I)),height=55)
# peaks_Q, _ = find_peaks(20*np.log10(np.abs(fft_radar_IF_Q)),height=55)
peak_I = np.max(peaks_I)

print('Peaks in IF_I:',freq[peak_I])

def velocity(f_d,f_0): 
    c = 3*10**8
    return ((c*f_d) / (2*f_0))

print(velocity(freq[peak_I],24.13*10**9))
