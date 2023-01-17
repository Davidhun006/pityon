def arboc(magassag):
    return magassag/100
def kapnev(neve):
    neve=neve.title
    return neve.title

h = int(input("Árbóc magassga! "))
neve=input("Kapitány neve")
print(arboc(h))
print(kapnev(neve))