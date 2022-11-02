# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer.")
         print("************************************")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
     '''
     donneur=[]
     autre=[]
         

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI

     i=0
     while i<len(p)-1:
         donneur.append(p[i])
         autre.append(p[i+1])
         i=i+2
     donneur.append(p[len(p)-1])  
     
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''        


    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
     
    test=False
    resultat=[]
    j=1

    while l!=[]:
        j=1
        test=False
        while test==False and j<len(l) :
                   
               
                   if l[0][0:len(l[0])-1]==l[j][0:len(l[j])-1]:
                       del l[0]
                       del l[j-1]  
                       test=True             
                   else:
                   
                        j=j+1
        if test==False:
           
            resultat.append(l[0])
            del l[0]    

    random.shuffle(resultat)
    return resultat


def affiche_cartes(p):
    '''
    (list)-None
    Affiche les éléments de la liste p séparées par d'espaces
    '''

    # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
    # AJOUTEZ VOTRE CODE ICI
    a=" ".join(p)
    print(a)


    

def entrez_position_valide(n):
    '''
     (int)->int
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     
     Précondition: n>=1
    '''
     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
    print("j'ai ",n," cartes. Si 1 est la position de ma première carte et ",n," la position de ma dernière carte, laquelle de mes cartes voulez-vous?")
    ent=int(input( "SVP entrez un entier de 1 à "+str(n)+" :")) 
    while not (1<=ent<=n):
         ent=int(input("position invalide. SVP entrez un entier de 1 à "+str(n)))
    return ent
     

def joue():
     '''()->None
     Cette fonction joue le jeu'''
    
     p=prepare_paquet()
     melange_paquet(p)
    
     tmp=donne_cartes(p)
     donneur=tmp[0]
     humain=tmp[1]
    
     print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
     print("Votre main est:")
     affiche_cartes(humain)
     print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
     print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
    

     # COMPLETEZ CETTE FONCTION EN CONFORMITE AVEC LA DESCRIPTION CI-DESSUS
     # AJOUTEZ VOTRE CODE ICI
     while humain!=[] and donneur!=[]: 
         attend_le_joueur()
         print("votre tour.")
         print("votre main est : ")
         donneur=elimine_paires(donneur)
         humain=elimine_paires(humain)
         affiche_cartes(humain)
         #print("la main de l'ordi est")
         #affiche_cartes(donneur)
         if len(humain)>0 and len(donneur)>0:
             num=entrez_position_valide(len(donneur))
             print("vous avez demandez ma",num,"carte")
             print(" La voilà c'est un " ,donneur[num-1],)
             print("avec ",donneur[num-1]," ajoutée,votre main est :")
             humain.append(donneur[num-1])
             del donneur[num-1]
             affiche_cartes(humain)
             print("Après avoir défaussé toutes les paires et mélangé les cartes, votre main est:")

             donneur=elimine_paires(donneur)
             humain=elimine_paires(humain)
             affiche_cartes(humain)
             attend_le_joueur()
             if len(humain)==0:
                 break
             
             print("mon tour. ")
             #print("la main de l'ordi est")
             #affiche_cartes(donneur)
             carte=random.choice(humain)
             print("j'ai pris votre ",humain.index(carte)+1, " ème carte")
             donneur.append(carte)
             del humain[humain.index(carte)]
     if humain==[]:
         print("tu as terminé toutes les cartes. Félicitations! Vous, Humain, vous avez gagné.")       
     elif donneur==[]:
         print("j'ai terminé toutes les cartes. Moi Robot, j'ai gagné")


	 
# programme principale
joue()
