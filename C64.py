név=input("mi a gép neve?")
mukodik= True if input("Mukodik (i/n)?") == "i" else False
ar=int(input("MEnnyi az ara??" ))

if (név=="ZX Spectrum" or név == "C64") and mukodik and ar <=25000:
    print("Bisznisz csincsing!!!")
else:
    print('MENJ MÁR A FENEBE A ROSZ MEGFIZETHETETLEN GAGYI GÉPEDDEL')