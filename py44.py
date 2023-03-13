import random

lista = []
for i in range(5):
    lista.append(random.randint(1, 10))

osszeg = 0
for szam in lista:
    if szam % 2 == 0:
        osszeg += szam

print("A lista elemei:", lista)
print("Az összegük (csak a páros számoké):", osszeg)