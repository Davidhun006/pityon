nev='bori99'
jelszo='Szivecske<3'
belep1=False
belep2=False
while True:
    ker1=input('Adja meg a felhasználónevét! ')
    ker2=input('Adja meg a jelszavát! ')
    if ker1==nev:
        belep1=True
        if ker2==jelszo:
            belep2=True
            break
        else:
            print('Belépés megtagadva.')
    else:
        print('Belépés megtagadva.')
print('Belépés engedélyezve')
