n=int(input("enter the number:--"))
i=1
while i<=n:
    j=1
    c=0
    s=0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    if c==2:
        s+=i
    i+=1
    print(s)

