from math import sqrt
#question1:
x=int(input("donne moi un entier"))
y=int(input("donne moi un autre entier"))
print(x//y,';',x%y)
#question2:
def cel_fah(c):
    f=9/5*c+32
    return f
a=100
b=50
c=0
res=cel_fah(a)
res=cel_fah(b)
res=cel_fah(c)
print(a,"celsius est",res)
print(b,"celsius est",res)
print(c,"celsius est",res)

#question3:
def notef(devoirMoyenne,partiel,examen):
    note=devoirMoyenne*25/100+partiel*25/100+examen*50/100
    return note
note=notef(100,100,100)
note2=notef(200,300,100)
print(note)
print(note2)

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
