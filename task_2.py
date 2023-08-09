a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))

if a+b>c or b+c>a or c+a>b:\
    print("validate tringle")
elif a==b or b==c or c==a:
    print("equilateral ")
elif a!=b or b!=c or c!=a:
    print("scalene")
elif (a==b and a!=c) or (b==c and c!=a) or (c==a and c!=b):
    print("isosceles ")
if a*a+b*b==c or b*b+c*c==a*a or c*c+a*a==b*b:
    print("right-angled triangle")

