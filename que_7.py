n=int(input("enter the number:"))
i=1
s=0
c=0
while c<n:
    if i%3==0:
        s+=i**2
        c+=1
    i+=1
print(s)
