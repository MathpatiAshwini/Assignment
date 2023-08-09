n=int(input("enter the number:"))
m=int(input("enter the number:"))
s=n+1
while s<m:
    if s%2==0:
        print(s,end=",")
    s+=1