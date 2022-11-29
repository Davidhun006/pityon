# Naponta legalább 2,5 liter folyadékot kell fogyasztanunk,
# és ivásból nem vagyunk valami jók.  Írjunk programot,
# amelyik bekéri, hogy egy-egy alkalommal hány decit ittunk!
# Teszi mindezt addig, amíg 0 értéket nem adunk meg.
# Minden bekéréskor kiírja, hogy addig hány litert ittunk összesen,
# és ha elérjük a 2,5 litert, akkor erről is megemlékezik.
# 3,5 liter fölött kilép, szépen elbúcsúzva tőlünk.


literek = 0
maximum = 3.5
jo = 2.5
napi_teljesítve = False
elmondta = False

while literek < 3.5:
    deci = int(input("Hány deci vízet ivott? "))
    literek = deci/100 + literek
    print(literek," l vizet ivott.")
    if literek >= jo:
        napi_teljesítve = True
        if not elmondta:
            print("Megitta a napi célt!:) ")
            elmondta = True
        if literek >= maximum:
            print("Viszlát!")
            break