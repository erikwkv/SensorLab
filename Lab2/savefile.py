import matplotlib.pyplot as plt
from raspi_import import raspi_import
import numpy as np
from scipy.signal import find_peaks

sample_period, data = raspi_import('Lab2/theta-measurements/a180out-2024-01-08-10.00.25.bin')



# Plotting the data
time_axis = 1e3*sample_period*np.arange(len(data))

mic_3_ac = (data[1:,0] - np.mean(data[:,0]))*0.00081
mic_1_ac = (data[1:,1] - np.mean(data[:,1]))*0.00081
mic_2_ac = (data[1:,2] - np.mean(data[:,2]))*0.00081


time_axis = 1e3*sample_period*np.arange(len(data)-1)
# plt.plot(time_axis,mic_1_ac,label='Mic 1')
# plt.plot(time_axis,mic_2_ac,label='Mic 2')
# plt.plot(time_axis,mic_3_ac,label='Mic 3')
# plt.legend()
# plt.show()

#new time axis for the autocorrelation


up_factor = 4

x_vals = np.linspace(-len(mic_1_ac)/2,len(mic_1_ac)/2,len(mic_1_ac)*up_factor)
x_in = np.linspace(-len(mic_1_ac)/2,len(mic_1_ac)/2,len(mic_1_ac))

mic_1_interp = np.interp(x_vals,x_in,mic_1_ac)
mic_2_interp = np.interp(x_vals,x_in,mic_2_ac)
mic_3_interp = np.interp(x_vals,x_in,mic_3_ac)

# plt.plot(x_vals,mic_1_interp,'-x',label='Interpolated')
# plt.plot(x_in,mic_1_ac,'o',label='Original')
# plt.legend()
# plt.grid()
# plt.show()

# auto_corr_1 = np.correlate(mic_1_interp,mic_1_interp,mode='same')


# plt.plot(time_axis2,auto_corr_1)
# plt.xlabel('Time [ms]')
# plt.ylabel('Amplitude')
# plt.show()

print('beginning cross-correlation')
crosscorr_2_1 = np.correlate(mic_2_interp,mic_1_interp,mode='same')
print('done crosscorr 2-1')
crosscorr_3_1 = np.correlate(mic_3_interp,mic_1_interp,mode='same')
print('done crosscorr 3-1')
crosscorr_3_2 = np.correlate(mic_3_interp,mic_2_interp,mode='same')
print('done crosscorr 3-2')

time_axis2 = 1e3*sample_period*np.linspace(-len(data)/2,len(data)/2,len(crosscorr_2_1))

# peaks2_1, _ = find_peaks(crosscorr_2_1,distance=1)
# peaks3_1, _ = find_peaks(crosscorr_3_1,distance=1)
# peaks3_2, _ = find_peaks(crosscorr_3_2,distance=1)

# x_maxima = time_axis2[peaks3_1]

# plt.plot(time_axis2,crosscorr_2_1)
# plt.plot(x_maxima,crosscorr_2_1[peaks3_1],'ro')
# plt.show()

fig, ax = plt.subplots(3,1)
ax[0].plot(time_axis2,crosscorr_2_1)
# ax[0].plot(x_maxima,crosscorr_2_1[peaks2_1],'ro')
ax[0].set_title('Cross-correlation between Mic 2 and Mic 1')
ax[0].set_xlabel('Time [ms]')
ax[0].set_ylabel('Amplitude')
ax[0].set_xlim([-.5,.5])

ax[1].plot(time_axis2,crosscorr_3_1)
# ax[1].plot(x_maxima,crosscorr_3_1[peaks3_1],'ro')
ax[1].set_title('Cross-correlation between Mic 3 and Mic 1')
ax[1].set_xlabel('Time [ms]')
ax[1].set_ylabel('Amplitude')
ax[1].set_xlim([-.5,.5])


ax[2].plot(time_axis2,crosscorr_3_2)
# ax[2].plot(x_maxima,crosscorr_3_2[peaks3_2],'ro')
ax[2].set_title('Cross-correlation between Mic 3 and Mic 2')
ax[2].set_xlabel('Time [ms]')
ax[2].set_ylabel('Amplitude')
ax[2].set_xlim([-.5,.5])

plt.tight_layout()
plt.show()

#slice cross-correlation to only look at the peaks around 0
slice = 30
crosscorr_2_1 = crosscorr_2_1[int(len(crosscorr_2_1)/2)-slice:int(len(crosscorr_2_1)/2)+slice]
crosscorr_3_1 = crosscorr_3_1[int(len(crosscorr_3_1)/2)-slice:int(len(crosscorr_3_1)/2)+slice]
crosscorr_3_2 = crosscorr_3_2[int(len(crosscorr_3_2)/2)-slice:int(len(crosscorr_3_2)/2)+slice]
time_axis2 = 1e3*sample_period*np.linspace(-slice,slice,len(crosscorr_2_1))

peaks2_1, _ = find_peaks(crosscorr_2_1)
peaks3_1, _ = find_peaks(crosscorr_3_1)
peaks3_2, _ = find_peaks(crosscorr_3_2)

# plt.plot(time_axis2,crosscorr_2_1)
# plt.plot(time_axis2[peaks2_1],crosscorr_2_1[peaks2_1],'ro')
# plt.show()

fig, ax = plt.subplots(3,1)
ax[0].plot(time_axis2,crosscorr_2_1)
ax[0].plot(time_axis2[peaks2_1],crosscorr_2_1[peaks2_1],'ro')
ax[0].set_title('Cross-correlation between Mic 2 and Mic 1')
ax[0].set_xlabel('Time [ms]')
ax[0].set_ylabel('Amplitude')
ax[0].set_xlim([-slice*sample_period*1e3,slice*sample_period*1e3])

ax[1].plot(time_axis2,crosscorr_3_1)
ax[1].plot(time_axis2[peaks3_1],crosscorr_3_1[peaks3_1],'ro')
ax[1].set_title('Cross-correlation between Mic 3 and Mic 1')
ax[1].set_xlabel('Time [ms]')
ax[1].set_ylabel('Amplitude')
ax[1].set_xlim([-slice*sample_period*1e3,slice*sample_period*1e3])

ax[2].plot(time_axis2,crosscorr_3_2)
ax[2].plot(time_axis2[peaks3_2],crosscorr_3_2[peaks3_2],'ro')
ax[2].set_title('Cross-correlation between Mic 3 and Mic 2')
ax[2].set_xlabel('Time [ms]')
ax[2].set_ylabel('Amplitude')
ax[2].set_xlim([-slice*sample_period*1e3,slice*sample_period*1e3])

plt.tight_layout()
plt.show()

#find values of the peaks
time_2_1 = time_axis2[peaks2_1]
time_3_1 = time_axis2[peaks3_1]
time_3_2 = time_axis2[peaks3_2]

print('Time 2-1:',time_2_1)
print('Time 3-1:',time_3_1)
print('Time 3-2:',time_3_2)

def find_angle(t21,t31,t32):
    angle = np.arctan(np.sqrt(3)*(t21+t31)/(t21-t31-2*t32))
    return angle

angle_limited = find_angle(time_2_1,time_3_1,time_3_2)
if angle_limited < 0:
    angle_return = (angle_limited + np.pi)*(180/np.pi)
else:
    angle_return = angle_limited*(180/np.pi)

print(angle_return)
