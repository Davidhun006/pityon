#1
while True:
    try:
        szam = int(input("Adj meg egy páros számot: "))
        if szam % 2 == 0:
            break
        else:
            print("A megadott szám páratlan. Adj meg egy páros számot!")
    except ValueError:
        print("Adj meg egy egész számot!")

for i in range(szam // 2):
    print("O " * (i + 1))
for i in range(szam // 2, 0, -1):
    print("O " * (i))


#2
for i in range(5):
    for j in range(5):
        if i == j:
            print("O", end=" ")
        else:
            print(".", end=" ")
    print()


#3
for i in range(7):
    for j in range(7):
        if i == j or i + j == 6:
            print("O", end=" ")
        else:
            print(".", end=" ")
    print()
