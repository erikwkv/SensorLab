import matplotlib.pyplot as plt
from raspi_import import raspi_import
import numpy as np

sample_period, data = raspi_import('LAB1\data-sampling\out-2024-00-30-16.54.22.bin')

#factor to multiply with to get voltage:
res_factor = 0.00081
#Separating adc channels and removing dc offset.


adc_1_ac = (data[:,0] - np.mean(data[:,0]))*res_factor
adc_2_ac = (data[:,1] - np.mean(data[:,1]))*res_factor
adc_3_ac = (data[:,2] - np.mean(data[:,2]))*res_factor
adc_4_ac = (data[:,3] - np.mean(data[:,3]))*res_factor
adc_5_ac = (data[:,4] - np.mean(data[:,4]))*res_factor


time_axis = 1e3*sample_period*np.arange(len(adc_1_ac))
# plt.plot(time_axis,adc_1_ac, label='ADC 1')
# plt.plot(time_axis,adc_2_ac, label='ADC 2')
# plt.plot(time_axis,adc_3_ac, label='ADC 3')
# plt.plot(time_axis,adc_4_ac, label='ADC 4')
# plt.plot(time_axis,adc_5_ac, label='ADC 5')
# plt.xlabel('Tid [ms]')
# plt.ylabel('Spenning [V]')
# plt.title('Spenning som funksjon av tid for de fem ADCene')
# plt.legend()
# plt.xlim(20,25)
# plt.ylim(-1.5,1.5)
# plt.show()


# print(data.shape)
# print(len(data[:,0]))

#fft of one channel
Y = np.fft.fft(adc_1_ac,2**15)
freqs = np.fft.fftfreq(2**15,sample_period)
relative_Y = 20*np.log10(abs(Y))
Y_dB = relative_Y - np.max(relative_Y)

#only positive freqs, and removing the first 20 values due to dc noise
# positive_freqs = freqs[:len(freqs)//2]
# positive_Y = abs(Y)[:len(Y)//2]


# plt.yscale('log')
# plt.plot(freqs,Y_dB)
# plt.xlabel('Frekvens [Hz]')
# plt.ylabel('Relativ amplitude [dB]')
# plt.title('Relativ amplituderespons for signalet fra én ADC uten vindu')
# plt.xlim(0,5000)
# plt.ylim(-100,5)
# plt.show()


#windowed function fft
window = np.hanning(len(data[:,0]))
windowed_data = adc_1_ac*window

Y_windowed = np.fft.fft(windowed_data,2**15)
freqs_windowed = np.fft.fftfreq(2**15,sample_period)

rel_Y_wind = 20*np.log10(abs(Y_windowed))
Y_windowed_dB = rel_Y_wind - np.max(rel_Y_wind)

# positive_freqs_windowed = freqs_windowed[:len(freqs_windowed)//2]
# positive_Y_windowed = abs(Y_windowed)[:len(Y_windowed)//2]

# plt.yscale('log')
# plt.plot(freqs_windowed, Y_windowed_dB)
# plt.title('Relativ amplituderespons for signalet fra én ADC med Hanning-vindu')
# plt.xlabel('Frekvens [Hz]')
# plt.ylabel('Relativ amplitude [dB]')
# plt.xlim(0,5000)
# plt.show()

#Power plot
power = abs(Y_windowed)**2
rel_pow = 10*np.log10(power)

plt.plot(freqs_windowed,power)
plt.title('Effektspekter for signalet fra én ADC med Hanning-vindu')
plt.xlabel('Frekvens [Hz]')
plt.ylabel('Effekt [V^2]')
plt.xlim(0,5000)
plt.show()




