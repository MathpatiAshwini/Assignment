n=int(input("enter the number:"))
m=int(input("enter the number:"))
s=0
s2=0
while n<=m:
    if n%2==0:
        s+=n
    else:
        s2+=n
    n+=1
print(s)
print(s2)