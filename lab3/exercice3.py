num=int(input("svp entrer votre nombre"))
if num%2==0 and num%3==0:
    print("divisible par 2 et 3 ")
elif num%2==0 or num%3==0:
    print("divisible par 2 ou 3 ")
else:
    print("pas divisible ni par 2 ni par 3 ")
