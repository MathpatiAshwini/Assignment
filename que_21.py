n=int(input("enter the number:-"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end=" ")
        j+=1
    j=i-1
    while j>=1:
        print(j,end=" ")
        j-=1
    print()
    i+=1