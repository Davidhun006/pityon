import random

def alahuzas(alahuzas):
    print(alahuzas)

szam1 = int(input("Adjon meg egy számot: "))
szam2 = random.randint(10,50)
SZAM3 = 4

alahuzas([szam1,szam2,SZAM3])

if szam2%2 == 0:
    szam2+=1

if szam1%2 == 0:
    alahuzas("Páros")
else:
    alahuzas("Páratlan")

szamok = [szam1,szam2,SZAM3]

alahuzas(szamok.count(4))
szamok.sort()
alahuzas(szamok)
szamok.reverse()
alahuzas(szamok)
szamok.remove(4)
alahuzas(szamok)
szamok.clear()
alahuzas(szamok)

halmaz = {szam1,szam2,SZAM3}
halmaz.update({7})
alahuzas(halmaz)
halmaz.add(2)
alahuzas(halmaz)
halmaz.pop()
alahuzas(halmaz)
halmaz.remove(4)
alahuzas(halmaz)
halmaz.clear()
alahuzas(halmaz)
szamok = [szam1,szam2,SZAM3]
with open("szám.txt","w") as file:
    file.write(str(szamok))
    file.close()

file = open("szám.txt","r")
line = file.readline()
while line != "":
    alahuzas(line)
    line = file.readline()


file.close()
