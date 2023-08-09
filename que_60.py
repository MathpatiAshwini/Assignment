n=int(input("enter the number:"))
x=int(input("enter the number:"))
sum=0
i=1
v=1
while i<=n:
    t=v(x**i)
    v=v*(-1)
    sum+=t
    i+=2
print(sum)