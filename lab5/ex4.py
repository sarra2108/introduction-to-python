from math import sqrt
def ecart_type(l):
    m=0
    for i in range(len(l)):
        m=m+l[i]

    moy=m/len(l)
    a=0
    for i in range(len(l)):
        a=a+(l[i]-moy)**2
        s=sqrt(a/((len(l)-1)))
    print(s)
a=input('entrez une liste svp')
l=list(eval(a))
ecart_type(l)
               
