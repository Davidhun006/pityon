import random
lista = []
for i in range(10):
    szám = random.randint(0,50)
    if szám % 4 == 0:
        lista.append(szám)

print(*lista, sep="\n")
print(f"{len(lista)} elemből áll a lista.")