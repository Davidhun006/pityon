import random
feldobasok = []
for _ in range(10):
    feldobas = random.choice(['f', 'í'])
    feldobasok.append(feldobas)

print('A feldobások: ', ', '.join(feldobasok))

fej_utan_fej = 0
for index, feldobas in enumerate(feldobasok):
    if index > 0 and \
        feldobas == 'f' and feldobasok[index-1] == 'f':
        fej_utan_fej += 1

print('Ennyiszer volt fej után fej: ', fej_utan_fej)