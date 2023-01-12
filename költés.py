kedd=int(input("hány forintot költöttél kedden "))
szerda=int(input("hány forintot költöttél szerdán "))

if kedd>szerda:
    print(f"kedden költöttél többet,{kedd}")
elif szerda>kedd:
    print(f"szerdán költöttél többet,{szerda}")
else:
    print(f"kedden és szerdán ugyanannyit költöttél{szerda,kedd}")
