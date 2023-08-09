n = int(input("Enter the value of N: "))
i=1
while i<=n:
    j=1
    while j<=i:
        if i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j+=1
    i+=1
    print()





    