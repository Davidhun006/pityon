
op=1539
fp=2750
hof=float(input("Kérem adjon meg egy hőfokot "))

if hof < op:
    print("Szilárd")
elif hof < fp:
    print("Folyékony")
else:
    print("Gáz")