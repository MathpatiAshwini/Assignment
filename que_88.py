n=int(input("enter the number:-"))
i=1
j=1
v=1
while i<=n:
    if i%2==0:
        print(i*i,end="-")
    else:
        print(i*i,end="+")
    i+=1
