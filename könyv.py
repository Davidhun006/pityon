könyv1=int(input("Adj meg az egyik könyv oldalszámát! "))
könyv2=int(input('Adjon meg egy másik könyv oldalszámát! '))

if könyv1 > könyv2:
    print("A könyv oldalszáma az egyik könyvben több",könyv1 )
    
elif könyv2>könyv1:
    print('A könyv oldalszáma a másik könyvben több,',könyv2)

else:
    print('A két könyv egyenlő oldalszámú.')
