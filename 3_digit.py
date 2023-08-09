n=int(input("enter the number:"))
temp=n
c=0
while n>0:
    r=n%10
    c+=1
    n//=10
if c==3:
    print(temp,"is 3 digit number")
else:
    print(temp,"is not 3 digit number")