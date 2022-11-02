def coder(s):
    r=''
    if len(s)%2==0:
        for i in range(0,len(s),2):

                r=r+s[i+1]+s[i]
    else:
        for i in range(0,len(s)-1,2):

                r=r+s[i+1]+s[i]
        r=r+s[-1]
    return r

print(coder('message secret'))
print(coder('message'))

