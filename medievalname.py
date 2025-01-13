#Marco Anaya
#Name generator project
print("Welcome to your Medieval name 2000")
def name():
    chip = input("Stale(s) or Fresh chips(f)?: ")
    if chip == "s":
        country1 = input("England(e) or Germany(g)? ")
        if country1 == "e":
            prof = input("Are you a farmer(f) or noble(n)?")
            if prof == "f": print("Your name is Bartholomew.")
            else: print("Your name is Ethelred")
        else:
            born = input("Were you fried(f) into existence or born normally(n)?")
            if born == "f":print("Your name is Björn")
            else: print("Your name is Gottfried")
    else:
        country2 = input("Spain(s)or France(f)?:")
        if country2 == "s":
            animal = input("Bird(b) or animal(a)?")
            if animal == "b": print("Your name is Falcona")
            else: print("Your name is Ordoño")
        else:
            pron = input("Do you want to be able to say your name? Yes(y) or no(n)?")
            if pron == "n": print("Your name is Yvonnet")
            else: print("Your name is Guy.")


name()
