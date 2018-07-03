################################################################################
#                                                                              #
#                                Solar System                                  #
#                        Written by Johnathan Nicolosi                         #
#                             Created June 9, 2018                             #
#                                                                              #
################################################################################

import matplotlib.pyplot as plt
import numpy as np
import math

# universal gravitational constant
G = 6.67408 * 10**-11 # Newton-meter^2/kilogram^2
gravitational_parameter = 3.986 * 10**5 # km^3/s^2

# The mass for each celestial body (in kilograms)
mass_mercury = 3.30 * 10**23
mass_venus = 4.87 * 10**24
mass_earth = 5.98 * 10**24
mass_mars = 6.42 * 10**23
mass_jupiter = 1.90 * 10**27
mass_saturn = 5.69 * 10**26
mass_uranus = 8.68 * 10**25
mass_neptune = 1.02 * 10**26
mass_sun = 1.99 * 10**30
mass_moon = 7.35 * 10**22

# The radius of each celestial body (in kilometers)
radius_mercury = 2439 * 10**3
radius_venus = 6051 * 10**3
radius_earth = 6378 * 10**3
radius_mars = 3393 * 10**3
radius_jupiter = 71492 * 10**3
radius_saturn = 60268 * 10**3
radius_uranus = 25559 * 10**3
radius_neptune = 24764 * 10**3
radius_sun = 696000 * 10**3
radius_moon = 1738 * 10**3

# The gravitational acceleration vector of each celestial body (in Newtons)
gravity_mercury = G * mass_mercury / radius_mercury**2
gravity_venus = G * mass_venus / radius_venus**2
gravity_earth = G * mass_earth / radius_earth**2
gravity_mars = G * mass_mars / radius_mars**2
gravity_jupiter = G * mass_jupiter / radius_jupiter**2
gravity_saturn = G * mass_saturn / radius_saturn**2
gravity_uranus = G * mass_uranus / radius_uranus**2
gravity_neptune = G * mass_neptune / radius_neptune**2
gravity_sun = G * mass_sun / radius_sun**2
gravity_moon = G * mass_moon / radius_moon**2

# Distance of planet from from sun (as list)
distance_sun = [58000000, 108000000, 150000000, 228000000, 778000000, 1432000000, 2871000000, 4498000000, 5914000000]

# List of known planets orbiting the sun
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

solar_system_bodies  = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Sun', 'Moon']
# Create a list of the gravitational fields of each planet
gravity_planets = [gravity_mercury, gravity_venus, gravity_earth, gravity_mars, gravity_jupiter, gravity_saturn,
                   gravity_uranus, gravity_neptune, gravity_sun, gravity_moon]

# Distance of planet from sun (as dictionary)
distance_from_sun = {
    "Mercury": 58,
    "Venus": 108,
    "Earth": 150,
    "Mars": 228,
    "Jupiter": 778,
    "Saturn": 1432,
    "Uranus": 2871,
    "Neptune": 4498,
    "Pluto": 5914
}

# Orbit of planet (in Earth days)
orbital_periods = [87.98, 224.7, 365.36, 686.98, 11.86, 29.41, 84.04, 164.8, 248.6]

# Rotation of planet along its axis of rotation (in hours)
rotational_periods = [58.65, 5832.24, 24, 24.56, 9.89, 10.24, 17.25, 16.10, 153.36]

# Primary Foci or Radius of Perigee measures closest approach (in km)
radius_perigee = [46000000, 107500000, 147100000, 206700000, 740900000, 1348000000, 2871000000, 4456000000, 4447000000]

# Vacant Foci or Radius of Apogee measures closest approach (in km)
radius_apogee = [69800000, 108900000, 152100000, 249100000, 815700000, 1503000000, 3003000000, 4546000000, 7380000000]

# Angle of axial tilt (in deg)
axial_inclination = [0, 117.4, 23.5, 23.98, 3.1, 27, 97.9, 29.6, 119.6]

# Angle of orbit to the ecliptic plane
angle_orbit_ecliptic = [7, 3.4, 0, 1.85, 1.3, 2.48, 0.77, 1.77, 17.1]

# Number of natural or captured satellites
number_satellites = [0, 0, 1, 2, 61, 31, 27, 13, 2]

# Mean surface temperature of planetary body (in C)
mean_surface_temp = [430, 480, 22, -23, -150, -80, -215, -220, -230]

# Strength of planetary magnetic field (in gauss)
magnetic_field_strength = [0.003, 0.00002, 0.31, 0.0003, 4.28, 0.22, 0.23, 0.14,0]

# Eccentricity of each planet's orbit around the sun
planetary_eccentricity = [0.205, 0.007, 0.017, 0.094, 0.049, 0.057, 0.046, 0.011, 0.244]

# Orbital velocity of each planetary body (in km/s)
orbital_velocity = [47.4, 35, 29.8, 24, 13.1, 9.7, 6.8, 5.4, 4.7]

# Due to its proximity near the sun, Mercury does not possess an atmosphere
mercury_atmosphere = {
    "Argon": 0,
    "Carbon dioxide": 0,
    "Helium": 0,
    "Hydrogen": 0,
    "Methane": 0,
    "Nitrogen": 0,
    "Other": 0
}

