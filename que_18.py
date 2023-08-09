n=int(input("enter the number:"))
temp=n
i=1
s=0
while i<n:
    if n%i==0:
        s+=i
    i+=1
if s==temp:
    print(n,"is perfect number")
else:
    print(n,"is not perfect number")