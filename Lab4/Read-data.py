import matplotlib.pyplot as plt
from raspi_import import raspi_import
import numpy as np
from scipy.signal import find_peaks

sample_period, data = raspi_import('Lab4/kjapp1.bin')

# Plotting the data
time_axis = 1e3*sample_period*np.arange(len(data))

radar_IF_I = (data[1:,4] - np.mean(data[:,1]))*0.00081
radar_IF_Q = (data[1:,2] - np.mean(data[:,2]))*0.00081



time_axis = 1e3*sample_period*np.arange(len(data)-1)


#remove dc offset
radar_IF_I = radar_IF_I[0:54000] - np.mean(radar_IF_I)
radar_IF_Q = radar_IF_Q[0:54000] - np.mean(radar_IF_Q)

x = radar_IF_I + 1j*radar_IF_Q

# plt.plot(radar_IF_I,label='IF_I',color='b')
# plt.plot(radar_IF_Q,label='IF_Q',color='r')
# plt.xlabel('Time (ms)')
# plt.ylabel('Amplitude (V)')
# plt.legend()
# plt.show()

# z = z[0:54000]

# print(len(radar_IF_I))
# radar_IF_I = radar_IF_I[10_000:25_000]


# plt.plot(radar_IF_I,label='IF_I',color='b')
# plt.xlabel('Time (ms)')
# plt.ylabel('Amplitude (V)')
# plt.legend()
# plt.show()


#windowing
window = np.hanning(len(x))
radar_IF_I = radar_IF_I*window
x = x*window
#fft
X = np.fft.fft(x,2**23)
freqz = np.fft.fftfreq(2**23,sample_period)
fft_radar_IF_I = np.fft.fft(radar_IF_I,n=len(radar_IF_I))
freq = np.fft.fftfreq(len(radar_IF_I),sample_period)

plt.plot(freqz,20*np.log10(np.abs(X)),label='X',color='r')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude (dB)')
plt.grid()
plt.legend()
plt.show()


#find peaks between -15hz to -5hz
# peaks_I, _ = find_peaks(20*np.log10(np.abs(Z)))
# peaks_Q, _ = find_peaks(20*np.log10(np.abs(fft_radar_IF_Q)),height=55)

peak_index = np.argmax(np.abs(X))
f_d = freqz[peak_index]

# peaks, _ = find_peaks(20*np.log10(np.abs(X)),height=51.7)

# freq_peaks = freqz[peaks]

# print(freq_peaks)

f_0 = 24.13*10**9

def velocity(f_d,f_0): 
    c = 3*10**8
    return ((c*f_d) / (2*f_0))

print(velocity(f_d,f_0))
