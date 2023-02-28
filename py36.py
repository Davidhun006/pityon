betuk = []
while True:
    betu = input("Kérem adjon meg egy betűt (ENTER-el végezhet): ")
    if betu == "":
        break
    betu = betu.lower()
    if betu in betuk:
        print("Ezt a betűt már rögzítettem.")
    else:
        betuk.append(betu)
        betuk.sort(key=lambda x: (x.isupper(), x))
    print("Már rögzített betűk: ", betuk)