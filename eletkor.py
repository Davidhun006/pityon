
nev= input("Kérem adja meg a nevét ")
print(nev)
ÉV=int(2022)
udv = (f'Üdvözöllek {nev}')
print(udv,"szép napot kívánok neked", sep= " ")
eletkor = (input("Kérem adja meg a születési évét"))
eletk=ÉV-eletkor
if eletk <14: 
    print("Felnőtt vagy")
