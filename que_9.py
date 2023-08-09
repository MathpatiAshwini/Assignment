lower=int(input("enter the number:"))
upper=int(input("enter the number:"))
p=int(input("enter the number:-"))
q=int(input("enter the number:-"))
s=0
i=1
while lower<=upper:
    if lower%p==0 and lower%q!=0:
        s+=lower
    lower+=1
print(s)