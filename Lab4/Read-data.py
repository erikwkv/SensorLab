import matplotlib.pyplot as plt
from raspi_import import raspi_import
import numpy as np

def get_IFI_IFQ_fft(filename):
    sample_period, data = raspi_import(filename)

    radar_IF_I = (data[1:,4])*0.00081
    radar_IF_Q = (data[1:,2])*0.00081

    #remove dc offset
    radar_IF_I = radar_IF_I - np.mean(radar_IF_I)
    radar_IF_Q = radar_IF_Q - np.mean(radar_IF_Q)

    x = radar_IF_I + 1j*radar_IF_Q

    #windowing
    window = np.hanning(len(x))
    radar_IF_I = radar_IF_I*window
    x = x*window
    #fft
    X = np.fft.fft(x)
    freqz = np.fft.fftfreq(len(x),sample_period)

    return X, freqz, x, radar_IF_I, radar_IF_Q, sample_period

def plot_time_domain(x, radar_IF_I, radar_IF_Q,sample_period):

    time_axis = 1e3*sample_period*np.arange(len(radar_IF_I))
    plt.plot(radar_IF_Q,label='IF_Q',color='r')
    plt.plot(radar_IF_I,label='IF_I',color='b')
    plt.xlabel('Time (ms)')
    plt.ylabel('Amplitude (V)')
    plt.legend()
    plt.show()


def plot_freq_domain(X,freqz):
    plt.plot(freqz,20*np.log10(np.abs(X)))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.xlim(-5000,5000)
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


def hele(filename):
    X, freqz, x, radar_IF_I, radar_IF_Q, sample_period = get_IFI_IFQ_fft(filename)
    f_d = find_freq(X,freqz)
    print('f_d:',f_d)
    v = velocity(f_d)
    print('velocity:',v)
    plot_time_domain(x, radar_IF_I, radar_IF_Q,sample_period)
    plot_freq_domain(X,freqz)

hele('Lab4/sakte2.bin')

# print('Sakte:')
# hele('Lab4/sakte1.bin')
# hele('Lab4/sakte2.bin')
# hele('Lab4/sakte3.bin')
# hele('Lab4/sakte4.bin')

# print('Kjapp:')
# hele('Lab4/kjapp1.bin')
# hele('Lab4/kjapp2.bin')
# hele('Lab4/kjapp3.bin')
# hele('Lab4/kjapp4.bin')

# print('Rygging:')
# hele('Lab4/rygging1.bin')
# hele('Lab4/rygging2.bin')
# hele('Lab4/rygging3.bin')
# hele('Lab4/rygging4.bin')


