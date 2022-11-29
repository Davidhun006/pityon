# 1 A kitermelés 50 és 100 m3 között lehetséges naponta októberben!

# 2 A legnagyobb fakitermelés mennyiségét a tervszerint 

# 3 A legkisebb fakitermelés mennyiségét a tervszerint 

# 4 Hány alkalommal volt a fakitermelés mennyiségé 82 m3 felett?

# 5 mekkora volt a fakitermelés mennyisége októberi 20.-án?

# 6 mekkora volt a fakitermelés átlag mennyisége?

# Fájl írása fa.txt néven az amelyben az összes eredmény szerepel!
import random
fa=[]
for i in range(31):
    fa.append(random.randint(50,100))

print(fa)
max=0
for num in fa:
    if num>max:
        max=num
print("A legtöbb ",max)

min=100
for num in fa:
    if num<min:
        min=num
print("a legkevesebb ",min)

felett=0
for num in fa:
    if num>82:
        felett+=1
print("82m3 felett",felett)

ker=20
print("20adikai kitermelés",fa[ker+1])

osszes=0
for num in fa:
    osszes=osszes+num

atlag=osszes/31
print("átlag:",atlag)

wr=open("fa.txt","w")
wr.write(f'legnagyobb:{max}\n')
wr.write(f'legkisebb:{min}\n')
wr.write(f'31fok felett:{felett}\n')
wr.write(f'átlag:{atlag}\n')
wr.write(f'20adikai kitermelés{fa[ker+1]}\n')
wr.close()