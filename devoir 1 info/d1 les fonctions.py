#QUESTION1:
def tempsVoyage(d,v):#la fonction prend deux variables reels d(distance) et v(vitesse)
    '''(float,float)--float'''
    temps=d/v*60
    return temps #la fonction calcule et retourne le temps qui est un reel
a=tempsVoyage(400,100)#appel de la fonction
print(a)

#QUESTION2:
def noteFinale(note_lab,moy_dev,note_quiz,note_expart,note_final):#la fonction prend 5variables de types reels 
    '''(float,float,float,float,float)--float'''
    res=note_lab*(10/100)+moy_dev*(25/100)+note_quiz*(5/100)+note_expart*20/100+note_final*40/100
    return res #la fonction calcule et retourne la note finale de type reel 
b=noteFinale(100,100,100,100,100)
note=noteFinale(50,90.5,60,80,70)#appel de la fonction
print(b)

#QUESTION3:
def bibformat(auteur,titre,ville,maisonedition,annee):#la fonction prend 4 variables de type chaines de caractères et un variable de type entier
    '''(str,str,str,str,int)--str'''
    bibformat =(auteur +' ('+str(annee) + '). ' + titre +'. ' + ville + ': ' + maisonedition)
    return bibformat#la fonction retourne une chaine de caractère sous une format specifique
f=bibformat("Antoine de Saint Exupery","le petit prince","paris","jeunesse",1943)#appel de la fonction
print(f)
            
#QUESTION4:
def bibformatPrint():
    ''' ()->None'''
    a=input("donne moi un titre d'un livre ")
    n=input("le nom de l'auteur ")
    s=int(input("l'année de publication "))     #la fonction prend du clavier 5 variables de type chaine
    z=input("la maison d'edition ")
    q=input("la ville de la maison d'edition ")
    t=bibformat(n,a,q,z,s) #La fonction affiche l’information sur le livre dans le format spécifie dans la question 3.
    print(t)#la fonction ne retourne rien
bib=bibformatPrint()#appel de la fonction

    


