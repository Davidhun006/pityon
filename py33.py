paletta = ['kék', 'piros', 'fehér', 'fekete', 'zöld',
           'sárga', 'barna', 'piros', 'fehér', 'szürke']
szin = input('Adj meg egy színt!\t')
hány=0
for szinek in paletta:
    if szinek==szin:
        hány+=1


if szin in paletta:
    print('A megadott szín szerepel a listában, és',hány, '-szor van benne')


else:
    print('A megadott szín nem szerepel a listában.')


print('A lista színei:')

for szin in paletta:
    print(szin, end=', ')
