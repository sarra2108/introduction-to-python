n=int(input("entrez un nombre non negatif"))
while n<0:
    n=int(input("entrez de nouveau un nombre non negatif"))
def calculeFact(n):
    if n==0:
        f=1
    else:
        f=1
        for i in range(1,n+1):
            f=f*i
    return f
    
a=calculeFact(n)
print("le factoriel de",n,"est",a)

    
