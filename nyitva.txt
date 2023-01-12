ora=int(input("Hány óra van most?"))
if ora >=8 and ora <16:
    print(f"A bolt nyitva van!")
    meg_ennyit_van_nyitva= 16-ora
    print(f"Ennyi órád van még ma boltba menni:{meg_ennyit_van_nyitva}")
else:
    print(f"A bolt zárva van")