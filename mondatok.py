import random
def nevelo(szo):
    maganhangzo=("a á e é i í o ó ö ő u ú ü ű")
    if szo[0].lower() in maganhangzo:
        return "az"
    else:
        return "a"
def jelzo():
    return random.choice(['piros',"nagy","könnyed"])

print("Adj meg 3 főnevet")
for szam in range(1,4):
    fonev=input(str(szam)+".főnév: ")
    print(nevelo(fonev).capitalize()," ",fonev," ",jelzo(),".",sep=" ")