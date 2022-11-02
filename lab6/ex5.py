def espaces(s):
    r=''
    for i in range(len(s)):
        r=r+s[i]+" "
    
    r=r[0:len(r)-1]
    return r
print(espaces("important"))
