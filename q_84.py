a=int(input("enter teh length"))
b=int(input("enter teh length"))
c=int(input("enter teh length"))
if a==b and b==c and a==c:
    print("equilateral triangle")
elif a==b or a==c or b==c:
    print("isosceles triangle")
elif (a*a+b*b)==c*c or (b*b+c*c)==a*a or (c*c+a*a)==b*b:
    print("right-angled triangle ")
