mettöl=int(input('Hány órás visszaszámlálást tervezünk? '))
orak=0
vissza=mettöl
while mettöl!=0:
    függeszt=input('Fel kell függeszteni a visszaszámlálást (i/n)?')
    if függeszt=='n':
        vissza-=1
        orak+=1
    elif függeszt=='i':
        print('A rakéta a visszaszámlálást követően ennyi órával indult: ',orak+vissza)
        exit()
    else:
        print('kys')
print('A rakéta a visszaszámlálást követően ennyi órával indult: ',orak)