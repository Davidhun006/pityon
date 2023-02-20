import random

szam1 = random.randint(1,3)
szam = int(input("Kérlek adj meg egy számot 1 és 3 között: "))

if szam1 == szam:
    print("Az általad beírt szám egyenlő a gép által kitalált számmal. A te számod: ", szam, "a gép által gondolt szám: ", szam1 )

elif szam1 > szam:
    print("A gép által gondolt szám nagyobb mint az általad beírt szám. A te számod: ", szam, "a gép által gondolt szám: ", szam1 )

else:
   print("Az általad beírt szám nagyobb mint a gép által gondolt szám. A te számod: ", szam, "a gép által gondolt szám: ", szam1)