from random import randint
def deviner():
    n=randint(1,10)
    
    a=int(input("devinez le numero"))
    comp=1
    while a!=n:
        if a<n:
            print("essayer avec un nombre plus grand que",a)
            a=int(input("essayer de nouveau"))
            comp=comp+1
        else:
            print("essayer avec un nombre plus petit que", a)
            a=int(input("essayer de nouveau"))
            comp=comp+1
    
    
    return comp
    
a=deviner()
print("felicitation le nombre d'essai est",a)

