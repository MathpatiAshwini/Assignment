n=int(input("enter the number:--"))
p=1
while n>0:
    r=n%10
    p*=r
    n//=10
print(p)