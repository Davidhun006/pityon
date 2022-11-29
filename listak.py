ps=[10,20,30,40]
qs=["alma","eper","barack"]
print(ps)
print(qs)

zs=["hello",2.0,5,[10,20]]
print(zs[3])
print(zs)

szotar=["alma","sajt","kutya"]
szamok=[17,123]
ures_lista=[]
print(szotar,szamok,ures_lista)

print(szamok[0])
for i in enumerate(szamok):
    print(i)

for(i,ert) in enumerate(szamok):
    szamok[1]=ert**2
    print(szamok[i])

for(i,v) in enumerate(["banán","alma","körte","citrom"]):
    print(i,v)

slista=[]
slista.append(6)
slista.append(20)
slista.append(4)
slista.append(16)
print(slista)

slista.insert(1,10)
print(slista)

slista.insert(1,16)
print(slista)

print(slista.count(16))

slista.extend([5,9,5,11])
print(slista)

print(slista.index(9))

slista.reverse()
print(slista)

slista.sort()
print(slista)

slista.remove(16)
print(slista)

szlista=["barack","alma","mandarin"]
szlista.sort()
print(szlista)
szlista2=["én","te","ő","mi","ti","ők"]
szlista2.sort()
print(szlista2)