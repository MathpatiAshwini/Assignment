a=int(input("enter the number:-"))
b=int(input("enter the number:-"))
c=int(input("enter the number:-"))
d=int(input("enter the number"))
if a>b:
    max1=a
    sec1=b
else:
    max1=b
    sec1=a
if c>d:
    max2=c
    sec2=d
else:
    max2=d
    sec2=c
if max1>max2:
    if max2>sec1:
        print(max2)
    else:
        print(sec1)
else:
    if max1>sec2:
        print(max1)
    else:
        print(sec2)