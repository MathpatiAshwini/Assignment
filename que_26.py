n=int(input("enter the number:-"))
i=1
l=[]
while i<=n:
    m=int(input("enter the number:-"))
    l.append(m)
    i+=1
l.sort()
print(l[-3])