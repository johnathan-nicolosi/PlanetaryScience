########################################################
#                                                      #
#              Standard Atmosphere Model               #
#            Written by Johnathan Nicolosi             #
#                                                      #
#                                                      #
########################################################

import math

# Obtain altitude (in feet) from user and convert to kilometers
h = float(input("Enter altitude (ft):"))
h_km = h / 3280.84


# Calculate temperature and pressure based on altitude
a3 = -4.5*10**-3  # K/m

if h > 82345 and h <= 155511:
    T = -205.05 + 0.00164 * h
    p = 51.97 * ((T + 459.7)/389.98)**-11.388

elif h > 36152 and h <= 82345:
    T = -70
    p = 473.1 * math.exp(1.73-0.000048 * h)

elif h < 36152:
    T = 59 - 0.00356 * h
    p = 2116 * ((T + 459.7)/518.6)**5.256

# Calculate density
d = p /(1718 * (T + 459.7))
d_metric = d * 515.379

# Convert pressure from psf to N/m**2
# p_n = p*47.88
p_n = p / 0.020885

# Convert termperature from F to C and then from C to K
C = (T-32) * (5/9)  # convert from Fahrenheit to Celsius
K = C + 273.15  # convert from Celsius to Kelvin

# Calculate the speed of sound and then convert it from m/s to knots
gamma = 1.4  # ratio of specific heats (for dry air)
M = 0.029 # molar mass - kg/mol
R = 8.314  # gas constant - J mol**-1 K**-1 (SI unit)
Rs = R / M  # specific gas constant - m**2 / s**2 / K
a = math.sqrt(gamma * Rs*K)  # results are measured in meters per second
a_knot = a * 1.944  # convert from m/s to knots

# Identify the atmopsheric layer based on altitude
atmospheric_layers = ["Outer Space", "Exosphere", "Thermopause", "Thermosphere", "Mesopause", "Mesosphere",
                      "Stratopause", "Stratosphere", "Tropopause", "Troposphere"]
print("")
if h_km > 555:
    a = 0
    d = 0
    T = 0
    print("Atmospheric Layer =", atmospheric_layers[0])

if h_km < 555 and h_km > 525:
    print("Atmospheric Layer =", atmospheric_layers[1])

if h_km < 525 and h_km > 515:
    print("Atmospheric Layer =", atmospheric_layers[2])

if h_km < 515 and h_km > 95:
    print("Atmospheric Layer =", atmospheric_layers[3])

if h_km < 85 and h_km > 75:
    print("Atmospheric Layer =", atmospheric_layers[4])

if h_km < 75 and h_km > 45:
    print("Atmospheric Layer =", atmospheric_layers[5])

if h_km < 45 and h_km > 40:
    print("Atmospheric Layer =", atmospheric_layers[6])

if h_km < 40 and h_km > 18:
    print("Atmospheric Layer =", atmospheric_layers[7])

if h_km < 18 and h_km > 14:
    print("Atmospheric Layer =", atmospheric_layers[8])

if h_km < 14 and h_km > 0:
    print("Atmospheric Layer =", atmospheric_layers[9])

if l > 0:
    hemisphere = "Northern Hemisphere"
elif l < 0:
    hemisphere = "Southern Hemisphere"
print("Hemisphere =", hemisphere)
if l == 66.5:
    print("Arctic Circle\n")
elif l == 23.5:
    print("Tropic of Cancer\n")
elif l == -23.5:
    print("Tropic of Capricorn\n")
elif l == -66.5:
    print("Antarctic Circle\n")

print("Altitude (h) = ", h, "ft:", "%.4f" % h_km, "km")
print("Pressure (p) =", "%.3f" % p, "psf:", "%.3f" % p_n, "N/m**2")
print("Density (d) =", "%.6f" % d, "slugs/cu ft:", "%.6f" % d_metric, "kg/m**3")
print("Temperature (T) =", "%.2f" % T, "(F)", "%.2f" % C, "(C)", "%.2f" % K, "(K)")
print("Speed of Sound (a) =", "%.1f" % a, "m/s:", "%.1f" % a_knot, "(knots)\n")

altitudes = [1, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000, 16000,
             17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000, 30000, 31000,
             32000, 33000, 34000, 35000, 36000, 37000, 38000, 39000, 40000, 41000, 42000, 43000, 44000, 45000, 46000,
             47000, 48000, 49000, 50000, 51000, 52000, 53000, 54000, 55000, 56000, 57000, 58000, 59000, 60000, 61000,
             62000, 63000, 64000, 65000, 66000, 67000, 68000, 69000, 70000, 71000, 72000, 73000, 74000, 75000, 76000,
             77000, 78000, 79000, 	80000, 81000, 82000, 83000, 84000, 85000, 86000, 87000, 88000, 89000, 90000, 91000,
             92000, 93000, 94000, 95000, 96000, 97000, 98000, 99000, 100000]
print("Alt Temp Pressure Density Speed of Sound")
for x in altitudes:
    if x > 82345 and x <= 100000:
        h = x
        T = -205.05 + 0.00164 * h
        C = (T - 32) * (5 / 9)  # convert from Fahrenheit to Celsius
        K = C + 273.15  # convert from Celsius to Kelvin
        p = 51.97 * ((T + 459.7) / 389.98) ** -11.388
        d = p /(1718 * (T + 459.7))
        a = math.sqrt(gamma * Rs * K)  # results are measured in meters per second
        a_knot = a * 1.944  # convert from m/s to knots

    elif x > 36152 and x <= 82345:
        h = x
        T = -70
        C = (T - 32) * (5 / 9)  # convert from Fahrenheit to Celsius
        K = C + 273.15  # convert from Celsius to Kelvin
        p = 473.1 * math.exp(1.73 - 0.000048 * h)
        d = p /(1718 * (T + 459.7))
        a = math.sqrt(gamma * Rs * K)  # results are measured in meters per second
        a_knot = a * 1.944  # convert from m/s to knots

    elif x < 36152:
        h = x
        T = 59 - 0.00356 * h
        C = (T - 32) * (5 / 9)  # convert from Fahrenheit to Celsius
        K = C + 273.15  # convert from Celsius to Kelvin
        p = 2116 * ((T + 459.7) / 518.6) ** 5.256
        d = p /(1718 * (T + 459.7))
        a = math.sqrt(gamma * Rs * K)  # results are measured in meters per second
        a_knot = a * 1.944  # convert from m/s to knots

    print(h, "%.2f" % T, "%.2f" % p, "%.6f" % d, "%.1f" % a_knot)

