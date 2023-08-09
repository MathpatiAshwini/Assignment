sp=int(input("enter the number:--"))
cp=int(input("enter the number:--"))
if sp>cp:
    print(sp-cp)
elif sp==cp:
    print("no profit - no loss")
else:
    print(cp-sp)