# Venus atmosphere is thick with carbon dioxide
venus_atmosphere = {
    "Argon": 0,
    "Carbon dioxide": 96,
    "Helium": 0,
    "Hydrogen": 0,
    "Methane": 0,
    "Nitrogen": 3.2,
    "Other": 0.8
}

# Earth's atmospheric gases
earth_atmosphere = {
    "Argon": 0.9,
    "Carbon dioxide": 0,
    "Helium": 0,
    "Hydrogen": 0,
    "Methane": 0,
    "Nitrogen": 78,
    "Other": 0.1
}

# Mars' atmospheric gases
mars_atmosphere = {
    "Argon": 1.6,
    "Carbon dioxide": 95,
    "Helium": 0,
    "Hydrogen": 0,
    "Methane": 0,
    "Nitrogen": 2.7,
    "Other": 0.7
}

# Jupiter's atmospheric gases
jupiter_atmosphere = {
    "Argon": 0,
    "Carbon dioxide": 0,
    "Helium": 10,
    "Hydrogen": 90,
    "Methane": 0,
    "Nitrogen": 0,
    "Other": 0
}

# Saturn's atmospheric gases
saturn_atmosphere = {
    "Argon": 0,
    "Carbon dioxide": 0,
    "Helium": 4,
    "Hydrogen": 96,
    "Methane": 0,
    "Nitrogen": 0,
    "Other": 0
}

# Uranus' atmospheric gases
uranus_atmosphere = {
    "Argon": 0,
    "Carbon dioxide": 0,
    "Helium": 15,
    "Hydrogen": 83,
    "Methane": 2,
    "Nitrogen": 0,
    "Other": 0
}

# Neptune's atmospheric gases
neptune_atmosphere = {
    "Argon": 0,
    "Carbon dioxide": 0,
    "Helium": 18,
    "Hydrogen": 79,
    "Methane": 3,
    "Nitrogen": 0,
    "Other": 0
}

# Pluto's atmospheric gases
pluto_atmosphere = {
    "Argon": 0,
    "Carbon dioxide": 0,
    "Helium": 0,
    "Hydrogen": 0,
    "Methane": 0,
    "Nitrogen": 90,
    "Other": 10
}

major_axis_earth = radius_apogee[2] + radius_perigee[2]
distance_between_foci_earth = radius_apogee[2] - radius_perigee[2]
a = int(radius_apogee[2])
b = int(radius_perigee[2])
minor_axis_earth = math.sqrt((a + b)**2 - (distance_between_foci_earth**2))

print("Orbital Geometry (Earth)")
print("Distance from Sun:", distance_sun[2], "(km)")
print("Rp (Earth):", radius_perigee[2], "(km)")
print("Ra (Earth)", radius_apogee[2], "(km)")
print("2a (Earth)", major_axis_earth, "(km)")
print("2b (Earth)", "%.0f" % minor_axis_earth, "(km)")
print("2c (Earth)", distance_between_foci_earth, "(km)")
print("##########################################")

print("Orbital Geometry (Neptune)")
print("Distance from Sun:", distance_sun[7], "(km)")

plt.figure(1)
plt.barh(planets, distance_sun, color=(0.1, 0.1, 0.1, 0.1),  edgecolor='blue')
# plt.xticks(rotation='vertical')
plt.xlabel('Distance (km)')
plt.ylabel('Planets')
plt.title('Distance of each planet from the Sun')

##############################################
# This section turns off scientific notation #
##############################################
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_scientific(False)
##############################################

plt.figure(2)
plt.barh(solar_system_bodies, gravity_planets, color=(0.1, 0.1, 0.1, 0.1),  edgecolor='blue')
plt.xlabel('Gravity (N)')
plt.ylabel('Planets')
plt.title('Gravitational Field of each solar body')

plt.figure(3)
plt.bar(planets, orbital_periods, color=(0.1, 0.1, 0.1, 0.1),  edgecolor='blue')
plt.xlabel('Planets')
plt.ylabel('Orbital Period - Days')
plt.title('Orbital Period of Planets (1 Solar Orbit)')

plt.figure(4)
plt.bar(planets, rotational_periods, color=(0.1, 0.1, 0.1, 0.1),  edgecolor='blue')
plt.xlabel('Planets')
plt.ylabel('Rotational Period - Hours')
plt.title('Rotational Period of Planets (1 Day)')

plt.figure(5)
plt.bar(planets, orbital_velocity, color=(0.1, 0.1, 0.1, 0.1),  edgecolor='blue')
plt.ylabel('Orbital Velocity (km/s)')
plt.title('Orbital Velocity of Planets Around the Sun')

plt.figure(6)
plt.bar(planets, mean_surface_temp, color=(0.1, 0.1, 0.1, 0.1),  edgecolor='blue')
plt.ylabel('Mean Surface Temp (C)')
plt.title('Mean Surface Temperature of Each Planet')

plt.figure(7)
plt.bar(planets, axial_inclination, color=(0.1, 0.1, 0.1, 0.1),  edgecolor='blue')
plt.ylabel('Axial Inclination (deg)')
plt.title('Angle of Axial Tilt for Each Planet')

plt.figure(8)
plt.bar(planets, planetary_eccentricity, color=(0.1, 0.1, 0.1, 0.1),  edgecolor='blue')
plt.ylabel('Eccentricity')
plt.title('Eccentricity for Each Planet')

plt.show()