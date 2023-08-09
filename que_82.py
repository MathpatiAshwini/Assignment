i=1
l=[]
while i<=10:
    n=int(input("enter the number:-"))
    l.append(n)
    i+=1
l.sort()
print(l[0],l[9])