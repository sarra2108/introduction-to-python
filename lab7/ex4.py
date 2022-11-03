listee=[1, 0, 3, 0, 0, 5, 7]
def  move_zeros_v1(listee):
    t=[]
    c=0
    for i in range(len(listee)):
        if listee[i]!=0:
            t.append(listee[i])
        else:
            c=c+1
    for i in range(c):
        t.append(0)
    return t
print(listee,move_zeros_v1([1, 0, 3, 0, 0, 5, 7]))

def move_zeros_v2(listee):
    t=[]
    c=0
    for i in range(len(listee)):
        if listee[i]!=0:
            t.append(listee[i])
        else:
            c=c+1
    for i in range(c):
        t.append(0)
    for i in range(len(listee)):
        listee[i]=(t[i])
    
move_zeros_v2(listee)
print(listee,move_zeros_v2([1, 0, 3, 0, 0, 5, 7]))

def move_zeros_v3(listee):
    i=0
    n=len(listee)
    while i<n:
        if listee[i]==0:
            listee.append(listee[i])
            del listee[i]
            n=n-1
        else:
            i=i+1
       
move_zeros_v3(listee)   
print(listee,move_zeros_v3([1, 0, 3, 0, 0, 5, 7]))
        
