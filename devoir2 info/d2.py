#QUESTION 1:
def patinage(ep,temp):#la fonction prend 2 variables de type float l'epaisseur et la temperature
    ''' (float, float)->bool '''
    return ep>=30 and temp<=-10 #la fonction retourne true si epaisseur est superieur a 30 ET la temperature inferieur à 10 et False sinon 
        
pat=patinage(33,-5)
b=patinage(30,-10)
c=patinage(25.4,-15)
print(b)
print(c)
print(pat)
#QUESTION 2:
def alphaNote(nb):#la fonction prend un variable de type entier
    ''' (integer)-> string '''
    if 0<=nb<=39:#on va retourner une note alphabetique pour une note numerique donnée
        return("F")
    elif 40<=nb<=49:
        return("E")
    elif 50<=nb<=54:
        return("D")
    elif 55<=nb<=59:
        return("D+")
    elif 60<=nb<=64:
        return("C")
    elif 65<=nb<=69:
        return("C+")
    elif 70<=nb<=74:
        return("B")
    elif 75<=nb<=79:
        return("B+")
    elif 80<=nb<=84:
        return("A-")
    elif 85<=nb<=89:
        return("A")
    elif 90<=nb<=100:
        return("A+")
note=alphaNote(99)
print(alphaNote(89))
print(alphaNote(56))
print(note)

#QUESTION 3:
def alphaNoteVerif():
    '''() ->None'''
    notef=float(input("svp entrez la note finale"))#la foction va lire du clavier une note final
    while not 0<=notef<=100:#la fonction va verifier si la note est comprise entre 0 et 100 .Le cas échéant ,on demande à l'utilisateur de saisir une valeur valide meme plusieur fois jusqu'a a une valeur attendue
        notef=float(input("svp entrez la note finale"))
    a=alphaNote(notef)#appel de la fonction alphaNote de la question 2 
    print("la note alphabitique",a)#la fonction affiche la note alphabetique
    if 0<=notef<=49:#la fonction affiche echoue si la note<=49 et reussi si note>49
        
        print("echoue")
    else:
        print("reussi")
n=alphaNoteVerif()

#QUESTION 4:
def boucles(n):#la fonction prend une variable de type entier
    '''(entier) ->None'''
    a=1
    while a<=n:
        print(a," ",end='')#la fonction affiche la 2e valeur de 1 à n
        a=a+2
    print(" ")
    b=n
    while b>=1:
        print(b," ",end='')#la fonction affiche la 2e valeur de n à 1
        b=b-2
bouc=boucles(10)#la fonction ne retourne rien
print(" ")
boucles(13)
#QUESTION 5:
print(" ")
def facteursDeN(n):#la fonction prend un entier n comme parametre
    '''(entier) ->bool'''
    somme=0
    print("les facteurs de",n,"sont ",end="")
    for i in range( 2,n):
        
        if n%i==0:
            print(i," ",end='')#imprime tous les facteurs de n
            somme=somme+i
    print(" ")
    print("la somme des facteurs est",somme)#imprime la somme des facteurs
    return somme<n#la fonction retourne True si la somme des facteur est inferieur a n et False le cas contraire
n=facteursDeN(12)
print(n)
print(facteursDeN(9))
#QUESTION6 
def carreParfait(x):#la fonction prend x comme variable de type entier
    '''(enetier) ->bool'''
    for i  in range(1,x//2+1):
        test=i*i#chercher un entier tel que n^2=x
        
        if test==x:#si on trouve un entier verifiant l'egalité n^2=x donc on sort du boucle
            break

    
    if test!=x:#la fonction affiche si x est un carre parfait ou non ainsi que la racine si il y'a un 
        print(x,"n'est pas un carre parfait")#
    else:
        print(x,"est un carre parfait, le carre parfait de",x,"est",i)
    return i*i==x#la fonction retourne True si x est un carre parfait et false le cas contraire
    
a=carreParfait(16)
print(a)
print(carreParfait(15))

            
        

    
    
