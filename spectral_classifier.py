########################################################
#                                                      #
#                 Spectral Classifier                  #
#            Written by Johnathan Nicolosi             #
#                                                      #
########################################################

import matplotlib.pyplot as plt
import numpy as np

h = 6.626e-34
c = 3.0e+8
k = 1.38e-23

def planck(wav, T):
    a = 2.0*h*c**2
    b = h*c/(wav*k*T)
    intensity = a/((wav**5) * (np.exp(b) - 1.0))
    return intensity

# generate x-axis in increments from 1nm to 3 micrometer in 1 nm increments
# starting at 1 nm to avoid wav = 0, which would result in division by zero.
wavelengths = np.arange(1e-9, 3e-6, 1e-9)

# intensity at 4000K, 5000K, 6000K, 7000K
intensity300 = planck(wavelengths, 300.)
intensity4000 = planck(wavelengths, 4000.)
intensity5000 = planck(wavelengths, 5000.)
intensity6000 = planck(wavelengths, 6000.)
intensity7000 = planck(wavelengths, 7000.)
intensity10000 = planck(wavelengths, 10000.)
intensity20000 = planck(wavelengths, 20000.)

fig = plt.figure()
fig.suptitle('Blackbody Radiation Curves')
ax = fig.add_subplot(111)
# ax.plot(x, wv, c='w', lw=2)

# Horizontal "axis" across the centre of the wave
# ax.axhline(c='w')
# Ditch the y-axis ticks and labels; label the x-axis
ax.set_ylabel('Power density ($10^{13} watts/m^3$)')
ax.set_xlabel(r'$\lambda\;(\mathrm{nm})$')

# Label and delimit the different regions of the electromagnetic spectrum
ax.text(1, 1.5, 'X Ray', color='k', verticalalignment='top', fontdict={'fontsize': 12})
ax.text(220, 1.5, 'UV', color='k', verticalalignment='top', fontdict={'fontsize': 12})
ax.text(480, 1.5, 'Visible', color='k', verticalalignment='top', fontdict={'fontsize': 12})
ax.text(1200, 1.5, ' Near Infrared', color='k', verticalalignment='top', fontdict={'fontsize': 12})
ax.text(2700, 1.5, ' IR', color='k', verticalalignment='top', fontdict={'fontsize': 12})

# Finally, add some colourful rectangles representing a rainbow in the
# visible region of the spectrum.
# Dictionary mapping of wavelength regions (nm) to approximate RGB values
rainbow_rgb = { (380, 440): '#8b00ff', (440, 460): '#4b0082',
                (460, 495): '#0000ff', (495, 570): '#00ff00',
                (570, 590): '#ffff00', (590, 620): '#ff7f00',
                (620, 750): '#ff0000', (750, 2200): '#E60000'}
for wv_range, rgb in rainbow_rgb.items():
    ax.axvspan(*wv_range, color=rgb, ec='none', alpha=1)

plt.hold(True) # doesn't erase plots on subsequent calls of plt.plot()
plt.plot(wavelengths*1e9, intensity4000, 'r-', label='4000 K')
plt.plot(wavelengths*1e9, intensity5000, 'g-', label='5000 K') # 5000K green line
plt.plot(wavelengths*1e9, intensity6000, 'b-', label='6000 K') # 6000K blue line
plt.plot(wavelengths*1e9, intensity7000, 'k-', label='7000 K') # 7000K black line

ax.legend()

# show the plot
plt.show()
