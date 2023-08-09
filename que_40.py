m=int(input("enter the number:-"))
i=1
l=[]
while i<=m:
    n=int(input("enter the number:-"))
    l.append(n)
    i+=1
p=int(",".join(map(str,l)))
print(sum(p))

