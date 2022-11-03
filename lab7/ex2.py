tuples=(1,2,-3,3,4,-3,3,3)

def dicti(tuples):
    

   
    
    lettres ={}
    for c in tuples:
      lettres[c] =lettres.get(c, 0) + 1
    return lettres
dicti(tuples)
lettres_triees = list(dicti(tuples).items())
lettres_triees.sort()
print(lettres_triees)


