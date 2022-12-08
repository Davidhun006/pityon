
def tengerszintek():
    if tengerszint<200:
        print("alföld")
    elif tengerszint<500:
        print("dombság")
    elif tengerszint<1500:
        print("középhegység")
    else:
        print("magashegység")


hely=None
tengerszint=None     
while hely or tengerszint!="":
    hely=input("földrajzi hely neve ")
    tengerszint=int(input("tengerszint feletti magasság "))
    if tengerszint=="":
        break
    tengerszintek()
    