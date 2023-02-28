print("Kérlek, adj meg néhány 'a' betűvel kezdődő szót! Ha nem 'a' illetve 'A' betűvel kezdődik, akkor azt kihagyjuk.")

szavak = []

while True:
    szo = input("Add meg az 'a' betűvel kezdődő szót: ")
    if szo == "":
        break
    elif szo[0] == "a":
        szavak.append(szo)
    elif szo[0] == "A":
        szavak.append(szo)

print("Az 'a' és 'A' betűvel kezdődő szavak, amiket megadtál:")
for szo in szavak:
    print(szo)