a=int(input("enter the gender"))
u=input("enter teh gender:-")
d =int(input("enter the days"))
if a>=18 and a<30 and u=="M":
    print(d*700)
elif a>=18 and a<30 and u=="F":
    print(d*750)
elif a>=30 and a<=40 and u=="M":
    print(d*800)
elif a>=30 and a<=40 and u=="M":
    print(d*850)
else:
    print("no wage")
    