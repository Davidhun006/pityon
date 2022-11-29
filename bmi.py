import math



lista=[]
listas=[]
for i in range(3):
    m=int(input("milyen magas vagy"))
    lista.append(m)
    s=int(input("hány kiló vagy"))
    listas.append(s)
    szm=m**2    
    bmi=s/szm*10000
    print(bmi)

    if bmi<18.5:
        print("Sovány vagy")
    elif bmi>25:
        print("túlsúlyos vagy")
    else:
        print("normális a testsúlyod")  