class Híres_auto:
    def __init__(self, márka_név, henger_térfogat, nemzetiseg): # konstruktor
        self.név = márka_név
        self.henger_térfogat = henger_térfogat
        self.nemzetiseg = nemzetiseg

    def elotag(self):
        if self.nemzetiseg == 'n':
            return "Német"
        else:
            return "Japán"

hires_autok = []
for _ in range(3):
    márka_név = input("Add meg egy autó márkanevét! ")
    henger_térfogat = input("Add meg a henger térfogatát! ")
    nemzetiseg = input("Add meg a gyártó országát (j/n)! ")
    hires_auto = Híres_auto(márka_név, henger_térfogat, nemzetiseg)
    hires_autok.append(hires_auto)

for autok in Híres_auto:
    print(autok.márka_név,'egy',autok.nemzetiseg(),'autó',autok.henger_térfogat,'m3 henger térfogattal.')
