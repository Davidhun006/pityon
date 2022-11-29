import random
import math
magasság=random.randint(2,10)
sugár=random.randint(2,10)

pi=22/7
magasság = float(input('A henger magassága: '))
sugár = float(input('A henger sugara: '))
térfogata = pi * sugár * sugár * magasság
felszíne = ((2*pi*sugár) * magasság) + ((pi*sugár**2)*2)
print("A térfogata: ", térfogata)
print("A felszíne: ", felszíne)