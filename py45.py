szamok = []
osszeg = 0

while True:
    szam = int(input("Kérem, adjon meg egy egész számot -5 és 5 között: "))
    if szam < -5 or szam > 5:
        break
    szamok.append(szam)
    osszeg += szam

print("Az intervallumba eső számok:", szamok)
print("Az összegük:", osszeg)