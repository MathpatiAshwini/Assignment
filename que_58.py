n = int(input("Enter the value of N: "))
for row in range(n):
    for col in range(n-2):
        if (col==0 )or (col==4 and (row!=0 and row!=6)) or (row==0 or row==6) and (col>0 and col<4): 
            print("*",end=" ")
        els
            print(end=" ")
    print()