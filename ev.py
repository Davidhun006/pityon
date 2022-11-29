ev= [2984,2348,2069,2204,2418,2037,2092,2495,2487,2827,2305,2650]
ev1=False
if len(ev)==12:
    ev1=True
    print(f'ez egy év adatsora')
else:
    print(f'ez nem egy év adatsora')

legnagyobb= ev[0]
for num in ev:
    if num>legnagyobb:
        legnagyobb=num
print(legnagyobb)

legkisebb= ev[0]
for num in ev:
    if num<legkisebb:
        legkisebb=num
print(legkisebb)
osszes=0
for num in ev:
    osszes=osszes+num
print(osszes)

alatt=0
for num in ev:
    if num<2400:
        alatt+=1
print(alatt)

hosz=len(ev)
ker=legnagyobb
i=0
while ev[i]!=ker:
    i+=1
print(f'legnagyobb helye: {i+1}')

hosz=len(ev)
ker=legkisebb
i=0
while ev[i]!=ker:
    i+=1
print(f'legkissebb helye: {i+1}')