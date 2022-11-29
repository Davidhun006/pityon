#1

tantargyak = ['matek', 'töri', 'bio', 'kémia', 'info']

for tantargy in tantargyak:
	    print(tantargy)

#2

# 0 -> 9
for i in range(10):
	    print(i)

# 5 -> 8
for i in range(5,9):
	    print(i)

# 3 -> 20-ig 6-osával
for i in range(3,21,6):
	    print(i)
  

#3

honapok = ['január', 'február','március', 'április', 'május', 'június'] 
  
index = 0
for honap in honapok:
    print(index, honap)
    index = index + 1

#4


honapok = ['január', 'február','március', 'április', 'május', 'június']
  
for index in range(len(honapok)):
    print(index, honapok[index])
  

#5


honapok = ['január', 'február','március', 'április', 'május', 'június']
  
for index, honap in enumerate(honapok):
      print(index, honap)


#+1

honapok = ['január', 'február','március', 'április', 'május', 'június']

for honap in honapok:
     # az eredeti listaelem NEM módosul!
	 honap = honap.upper()	

    

#+2


for index in range(len(honapok)):
 # az eredeti listaelem módosul!
     honapok[index] = honapok[index].upper()




#1
három=[]
for i in range(1,40):
    if i %3==0:
        három.append(i)
print(három)


#2.1
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
for i in szavak:
    if i.startswith("T") or i.startswith("t"):
        print(i)


#2.2
    


#3

szamok = [120, 9, 5, 24, 6, 17, -45, 92, 15, 48, 57]
