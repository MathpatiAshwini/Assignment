a=int(input("entre the number:-"))
b=int(input("entre the number:-"))
c=int(input("entre the number:-"))
if a>b and b>c:
    print(c)
elif b>a and c>a:
    print(a)
else:
    print(b)
