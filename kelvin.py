
cfok=int(input("Hány fok van"))
kelvin=cfok-(272.15)
print("ennyi fok van kelvinben", kelvin)
if cfok<18:
    print("hideg van mert magas a rezsi")
elif cfok>35:
    print("HU DE MELEG VAN")
else:
    print("megfelelő hőmérséklet")