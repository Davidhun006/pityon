
  
nev=None
alma=None
while nev!="":
    nev=input("Add meg a neved")
    alma=int(input("3 számjegyű kód "))
    if alma==599:
        print(nev,"hazai gyümölcsöt vásárolt")
    elif alma!=599:
        print(nev,"külföldi gyümölcsöt vásárolt")