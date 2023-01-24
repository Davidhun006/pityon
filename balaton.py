from balatonalap import balaton

telepulesek = []
for _ in range(1):
    település = input("Add meg egy település nevét! ")
    fekvés = input("Add meg a fekvését (é/d)! ")
    szám = int(input("Add meg a lakosság számát! "))
    telepulesek.append(balaton(település, fekvés, szám))
for telepules in telepulesek:
    print(f"{telepules.település} egy {telepules.fugg()} parti {telepules.elotag()}, {szám} fővel.")
