import random

lista = []
for i in range(5):
    lista.append(random.randint(1, 10))

osszeg = sum(lista)

print("A lista elemei:", lista)
print("Az összegük:", osszeg)