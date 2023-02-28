import random

# véletlenszámok generálása és tárolása a listában
numbers = [random.randint(1, 3) for _ in range(10)]


print("Az eredeti lista:", numbers)


while True:

    num = input("Kérem adjon meg egy számot 1 és 3 között (kilépéshez nyomj egy ENTER-t): ")


    if not num:
        break

    
    try:
        num = int(num)
    except ValueError:
        print("A megadott érték nem egy szám!")
        continue

    
    if num < 1 or num > 3:
        print("A megadott érték nem esik a 1 és 3 intervallumba!")
        continue

   
    while num in numbers:
        numbers.remove(num)

  
    print("A módosított lista:", numbers)