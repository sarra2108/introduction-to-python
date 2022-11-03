ch=input("entrez une chaine")
def fonc(ch):
    lettres ={}
    for c in ch:
         lettres[c] =lettres.get(c, 0) + 1
    return lettres

lettres_triees = list(fonc(ch).items())
lettres_triees.sort()
print(lettres_triees)


