unit=int(input("enter the units"))
if unit==100:
    print("no")
elif unit >100 and unit<=200:
    print("5 per units")
elif unit >200:
    print(unit(10/100/unit))
else:
    print("nothing")
