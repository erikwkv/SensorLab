import numpy as np
from scipy.signal import freqs
import matplotlib.pyplot as plt


freqs = np.linspace(0.1,10000,100000)
R_2 = 6.6+11
L = 403e-3
# C_1 = 520e-6
C_2 = 470.1e-6


amp1 = np.abs(1/(1-(2*np.pi*freqs)**2*C_2*L+1j*(2*np.pi*freqs)*R_2*C_2))

fig, ax = plt.subplots(1,figsize=(10,10))

ax.set_xscale('log')
# ax.set_yscale('log')



w_c = np.sqrt((np.sqrt(C_2**2 *R_2**4 - 4*C_2*L *R_2**2 + 8*L**2) - C_2* R_2**2 + 2* L)/(C_2* L**2))/np.sqrt(2)
f_c = w_c/(2*np.pi)

print(f_c)

plt.plot(freqs,20*np.log10(amp1))
plt.axhline(y=-3,color='red',linestyle='--')
plt.axvline(x=f_c,color='red',linestyle='--')
plt.title(f"Frekvensrespons av pi-filteret")
plt.xlabel("Frekvens [Hz]")
plt.ylabel("Relativ amplitude [dB]")
plt.grid()
plt.show()

# sqrt((sqrt((470.1e-6)^2 (20)^4 - 4 *(470.1e-6)* (400e-3) *(20)^2 + 8 *(400e-3)^2) - (470.1e-6) *(20)^2 + 2*(400e-3))/((470.1e-6) *(400e-3)^2))/sqrt(2)