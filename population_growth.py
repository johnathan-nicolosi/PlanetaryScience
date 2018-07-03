
year = 1
age = 0
aveLifeSpanMale = 60
aveLifeSpanFemale = 70
ageFirstChild = 20
ageSecondChild = 22
aveNumChildren = 2
startingPopulation = 2
population = startingPopulation
birthRate = 0.11
deathRate = 0.1

for currentYear in range(1, 6001):
    print("Current Year:", currentYear, "\tCurrent Population:", "%.1f" % population)
    population = population + (birthRate * population) - (deathRate * population)