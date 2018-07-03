import matplotlib.pyplot as plt

year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
        2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

total_storms = [24393, 25045, 25195, 27108, 26701, 26918, 31352, 26657, 36184, 22936,
                21543, 29996, 22503, 19345, 18580, 19172, 20238, 21744]

tornadoes = [1072, 1219, 938, 1374, 1820, 1262, 1117, 1102, 1685, 1305,
             1543, 1894, 1119, 943, 1057, 1259, 1059, 1522]

hailstorms = [11223, 12143, 12485, 13857, 13088, 13640, 16566, 12637, 17680, 10223,
              5913, 9417, 7033, 5458, 5537, 5412, 5601, 6045]

windstorms = [12098, 11683, 11772, 11873, 11793, 12016, 13669, 12918, 16819, 11408,
              14087, 18685, 14351, 12944, 11986, 12501, 13578, 14177]

carbon_dioxide = [338.58, 371.14, 404.18, 375.8, 377.52, 379.8, 381.9, 383.79, 385.6, 387.43, 389.9,
                  391.65, 393.85, 396.52,398.65, 400.83, 404.21, 406.53]

sunspots = [2040 , 2027 , 2075 , 1352 , 854 , 580 , 342 , 158 , 55 , 82 , 325 , 872 , 1053 , 1188 , 1367 , 869 , 466 , 253]

geomagnetic_field =[ 178 , 153 , 164 , 245 , 177 , 154 , 103 , 97 , 79 , 51 , 70 , 90 , 96 , 90 , 102 , 149 , 139 , 128]

tropical_storms = [31 , 30 , 24 , 32 , 27 , 28 , 28 , 26 , 32 , 27 , 26 , 30 , 36 , 32 , 28 , 30 , 36 , 35]

radio_flux = [2129 , 2170 , 2124 , 1564 , 1296 , 1104 , 964 , 884 , 830 , 856 , 972 , 1308 , 1466 , 1500 , 1691 , 1427 , 1074 , 923]

plt.figure(1)
plt.title('Severe Weather - United States')
plt.subplot(211)
plt.plot(year, total_storms, lw=2, color='red')
plt.plot(year, hailstorms, lw=2, color='blue')
plt.plot(year, windstorms, lw=2, color='gray')
plt.legend(['Total Storms', 'Hailstorms', 'Windstorms'])
plt.grid(True)

plt.subplot(212)
plt.plot(year, tornadoes, lw=2, color='gray')
plt.plot(year, sunspots, lw=2, color='yellow')
plt.plot(year, radio_flux, lw=2, color='orange')
plt.xlabel('Years (2000 - 2017)')
plt.legend(['Tornadoes', 'Sunspots', 'Radio Flux'])
plt.grid(True)

plt.figure(2)
plt.subplot(211)
plt.plot(year, total_storms, lw=2, color='red')
plt.plot(year, hailstorms, lw=2, color='blue')
plt.plot(year, windstorms, lw=2, color='gray')
plt.legend(['Total Storms', 'Hailstorms', 'Windstorms'])
plt.grid(True)

plt.subplot(212)
plt.plot(year, tornadoes, lw=2, color='gray')
plt.legend(['Tornadoes'])
plt.xlabel('Years (2000 - 2017)')
plt.grid(True)

plt.figure(3)
plt.subplot(211)
plt.plot(year, geomagnetic_field, lw=2, color='brown')
plt.legend(['Geomagnetic Field'])
plt.grid(True)

plt.subplot(212)
plt.plot(year, tropical_storms, lw=2, color='green')
plt.legend(['Tropical Storms'])
plt.xlabel('Years (2000 - 2017)')
plt.grid(True)

plt.figure(4)
plt.subplot(211)
plt.plot(year, sunspots, lw=2, color='yellow')
plt.plot(year, radio_flux, lw=2, color='orange')
plt.legend(['Sunspots', 'Radio Flux'])
plt.grid(True)

plt.subplot(212)
plt.plot(year, geomagnetic_field, lw=2, color='brown')
plt.legend(['Geomagnetic Field'])
plt.xlabel('Years (2000 - 2017)')
plt.grid(True)

plt.figure(5)
plt.subplot(211)
plt.plot(year, geomagnetic_field, lw=2, color='brown')
plt.legend(['Geomagnetic Field'])
plt.grid(True)

plt.subplot(212)
plt.plot(year, tropical_storms, lw=2, color='green')
plt.legend(['Tropical Storms'])
plt.xlabel('Years (2000 - 2017)')
plt.grid(True)

plt.figure(6)
plt.subplot(211)
plt.plot(year, geomagnetic_field, lw=2, color='brown')
plt.legend(['Geomagnetic Field'])
plt.grid(True)

plt.subplot(212)
plt.plot(year, tornadoes, lw=2, color='gray')
plt.legend(['Tornadoes'])
plt.xlabel('Years (2000 - 2017)')
plt.grid(True)

plt.show()