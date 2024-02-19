import numpy as np
import matplotlib.pyplot as plt

muabo = np.genfromtxt("./muabo.txt", delimiter=",")
muabd = np.genfromtxt("./muabd.txt", delimiter=",")

red_wavelength = 605 # Replace with wavelength in nanometres
green_wavelength = 515 # Replace with wavelength in nanometres
blue_wavelength = 460 # Replace with wavelength in nanometres
7
wavelength = np.array([red_wavelength, green_wavelength, blue_wavelength])

def mua_blood_oxy(x): return np.interp(x, muabo[:, 0], muabo[:, 1])
def mua_blood_deoxy(x): return np.interp(x, muabd[:, 0], muabd[:, 1])

bvf = 0.01 # Blood volume fraction, average blood amount in tissue
oxy = 0.8 # Blood oxygenation

# Absorption coefficient ($\mu_a$ in lab text)
# Units: 1/m
mua_other = 25 # Background absorption due to collagen, et cetera
mua_blood = (mua_blood_oxy(wavelength)*oxy # Absorption due to
            + mua_blood_deoxy(wavelength)*(1-oxy)) # pure blood
mua = mua_blood*bvf + mua_other

# reduced scattering coefficient ($\mu_s^\prime$ in lab text)
# the numerical constants are thanks to N. Bashkatov, E. A. Genina and
# V. V. Tuchin. Optical properties of skin, subcutaneous and muscle
# tissues: A review. In: J. Innov. Opt. Health Sci., 4(1):9-38, 2011.
# Units: 1/m
musr = 100 * (17.6*(wavelength/500)**-4 + 18.78*(wavelength/500)**-0.22)

# mua and musr are now available as shape (3,) arrays
# Red, green and blue correspond to indexes 0, 1 and 2, respectively

# TODO calculate penetration depth
#delta formula
delta = np.sqrt(1/(3*(mua + musr)*mua))

print(delta)

def phi_of_z(z, mua, musr, delta):
    C = np.sqrt(3*mua*(musr+mua))
    phi_0 = 1/(2*delta*mua)
    return phi_0 * np.exp(-C*z)

def transmittance(z, mua, musr, delta):
    phi_0 = 1/(2*delta*mua)
    transmitted = phi_of_z(z, mua, musr, delta)
    percent = (transmitted/phi_0)*100
    return percent

print(transmittance(0.000874, mua, musr, delta))


# TODO C: calculate depth of penetration

def probedepth(reflectance_IS_phi_z_divided_by_phi_zero):
    -np.log(reflectance_IS_phi_z_divided_by_phi_zero)/2

def penetration_depth(wavelength_nm, mua):
    wavelength= wavelength_nm*10**-9
    
    mua_other = 25 # Background absorption due to collagen, et cetera
    mua_blood = (mua_blood_oxy(wavelength)*oxy # Absorption due to
                + mua_blood_deoxy(wavelength)*(1-oxy)) # pure blood
    mua = mua_blood*bvf + mua_other

    
    musr = 100 * (17.6*(wavelength/500)**-4 + 18.78*(wavelength/500)**-0.22)
    delta = np.sqrt(1/(3*(mua + musr)*mua))

    return 


freq_range = np.linspace(380, 800, 100) # wavelength range from 380 to 800 nm

penetration_depth_range = [penetration_depth(wavelength, mua) for wavelength in freq_range]
plt.plot(freq_range, penetration_depth_range)
plt.xlabel('Wavelength (nm)')
plt.ylabel('Penetration Depth')
plt.title('Penetration Depth vs Frequency')
plt.show()