s=input("entrez votre chaine")
def compte(s,a):
    c=0
    i=0
    while i<len(s) :
        if s[i:len(a)+i]==a:
                c=c+1

        i=i+1
        
        
                       
    return c 
print(compte(s,'a'))
print(compte(s,'de la'))
print(s.count('a'))
print(s.count('de la'))
