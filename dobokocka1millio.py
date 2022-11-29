import random

szamlalo=0
hat=0
dobás=random.randint(1,6)
while szamlalo<=1000000:
    dobás=random.randint(1,6)
    if dobás==6:
        hat+=1
    szamlalo+=1
print(hat)