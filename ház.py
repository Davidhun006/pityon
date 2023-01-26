def fugg(szám):
    if szám % 2 == 0:
        return "A ház az utca jobb oldalán áll."
    else:
        return "A ház az utca bal oldalán áll."

while True:
    utcanév = input("Adja meg az utca nevét! ")
    if utcanév == '':
        break
    házszám = int(input("Adja meg a házszámát! "))
    print(fugg(házszám))
