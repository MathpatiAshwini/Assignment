n=int(input("enter the number:"))
temp=n
i=1
while i<=n:
    if n%i==0:
        print(i,end=",")
    i+=1