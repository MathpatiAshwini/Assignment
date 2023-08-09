n=int(input("enter the number:"))
m=int(input("enter the number:"))
sum=0
i=1
v=1
while i<=n:
    t=v(m**i)/i
    v=v*(-1)
    sum+=t
    i+=1
print(sum)