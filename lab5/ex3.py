from math import*

def calcul():
    v=int(input("entrez la vitesse svp"))
    a=[]
    for i in range(9):
        d=(2*v**2*cos(pi/180*i*10)*sin(pi/180*i*10))/9.8
        a.append(d)
    return a


print(calcul())
