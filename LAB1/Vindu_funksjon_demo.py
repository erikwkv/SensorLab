import numpy as np
import matplotlib.pyplot as plt

# Generate a sine wave with a frequency of 1 kHz
fs = 10000  # Sampling frequency (Hz)
duration = 1  # Duration of the signal (seconds)
t = np.arange(0, duration, 1/fs)  # Time vector
f = 1000  # Frequency of the sine wave (Hz)
x = np.sin(2 * np.pi * f * t)

# Perform zero-padding
N = len(x)  # Length of the signal
M = 20 * N  # Length of the zero-padded signal
x_padded = np.pad(x, (0, M - N), 'constant')

# Compute the FFT
X = np.fft.fft(x_padded, M)

# Plot the magnitude spectrum
frequencies = np.fft.fftfreq(M, 1/fs)
plt.plot(frequencies, np.abs(X))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude Spectrum of the zero-padded sine wave of 1 kHz')
plt.xlim(980, 1020)
plt.grid(True)
plt.show()

# Apply Hanning window
window = np.hanning(M)
x_windowed = x_padded * window

# Compute the FFT
X_windowed = np.fft.fft(x_windowed, M)

# Plot the magnitude spectrum with Hanning window
plt.plot(frequencies, np.abs(X_windowed))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude Spectrum of the zero-padded sine wave of 1 kHz with Hanning window')
plt.xlim(980, 1020)
plt.grid(True)
plt.show()

