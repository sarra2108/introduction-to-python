temp=float(input("svp entrer une temperature"))
if temp>=80.0:
    a=1
elif 60.0<=temp<80.0:
    a=2
elif 40.0<=temp<60.0:
    a=3
else:
    a=4
if a==1:
    print("Nataton")
elif a==2:
    print("soccer")
elif a==3:
    print("volleyball")
else:
    print("ski")
    
