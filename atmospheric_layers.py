
import matplotlib.pyplot as plt
# Atmospheric layers
fig = plt.figure('Atmospheric Layers')
ax = fig.add_subplot(111)
# Altitude in feet from sea level to 100000 ft
altitude = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 25000, 30000, 35000, 40000,
            45000, 50000, 55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 95000, 100000]
# Temperature in degrees Kelvin from sea level to 100000 ft
temp_kelvin = [288.15, 286.15, 284.15, 282.25, 280.25, 278.25, 276.25, 274.25, 272.25, 270.35, 268.35, 258.45, 248.55,
               238.65, 228.75, 218.85, 216.65, 216.65, 216.65, 216.65, 216.65, 216.65, 216.65, 216.65, 216.65, 219.35,
               223.96, 228.55, 233.05]

# Atmospheric pressure, measured in bars from sea level to 100000 ft
pressure = [101325, 97773, 94322, 90971, 87718, 84560, 81494, 78520, 75634, 72835, 70121, 57752, 46575, 37757, 30346,
            24163, 18799, 14854, 11737, 9132, 7218, 5705, 4440, 3566, 2776, 2163, 1746, 1374, 1086]

# Density of air from sea level to 100000 ft
density = [1.2250, 1.1901, 1.1560, 1.1226, 1.09, 1.0581, 1.0269, 0.9965, 0.9667, 0.9377, 0.9093, 0.777, 0.6528, 0.5508,
           0.4615, 0.3837, 0.3023, 0.2388, 0.1887, 0.1468, 0.1161, 0.092, 0.071, 0.057, 0.045, 0.034, 0.0272, 0.02097,
           0.0162]

plt.axes()
plt.title('Standard Atmospheric Layers')

# Earth - thermosphere
thermosphere = plt.Circle((0, -6378000), radius=6903800, fc='lightskyblue')
plt.gca().add_patch(thermosphere)
# thermopause_label = ax.annotate('Thermopause', xy=(0, 0), xytext=(0, 500000), horizontalalignment='right')
# thermosphere_label = ax.annotate('Thermosphere', xy=(0, 0), xytext=(10000, 150000), horizontalalignment='left')

# Earth - mesosphere
mesosphere = plt.Circle((0, -6378000), radius=6473800, fc='deepskyblue')
plt.gca().add_patch(mesosphere)
# mesopause_label = ax.annotate('Mesopause', xy=(0, 0), xytext=(0, 92000), horizontalalignment='right')
# mesosphere_label = ax.annotate('Mesosphere', xy=(0, 0), xytext=(10000, 70000), horizontalalignment='left')

# Earth - stratosphere
stratosphere = plt.Circle((0, -6378000), radius=6423800, fc='mediumblue')
plt.gca().add_patch(stratosphere)
# stratopause_label = ax.annotate('Stratopause', xy=(0, 0), xytext=(0, 42000), horizontalalignment='right')
# stratosphere_label = ax.annotate('Stratosphere', xy=(0, 0), xytext=(10000, 34000), horizontalalignment='left')

# Earth - mesosphere
troposphere = plt.Circle((0, -6378000), radius=6393800, fc='darkblue')
plt.gca().add_patch(troposphere)
# tropopause_label = ax.annotate('Tropopause', xy=(0, 0), xytext=(0, 12000), horizontalalignment='right')
# troposphere_label = ax.annotate('Troposphere', xy=(0, 0), xytext=(7000, 10000), horizontalalignment='left')

# Earth - planet
earth = plt.Circle((0, -6378000), radius=6378800, fc='green')
plt.gca().add_patch(earth)
plt.ylabel('distance in meters')


plt.axis('scaled')
plt.show()
