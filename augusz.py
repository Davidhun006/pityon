
# Lehet e augusztus havi hóméséklet
# A legnagyobb hóméséklet
# A legkisebb hóméséklet
# Hány alkalommal volt a hőmeséklet 31 fok felett?
# mekkora volt a hómérséklet augusztus 20.-án?
# mekkora volt az átlag hőmérséklet?
# mekkora volt a hőingadoszás?
# Fájl írás
aug= [38,36,31,27,38,24,29,29,30,24,33,27,32,24,36,31,41,30,26,34,26,30,31,26,36,23,31,28,31,32,28]

legnagyobb= aug[0]
for num in aug:
    if num>legnagyobb:
        legnagyobb=num
print("legnagyobb",legnagyobb)

legkisebb= aug[0]
for num in aug:
    if num<legkisebb:
        legkisebb=num
print("legkisebb",legkisebb)

felett=0
for num in aug:
    if num>31:
        felett+=1
print("31fok felett",felett)

osszes=0
for num in aug:
    osszes=osszes+num

atlag=osszes/31
print("átlag:",atlag)

ingadozas=legnagyobb-legkisebb
print("ingadozás:",ingadozas)

ker=20
print("20adikai hőmérséklet",aug[ker+1])

wr=open("aug.txt","w")
wr.write(f'legnagyobb:{legnagyobb}\n')
wr.write(f'legkisebb:{legkisebb}\n')
wr.write(f'31fok felett:{felett}\n')
wr.write(f'átlag:{atlag}\n')
wr.write(f'ingadozás:{ingadozas}\n')
wr.write(f'20adikai hőmérséklet{aug[ker+1]}\n')
wr.close()
