class HíresEgyetem:
    def __init__(self, egyetemnév, város,nemzetiseg):
        self.név = egyetemnév
        self.város = város
        self.nemzetiseg=nemzetiseg
    def elotag(self):
        if self.nemzetiseg=="a":
            return"University"
        else:
            return"Universität"
egyetem1=[]
for _ in range(3):
    nev=input("Add meg egy egyetem nevét!")
    város=input("Add meg a az egyetem városát! ")
    nemzetiseg=input("Add meg a nemzetiségét (a/n)!")
    egyetem=HíresEgyetem(nev,város,nemzetiseg)
    egyetem1.append(egyetem)
for egyetemek in egyetem1:
    print(egyetemek.név,egyetemek.város,egyetemek.nemzetiseg,egyetemek.elotag())


 