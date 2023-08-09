
a=int(input("enter the number:-"))
b=int(input("enter the number:-"))
c=int(input("enter the number:-"))

if a > b:
    max = a
    sec = b
else:
    max= b
    sec= a

if c > max:
    sec= max
    max = c
elif c > sec:
    sec = c

print( sec)