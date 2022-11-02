nS = ''' En 1815, M. Charles-François-Bienvenu Myriel était évêque de 
Digne. C’était un vieillard d’environ soixante-quinze ans ; il occupait le
siège de Digne depuis 1806. … '''
a=nS.replace(" ",'.')
b=nS.replace(" ",',')
c=nS.replace(" ",';')
d=nS.replace(" ",'\n')
print(a)
print(b)
print(c)
print(d)
nS=nS.strip()
print(nS)
zle=nS.lower()
print(zle)
a=nS.count("de")
print(a)
nS=nS.replace("était","est")
print(nS)
