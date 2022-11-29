import math

sugar = float(input('Írd be a kúp sugarát '))
magassag = float(input('Írd be a kúp magasságát '))

l = math.sqrt(sugar * sugar + magassag * magassag)

Felszín = math.pi * sugar * (sugar + l)

Térfogat = (1.0/3) * math.pi * sugar * sugar * magassag

Oldalsófelület= math.pi * sugar  * l

print("\n A kúp oldalának (ferde) hossza = %.2f" %l)
print(" A kúp felszíne = %.2f " %Felszín)
print(" A kúp térfogata = %.2f" %Térfogat)
print(" A kúp oldalsó felülete = %.2f " %Oldalsófelület)