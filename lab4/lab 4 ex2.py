n=int(input("entrez une valeur N"))
def calcul(n):
    for i in range(1,n+1):
        print(i)
    a=1
    while n>=a:
        print(a)
        a=a+1
calcul(n)
