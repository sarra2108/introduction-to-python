#Question1:
def compte100(a):
    '''list-->entier'''
    #la fonction i prend une liste de nombres et retourne le nombre d’éléments superieurs a 100 trouvés dans la liste
    comp=0
    for i in range(len(a)):
        if a[i]>100:
            comp=comp+1
    return comp

print(compte100([1,102,-3.5,104]))
print(compte100([1,99,-3.5,-7]))
print(compte100([]))
#QUESTION2:
def sommeListeDiv2(a):
    '''list-->float'''
    #la fonction prend comme entré list des entiers et retourne la somme des éléments de la liste qui se divisent par 2
    s=0
    for i in range(len(a)):
        if a[i]%2==0:
            s=s+a[i]
    return s 
print(sommeListeDiv2([1,4,3,8,5]))

print(sommeListeDiv2([]))

print(sommeListeDiv2([4,-10,7]))
#QUESTION3:
def triples(ch):
    '''chaine-->bool'''
    # la fonction prend une chaine de caracteres et qui retourne True s’il y a au moins une séquence de 3 caracteres consécutifs égaux, et False dans le cas contraire.
    i=0
    while i<len(ch)-2:
        if ch[i]==ch[i+1]==ch[i+2]:
            return True      
            
        i=i+1
    return False
#QUESTION4:
def momo(ch):
    '''string-->string'''
    # la fonction prend une chaine de caracteres et retourne une nouvelle chaine de caracteres qui contient les caracteres de la chaine donnée une fois chacun (sans repetisions), en meme ordre, et avec leur nombre de repetitions
    res=""
    while len(ch)>1:
            b=ch[0]
            i=0
            j=0
            comp=1  
            while i<len(ch)-1 and ch[i]==ch[i+1]:
                    comp=comp+1
                    
                    i=i+1
            res=res+b+str(comp)
            while ch!="" and ch[j]==b:
                    ch=ch[0:j]+ch[j+1::]
    if len(ch)==1:
            res=res+ch+"1"
            
    return res

print(triples("abc"))
print(triples("abbbcdeeggggg"))
print(triples("a23xxxxx"))
print(triples("abaacd"))


print(momo("a"))
print(momo("aabbbccccx"))

print(momo("aaa1111"))
print(momo("aaabcaax"))

            
            
