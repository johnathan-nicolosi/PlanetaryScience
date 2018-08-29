#################################################
#                                               #
#          Celestial Object Classifier          #
#         Written by Johnathan Nicolosi         #
#                                               #
#################################################

print("Welcome to the Celestial Object Classifier")
print("")
print("Please enter 1 for yes and 0 for no")
print("")
orbits_sun = int(input("Orbits sun?"))
if orbits_sun == 1:
    is_sperical = int(input("Is spherical?"))
    if is_sperical == 1:
        orbits_planet = int(input("Also in orbit around a planet?"))
        if orbits_planet == 1:
            print("It is a moon")
        else:
            cleared_neighbourhood = int(input("Has cleared neighbourhood?"))
            if cleared_neighbourhood == 1:
                mostly_rock = int(input("Mostly made of rock?"))
                if mostly_rock == 1:
                    print("It is a terrestrial planet")
                else:
                    print("It is a gas giant")
            else:
                print("It is a dwarf planet")
    else:
        is_man_made = int(input("Is the object man-made?"))
        if is_man_made == 1:
            is_manned = int(input("Is it manned?"))
            if is_manned == 1:
                print("It is a spacecraft")
            else:
                print("It is a satellite")
        else:
            is_alien = int(input("Is alien-made?"))
            if is_alien == 1:
                print("It is a UFO")
            else:
                is_icy = int(input("Is icy?"))
                if is_icy == 1:
                    print("It is a Comet")
                else:
                    print("It is an asteroid")
else:
    is_sun = int(input("Converts hydrogen into helium?"))
    if is_sun == 1:
        print("It is a star")
    else:
        print("It is an extrasolar planet")
