szam1=int(input("Add meg az egyik iskolai számot "))
szam2=int(input("Add meg a másik iskolai számot "))
if szam1>szam2:
    print("A létszám érték az első iskolában több",szam1)
elif szam1<szam2:
    print("A létszám érték az második iskolában több",szam2)
else:
    print("A két létszám egyenlő")