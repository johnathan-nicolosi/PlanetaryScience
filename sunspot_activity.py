import matplotlib.pyplot as plt

year = [1700, 1701, 1702, 1703, 1704, 1705, 1706, 1707, 1708, 1709,
        1710, 1711, 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719,
        1720, 1721, 1722, 1723, 1724, 1725, 1726, 1727, 1728, 1729,
        1730, 1731, 1732, 1733, 1734, 1735, 1736, 1737, 1738, 1739,
        1740, 1741, 1742, 1743, 1744, 1745, 1746, 1747, 1748, 1749,
        1750, 1751, 1752, 1753, 1754, 1755, 1756, 1757, 1758, 1759,
        1760, 1761, 1762, 1763, 1764, 1765, 1766, 1767, 1768, 1769,
        1770, 1771, 1772, 1773, 1774, 1775, 1776, 1777, 1778, 1779,
        1780, 1781, 1782, 1783, 1784, 1785, 1786, 1787, 1788, 1789,
        1790, 1791, 1792, 1793, 1794, 1795, 1796, 1797, 1798, 1799,
        1800, 1801, 1802, 1803, 1804, 1805, 1806, 1807, 1808, 1809,
        1810, 1811, 1812, 1813, 1814, 1815, 1816, 1817, 1818, 1819,
        1820, 1821, 1822, 1823, 1824, 1825, 1826, 1827, 1828, 1829,
        1830, 1831, 1832, 1833, 1834, 1835, 1836, 1837, 1838, 1839,
        1840, 1841, 1842, 1843, 1844, 1845, 1846, 1847, 1848, 1849,
        1850, 1851, 1852, 1853, 1854, 1855, 1856, 1857, 1858, 1859,
        1860, 1861, 1862, 1863, 1864, 1865, 1866, 1867, 1868, 1869,
        1870, 1871, 1872, 1873, 1874, 1875, 1876, 1877, 1878, 1879,
        1880, 1881, 1882, 1883, 1884, 1885, 1886, 1887, 1888, 1889,
        1890, 1891, 1892, 1893, 1894, 1895, 1896, 1897, 1898, 1899,
        1900, 1901, 1902, 1903, 1904, 1905, 1906, 1907, 1908, 1909,
        1910, 1911, 1912, 1913, 1914, 1915, 1916, 1917, 1918, 1919,
        1920, 1921, 1922, 1923, 1924, 1925, 1926, 1927, 1928, 1929,
        1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 1939,
        1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949,
        1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959,
        1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969,
        1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979,
        1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
        1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999,
        2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009,
        2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

sunspots = [5, 11, 16, 23, 36, 58, 29, 20, 10, 8,
            3, 0, 0, 2, 11, 27, 47, 63, 60, 39,
            28, 26, 22, 11, 21, 40, 78, 122, 103, 73,
            47, 35, 11, 5, 16, 34, 70, 81, 111, 101,
            73, 40, 20, 16, 5, 11, 22, 40, 60, 80.9,
            83.4, 47.7, 47.8, 30.7, 12.2, 9.6, 10.2, 32.4, 47.6, 54,
            62.9, 85.9, 61.2, 45.1, 36.4, 20.9, 11.4, 37.8, 69.8, 106.1,
            100.8, 81.6, 66.5, 34.8, 30.6, 7, 19.8, 92.5, 154.4, 125.9,
            84.8, 68.1, 38.5, 22.8, 10.2, 24.1, 82.9, 132, 130.9, 118.1,
            89.9, 66.6, 60, 46.9, 41, 21.3, 16, 6.4, 4.1, 6.8,
            14.5, 34, 45, 43.1, 47.5, 42.2, 28.1, 10.1, 8.1, 2.5,
            0, 1.4, 5, 12.2, 13.9, 35.4, 45.8, 41.1, 30.1, 23.9,
            32.3, 54.3, 59.7, 63.7, 63.5, 52.2, 25.4, 13.1, 6.8, 6.3,
            70.9, 47.8, 27.5, 8.5, 13.2, 56.9, 121.5, 138.3, 103.2, 85.7,
            64.6, 36.7, 24.2, 10.7, 15, 40.1, 61.5, 98.5, 124.7, 96.3,
            66.6, 64.5, 54.1, 39, 20.6, 6.7, 4.3, 22.7, 54.8, 93.8,
            95.8, 77.2, 59.1, 44, 47, 30.5, 16.3, 7.3, 37.6, 74,
            139, 111.2, 101.6, 66.2, 44.7, 17, 11.3, 12.4, 3.4, 6,
            32.3, 54.3, 59.7, 63.7, 63.5, 52.2, 25.4, 13.1, 6.8, 6.3,
            7.1, 35.6, 73, 85.1, 78, 64, 41.8, 26.2, 26.7, 12.1,
            9.5, 2.7, 5, 24.4, 42, 63.5, 53.8, 62, 48.5, 43.9,
            18.6, 5.7, 3.6, 1.4, 9.6, 47.4, 57.1, 103.9, 80.6, 63.6,
            37.6, 26.1, 14.2, 5.8, 16.7, 44.3, 63.9, 69, 77.8, 64.9,
            35.7, 21.2, 11.1, 5.7, 8.7, 36.1, 79.7, 114.4, 109.6, 88.8,
            67.8, 47.5, 30.6, 16.3, 9.6, 33.2, 92.6, 151.6, 136.3, 134.7,
            83.9, 69.4, 31.5, 13.9, 4.4, 38, 141.7, 190.2, 184.8, 159,
            112.3, 53.9, 37.6, 27.9, 10.2, 15.1, 47, 93.8, 105.9, 105.5,
            104.5, 66.6, 68.9, 38, 34.5, 15.5, 12.6, 27.5, 92.5, 155.4,
            154.6, 140.4, 115.9, 66.6, 45.9, 17.9, 13.4, 29.4, 100.2,  157.6,
            142.6, 145.7, 94.3, 54.6, 29.9, 17.5, 8.6, 21.5, 64.3, 93.3,
            119.6, 110.9, 104.1, 63.6, 40.4, 29.8, 15.2, 7.6, 2.9, 3.1,
            16.5, 55.7, 57.6, 64.7, 79.3, 41.9, 23.9, 13.1]

plt.plot(year, sunspots)
plt.title('Yearly Mean Sunspot Numbers (1700 - 2017)')
plt.ylabel('Number of Sunspots')
plt.xlabel('Year')
plt.grid(True)
plt.show()