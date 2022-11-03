def somme_de_trois(x):
    '''(tuple)->bool
     Retourne True si la somme de 3 elements
     consecutive est zero
     Precondition: le tuple a au moins 3
     elements
     >>> t = (1,2,-3,4,-1,3)
     >>> somme_de_trois(t)
     True'''
    test=False
    i=0
    while i<len(x)-2:
         if x[i]+x[i+1]+x[i+2]==0:
             test=True
             break
         else:
             i=i+1
    return test
t = (1,2,-3,4,-1,3)
print(somme_de_trois(t))
             
