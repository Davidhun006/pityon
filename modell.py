# megfelel=False
# nev=input("Add meg a jelentkező nevét!")
# while nev!='':
#     magasság=int(input("Hány centiméter magas?"))
#     if magasság>=170:
#         megfelel=True
#     if megfelel==True:
#         print(nev,"Megfelelő magasságú")
#         magasság=int(input("Hány centiméter magas?"))
#     else:
#         print(nev,"A magasság nem megfelelő modellnek")
def megfelel(magassag):
    if int(magassag)<170:
        return False
    else:
        return True
nev = None
while nev !="":
    nev=input('Add meg a jelentkező nevét!')
    if nev!="":
        m=input("Hány centiméter magas?")
        if megfelel(m):
            print(nev,"Megfelelő magasságú")
        else:
            print(nev,"A magasság nem megfelelő modellnek")
