def kis_nagy(letszam):
    if letszam>=1000:
        return True
    else:
        return False
   
nev=None
letszam=None
while nev!='':
    nev=input('Add meg az iskola nevét! ')
    if nev=='':
        break
    letszam=int(input('Add meg a pontszámát!'))
    if kis_nagy(letszam)==True:
        print(nev,' nagy létszámú iskola.')
    else:
        print(nev,' kis létszámú iskola.')