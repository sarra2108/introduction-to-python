a=input("entrz une liste")
l=list(eval(a))
def calcul(l):
    m=0
    for i in range(len(l)):
        m=m+l[i]

    moy=m/len(l)
    mini=l[0]
    maxi=l[0]
    for i in range(len(l)):
        if l[i]<mini:
            mini=l[i]
        elif l[i]>maxi:
            maxi=l[i]
    b=[moy,mini,maxi]
    return b
print(calcul(l))
        
    
