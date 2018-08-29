
################################################################################
#                                                                              #
#                              Solar System Model                              #
#                        Written by Johnathan Nicolosi                         #
#                           Created August 28, 2018                            #
#                                                                              #
################################################################################

import matplotlib.pyplot as plt

radius_list = [2439700, 6051800, 6378800, 3396200, 71492000, 60268000, 25559000, 24764000, 695700000]

distance_meters = [58000000000, 108000000000, 150000000000, 228000000000, 778000000000, 1432000000000, 2871000000000,
                   4498000000000]

fig = plt.figure('Solar System')
ax = fig.add_subplot(111)

plt.title('Solar System - 08/28/2018')
plt.axes()

# Sun - host star
sun = plt.Circle((0, 0), radius=radius_list[8], fc='y')
plt.gca().add_patch(sun)

# Mercury - orbital path
orbit_mercury = plt.Circle((0, 0), radius=distance_meters[0], fc='none', ec='black')
plt.gca().add_patch(orbit_mercury)
# Mercury - planet
mercury = plt.Circle((41024400000, 41000000000), radius=radius_list[0], fc='orange')
plt.gca().add_patch(mercury)
# Mercury - label
mercury_label = ax.annotate('Mercury', xy=(41031000000, 41007000000), xytext=(41031000000, 41007000000),
                            horizontalalignment='left')

# Venus - orbital path
orbit_venus = plt.Circle((0, 0), radius=distance_meters[1], fc='none', ec='black')
plt.gca().add_patch(orbit_venus)
# Venus - planet
venus = plt.Circle((28808200000, -104086820000), radius=radius_list[1], fc='gray')
plt.gca().add_patch(venus)
# Venus - label
venus_label = ax.annotate('Venus', xy=(28820000000, -104100000000), xytext=(28820000000, -104100000000),
                          horizontalalignment='left')

# Earth - orbital path
orbit_earth = plt.Circle((0, 0), radius=distance_meters[2], fc='none', ec='black')
plt.gca().add_patch(orbit_earth)
# Earth - planet
earth = plt.Circle((140762580000, -51824100000), radius=radius_list[2], fc='b')
plt.gca().add_patch(earth)
# Earth - label
earth_label = ax.annotate('Earth', xy=(140770000000, -51830000000), xytext=(140770000000, -51830000000),
                          horizontalalignment='left')

# Mars - orbital path
orbit_mars = plt.Circle((0, 0), radius=radius_list[3], fc='none', ec='black')
plt.gca().add_patch(orbit_mars)
# Mars - planet
mars = plt.Circle((165635450000, -156681000000), radius=radius_list[3], fc='r')
plt.gca().add_patch(mars)
# Mars - label
mars_label = ax.annotate('Mars', xy=(165650000000, -156680000000), xytext=(165650000000, -156680000000),
                         horizontalalignment='left')

# Jupiter - orbital path
orbit_jupiter = plt.Circle((0, 0), radius=distance_meters[4], fc='none', ec='black')
plt.gca().add_patch(orbit_jupiter)
# Jupiter - planet
jupiter = plt.Circle((-447786000000, -636219000000), radius=radius_list[4], fc='tan')
plt.gca().add_patch(jupiter)
# Jupiter - label
jupiter_label = ax.annotate('Jupiter', xy=(-447700000000, -636057000000), xytext=(-447700000000, -636057000000),
                            horizontalalignment='left')

# Saturn - orbital path
orbit_saturn = plt.Circle((0, 0), radius=distance_meters[5], fc='none', ec='black')
plt.gca().add_patch(orbit_saturn)
# Saturn - planet
saturn = plt.Circle((150330000000, -1424091000000), radius=radius_list[5], fc='brown')
plt.gca().add_patch(saturn)
# Saturn - label
saturn_label = ax.annotate('Saturn', xy=(150400000000, -1424150000000), xytext=(150400000000, -1424150000000),
                           horizontalalignment='left')

# Uranus - orbital path
orbit_uranus = plt.Circle((0, 0), radius=distance_meters[6], fc='none', ec='black')
plt.gca().add_patch(orbit_uranus)
# Uranus - planet
uranus = plt.Circle((2488765800000, 1431320000000), radius=radius_list[6], fc='b')
plt.gca().add_patch(uranus)
# Uranus - label
uranus_label = ax.annotate('Uranus', xy=(2488900000000, 1431300000000), xytext=(2488900000000, 1431300000000),
                           horizontalalignment='left')

# Neptune - orbital path
orbit_neptune = plt.Circle((0, 0), radius=distance_meters[7], fc='none', ec='black')
plt.gca().add_patch(orbit_neptune)
# Neptune - planet
neptune = plt.Circle((4430207000000, -778054000000), radius=radius_list[7], fc='b')
plt.gca().add_patch(neptune)
# Neptune - label
neptune_label = ax.annotate('Neptune', xy=(4430200000000, -778050000000), xytext=(4430170000000, -778040000000),
                            horizontalalignment='right')

plt.ylabel('Distance in meters')
plt.xlabel('Distance in meters')

plt.axis('scaled')
plt.show()
