def moyenne():
    a=input('entrez une liste svp')
    l=list(eval(a))
    m=0
    for i in range(len(l)):
        m=m+l[i]

    moy=m/len(l)
    return moy
print(moyenne())
    
