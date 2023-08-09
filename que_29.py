n=int(input("enter the number:"))
i=2
while i<=n:
    if n%i==0:
        j=1
        c=0
        while j<=i:
            if i%j==0:
                c+=1
            j+=1
        if c==2:
            print(i,end=",")
    i+=1