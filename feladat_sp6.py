szam=int(input('Adl meg egy számot'))
if szam %2==0 and szam>0:
    print('a szám páros és pozitív')
elif szam %2==1 and szam<0:
    print('a szám páratlan és negatív')
