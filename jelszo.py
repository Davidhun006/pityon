
bejutott= False

while not bejutott:
    felhasznalo=input("Kéram adja meg a felhasználónevét")
    jelszo=input("Kéram adja meg a jelszavát")
    if felhasznalo == "bori99" and jelszo == "kismehe<3":
        print("a belépés megengedve")
        bejutott= True
    else:
        print("belépés megtagadva")