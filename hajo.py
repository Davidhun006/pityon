hajo1=int(input("Hajo1 sebessége"))
hajo2=int(input("Hajo2 sebessége"))
def valto(sebesseg):
    return sebesseg/1.852
if hajo1>hajo2:
    print("Hajo1 gyorsabb mint Hajo2")
elif hajo1<hajo2:
    print("Hajo2 gyorsabb mint Hajo1")
else:
    print("Egyenlő sebességűek")