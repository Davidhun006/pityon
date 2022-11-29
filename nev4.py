print('százszor kiírva a nevem')
név = "Gyula"
for i in range(1,101):
    print(név)
szamlalo = 0
while szamlalo <= 99:
    print(név)
    szamlalo=szamlalo+1

print(név*100)

if szamlalo!=100:
    print(név)
    szamlalo=szamlalo+1