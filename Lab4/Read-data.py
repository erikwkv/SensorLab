import matplotlib.pyplot as plt
from raspi_import import raspi_import
import numpy as np

def get_IFI_IFQ_fft(filename):
    sample_period, data = raspi_import('Lab4/kjapp2.bin')

    radar_IF_I = (data[1:,4] - np.mean(data[:,1]))*0.00081
    radar_IF_Q = (data[1:,2] - np.mean(data[:,2]))*0.00081

    #remove dc offset
    radar_IF_I = radar_IF_I - np.mean(radar_IF_I)
    radar_IF_Q = radar_IF_Q - np.mean(radar_IF_Q)

    x = radar_IF_I + 1j*radar_IF_Q

    #windowing
    window = np.hanning(len(x))
    radar_IF_I = radar_IF_I*window
    x = x*window
    #fft
    X = np.fft.fft(x,2**23)
    freqz = np.fft.fftfreq(2**23,sample_period)

    return X, freqz, x, radar_IF_I, radar_IF_Q, sample_period

def plot_time_domain(x, radar_IF_I, radar_IF_Q,sample_period):

    time_axis = 1e3*sample_period*np.arange(len(radar_IF_I))
    plt.plot(time_axis,radar_IF_Q,label='IF_Q',color='r')
    plt.plot(time_axis,radar_IF_I,label='IF_I',color='b')
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude (V)')
    plt.legend()
    plt.show()


def plot_freq_domain(X,freqz):
    plt.plot(freqz,20*np.log10(np.abs(X)))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.grid()
    plt.show()


def find_freq(X,freqz):
    peak_index = np.argmax(np.abs(X))
    f_d = freqz[peak_index]
    return f_d

def velocity(f_d): 
    f_0 = 24.13*10**9
    c = 3*10**8
    return ((c*f_d) / (2*f_0))

X, freqz, x, radar_IF_I, radar_IF_Q, sample_period = get_IFI_IFQ_fft('Lab4/kjapp2.bin')

plot_time_domain(x, radar_IF_I, radar_IF_Q,sample_period)
plot_freq_domain(X,freqz)
f_d = find_freq(X,freqz)
print('f_d:',f_d)
v = velocity(f_d)
print('velocity:',v)

