n=int(input("enter the number:--"))
i=1
temp=n
s=0
while n!=0:
    d=n%10
    s+=d**3
    n//=10
if s==temp:
    print(temp,"is armstrong number")
else:
    print(temp,"is not armstrong number")