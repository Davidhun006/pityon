
sentence = input("Kérlek add meg a mondatot: ")

while True:

    mondat = input("Kérlek add meg a mondatot (kilépéshez nyomd meg az ENTER-t): ")


    if not mondat:
        break


    
    központozás = mondat[-1]


    if központozás == ".":
        print("A mondat kijelentő.")
    elif központozás == "?":
        print("A mondat kérdő.")
    elif központozás == "!":
        print("A mondat felkiáltó / felszólító / óhatatlan.")
    else:
        print("A mondat vége nem ismeretlen karakter.")