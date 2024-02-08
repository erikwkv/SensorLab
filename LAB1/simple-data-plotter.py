import matplotlib.pyplot as plt
from raspi_import import raspi_import
import numpy as np

sample_period, data = raspi_import('data-sampling\out-2024-00-30-16.54.22.bin')

#factor to multiply with to get voltage:
res_factor = 0.00081
#Separating adc channels and removing dc offset.

def remove_dc_offset(data):
    for i in range(len(data[0,:])):
        data[1:,i] = (data[1:,i] - np.mean(data[:,i]))*res_factor
    return data_

adc_1_ac = (data[1:,0] - np.mean(data[:,0]))*res_factor
adc_2_ac = (data[1:,1] - np.mean(data[:,1]))*res_factor
adc_3_ac = (data[1:,2] - np.mean(data[:,2]))*res_factor
adc_4_ac = (data[1:,3] - np.mean(data[:,3]))*res_factor
adc_5_ac = (data[1:,4] - np.mean(data[:,4]))*res_factor


time_axis = 1e3*sample_period*np.arange(len(data)-1)
plt.plot(time_axis,adc_1_ac, label='Mic 1')
plt.plot(time_axis,adc_2_ac, label='Mic 2')
plt.plot(time_axis,adc_3_ac, label='Mic 3')
plt.plot(time_axis,adc_4_ac, label='Mic 4')
plt.plot(time_axis,adc_5_ac, label='Mic 5')
plt.xlabel('Time [ms]')
plt.ylabel('Spenning [V]')
plt.title('Time domain plot of the recorded data')
plt.legend()
plt.xlim(20,25)
plt.show()


# print(data.shape)
# print(len(data[:,0]))

#fft of one channel
Y = np.fft.fft(data[:,0],2**15)
freqs = np.fft.fftfreq(2**15,sample_period)

#only positive freqs, and removing the first 20 values due to dc noise
positive_freqs = freqs[20:len(freqs)//2]
positive_Y = abs(Y)[20:len(Y)//2]

# plt.yscale('log')
plt.plot(positive_freqs,positive_Y)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.xlim(0,5000)
plt.show()


#windowed function fft
window = np.hanning(len(data[:,0]))
windowed_data = data[:,0]*window

Y_windowed = np.fft.fft(windowed_data,2**15)
freqs_windowed = np.fft.fftfreq(2**15,sample_period)

positive_freqs_windowed = freqs_windowed[20:len(freqs_windowed)//2]
positive_Y_windowed = abs(Y_windowed)[20:len(Y_windowed)//2]

plt.yscale('log') 
plt.plot(positive_freqs_windowed, positive_Y_windowed)
plt.show()

#Power plot
power = abs(Y_windowed)**2

#only positive freqs
power = power[20:len(power)//2]
freqs_windowed = freqs_windowed[20:len(freqs_windowed)//2]

# plt.plot(freqs_windowed,power)
# plt.yscale('log')
# plt.show()



