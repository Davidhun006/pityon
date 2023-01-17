class Hajo:
    def __init__(self,neve,kapneve,arboc,sebesseg,orszag):
        self.kapneve=kapneve
        self.arboc=arboc
        self.sebesseg=sebesseg
        self.orszag=orszag
        self.neve=neve
    def valto(sebesseg):
        return sebesseg*1.852
    def arboc_m(arboc):
        return arboc/100
    def kapnev(neve):
        return neve.title()
    def nemzet(orszag):
        if orszag=="o":
            return "orosz"
        if orszag=="a":
            return "amerikai"
hajo=[]
for _ in range(3):
    neve=int(input("adja meg a hajo nevet"))
    h = int(input("Árbóc magassga! "))
    kapneve=input("Kapitány neve")
    seb=int(input("Adja meg a sebesseget csomoban"))
    orszag=input("Adja meg a hajo orszagat")
    sello=Hajo(neve,kapneve,h,seb,orszag)
