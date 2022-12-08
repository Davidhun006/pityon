def pn(num):
    end=int(num/2)
    s=1
    for i in range(2,end+1):
        if num %i==0:
            s+=i
    if s ==num:
        print("Tökéletes szám")
    else:
        print("nem tökéletes szám")

for i in range(2,1001):
    print(i,end=" ")
    pn(i)
ob=int(input("Kérem a vizsgálandó számot:"))
pn(ob)
print(ob)