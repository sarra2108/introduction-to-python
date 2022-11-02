a=float(input("entrer votre a "))
b=float(input("entrer votre b "))
c=float(input("entrer votre c "))
d=b*b-4*a*c
if d<0:
    print("pas de solutions")
elif d==0:
    print("1 racine")
else:
    print("2 racines")
