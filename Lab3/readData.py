import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the data from the file
y = pd.read_csv('Lab3/Transmitance/transmit_test.mp4roi.csv', sep=' ')

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

samp_period = 10/len(green)

Y = np.fft.fft(green_windowed,512)
freq = np.fft.fftfreq(512, samp_period)

# Scale frequency axis by 60 to give BPM
freq_bpm = freq * 60

plt.plot(freq_bpm, np.abs(Y))
plt.xlim(0,1200)
plt.xlabel('Pulse [BPM]')
plt.ylabel('Amplitude')
plt.title('FFT of green channel')
plt.show()

relative_Y = 20*np.log10(abs(Y))
Y_dB = relative_Y - np.max(relative_Y)

plt.plot(freq_bpm,Y_dB)
plt.xlabel('Pulse [BPM]')
plt.ylabel('Relative amplitude [dB]')
plt.title('FFT of green channel')
plt.xlim(0,1200)
plt.show()

print(freq_bpm)

