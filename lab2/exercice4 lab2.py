from math import sqrt
#question4:
def surface(cote1,cote2,cote3):
    p=cote1+cote2+cote3
    s=sqrt(p*(p-2*cote1)*(p-2*cote2)*(p-2*cote3))/4
    return s
a=surface(10,12,13)
b=surface(12,14,15)
q=surface(100,120,140)
print(a)
print(b)
print(q)
