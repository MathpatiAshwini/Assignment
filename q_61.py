n=int(input("enter the number:--"))
temp=n
c=0
while n>0:
    c+=1
    r=n%10
    n//=10
if c==1 :
    print(temp," is one digit")
elif c==2:
    print(temp,"is two digit")
elif c==3:
    print(temp,"three digit")
else:
    print(temp,"is more then three digit")