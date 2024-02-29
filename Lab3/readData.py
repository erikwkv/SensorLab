import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# Read the data from the file
y = pd.read_csv('Lab3\Genser\genser_1.mp4roi.csv', sep=' ')

# Plot the data
# Plot the data
red = y.iloc[:, 0]
green = y.iloc[:, 1]
blue = y.iloc[:, 2]

videolength = 10
time = np.linspace(0,videolength,len(green))

# plt.plot(time,red, label='red', color='red')
# plt.plot(time,green, label='green', color='green')
# plt.plot(time,blue, label='blue', color='blue')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Data from tommel2')
# plt.show()


#plot with normalised data
red = red-np.mean(red)
green = green-np.mean(green)
blue = blue-np.mean(blue)
plt.plot(time,red, label='red', color='red')
plt.plot(time,green, label='green', color='green')
plt.plot(time,blue, label='blue', color='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Data from tommel2')
plt.show()


#fft
window = np.hamming(len(green))
green_windowed = green*window

window = np.hamming(len(red))
red_windowed = red*window

window = np.hamming(len(blue))
blue_windowed = blue*window

samp_period = 10/len(green)

Y = np.fft.fft(red_windowed,512)
freq = np.fft.fftfreq(512, samp_period)

Y_green = np.fft.fft(green_windowed,512)
freq = np.fft.fftfreq(512, samp_period)

Y_blue = np.fft.fft(blue_windowed,512)
freq = np.fft.fftfreq(512, samp_period)



# Scale frequency axis by 60 to give BPM
freq_bpm = freq * 60

plt.plot(freq_bpm, np.abs(Y))
plt.xlim(0,1200)
plt.xlabel('Pulse [BPM]')
plt.ylabel('Amplitude')
plt.title('FFT of red channel')
plt.show()

peaks, _ = find_peaks(np.abs(Y))
peak_x_values = freq_bpm[peaks] 
for el in peak_x_values:
    if el > 60 and el < 100:
        print('Pulse: ', el)

relative_Y_red = 20*np.log10(abs(Y))
Y_dB_red = relative_Y_red - np.max(relative_Y_red)

relative_Y_green = 20*np.log10(abs(Y_green))
Y_dB_green = relative_Y_green - np.max(relative_Y_green)

relative_Y_blue = 20*np.log10(abs(Y_blue))
Y_dB_blue = relative_Y_blue - np.max(relative_Y_blue)

plt.plot(freq_bpm,Y_dB_red)
plt.xlabel('Pulse [BPM]')
plt.ylabel('Relative amplitude [dB]')
plt.title('FFT of red channel')
plt.xlim(0,1200)
plt.show()

plt.plot(freq_bpm,Y_dB_blue)
plt.xlabel('Pulse [BPM]')
plt.ylabel('Relative amplitude [dB]')
plt.title('FFT of green channel')
plt.xlim(0,1200)
plt.show()

plt.plot(freq_bpm,Y_dB_blue)
plt.xlabel('Pulse [BPM]')
plt.ylabel('Relative amplitude [dB]')
plt.title('FFT of blue channel')
plt.xlim(0,1200)
plt.show()

# print(freq_bpm)

