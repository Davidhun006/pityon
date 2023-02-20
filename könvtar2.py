def könyvn(könyvek):
    if könyvek>800:
        return True
    else:
        return False
    
könyvtárnev=None


while könyvtárnev!='':
    könyvtárnev=input("Add meg az könyvtár nevét")
    if könyvtárnev=='':
        break
    könyvek=int(input('Add meg a gyűjtött kötetek mennyiségét (ezer)!'))
    if könyvn(könyvek)==True:
        print(könyvtárnev,"ügyes gyűjtő címet kap.")
    else:
        print(könyvtárnev,"kevésbé szorgalmas gyűjtő címet kap.")