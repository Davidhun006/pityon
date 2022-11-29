össz=0
while össz <= 35 and (ivás:=int(input("Hány decit ittál?"))):
    print(f'Már {(össz:=össz+ivás)/10:3.1f} litert ittál')
    if össz>=25:
        print("Már sikerül elerned 2,5 litert")
print("Béka nőlk a hasadba\"!")    