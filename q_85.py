n=int(input("entre the number:--"))
if n%5==0 :
    print("divisible by 5")
elif n%11==0:
    print("divisible by 11")
elif n%5==0 and n%11==0:
    print("divisible by both")
else:
    print("none")