print("Kérlek, adj meg néhány 'a' betűvel kezdődő szót! Ha nem 'a' betűvel kezdődik, akkor azt kihagyjuk.")

szavak = []

while True:
    szo = input("Add meg az 'a' betűvel kezdődő szót: ")
    if szo == "":
        break
    elif szo[0] == "a":
        szavak.append(szo)

print("Az 'a' betűvel kezdődő szavak, amiket megadtál:")
for szo in szavak:
    print(szo)