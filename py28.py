szavak = ['ajtó', 'tojás', 'Ottó', 'Tamás', 'tép', 'Tesla', 'alma', 'python']
t_betus_szavak = []

for szo in szavak:
    if szo[0] == 't' or szo[0] == 'T':
        print(szo)
        t_betus_szavak.append(szo)

print('A "t" vagy "T" betűvel kezdődő szavak:', t_betus_szavak)