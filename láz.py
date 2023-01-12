def laz(hom):
    if hom>37.5:
        return 'lázas'
    else:
        return 'nem lázas'
    
nev=None
while nev!="":
    nev= input('Kérem adja meg a nevét ')
    if nev:
        hom=float(input('Kérem adja meg hömérsékletét '))
        if laz(hom):
            print(f"{nev} lázas vagy")
        else:
            print(f"{nev} nem vagy lázas")