import random
szamok=[]
for i in range(20):
    szam=random.randint(1,12)
    szamok.append(szam)

hámal=0
for szam in szamok:
    if szam%3==0:
        hámal+=1
    
print('ennyi hárommal osztható szám volt',hámal)