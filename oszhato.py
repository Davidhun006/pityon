szam=int(input('Adjon meg egy számot! '))
if szam % 3 == 0 and szam % 4 == 0:
    print('A szám néggyel és hárommal is osztható.')
elif szam % 3 == 0 and szam % 4 == 1:
    print('A szám csak hárommal osztható.')
elif szam % 3 == 1 and szam % 4 == 0:
    print('A szám csak néggyel osztható.')
else:
    print('A szám egyikkel sem osztható.')