class Híres_katona:
    def __init__(self,név,foglalkozás,nemzetiség):
        self.név=név
        self.foglalkozás = foglalkozás
        self.nemzetiség = nemzetiség
    def elotag(self):
        if nemzetiség == "n":
            return "Herr"
        else:
            return "Mister"
    def intialise(név):
        név=név.capitalise()
        return név
    

híres_katonak = []
for _ in range(2):
    név=input('kérem adja meg a katona nevét!')
    foglalkozás = input('kérem adja meg a katona rangját!')
    nemzetiség = input('kérem adja meg a katona nemzetiségét (o,n)!')
    híres_katona = Híres_katona(név,foglalkozás,nemzetiség) #példány
    híres_katonak.append(híres_katona)

for híres_katona in híres_katonak:
    print(f'{híres_katona.elotag()} {híres_katona.intialise()} egy híres {híres_katona.foglalkozás}')
