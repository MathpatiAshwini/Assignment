a1=int(input("enter the number"))
a2=int(input("enter the number"))
a3=int(input("enter the number"))
a4=int(input("enter the number"))
a5=int(input("enter the number"))
s=a1+a2+a3+a4+a5
avr=s/5
if avr>=90:
    print("grade a")
elif avr>=80 and avr<90:
    print("grade b")
elif avr>=70 and avr<80:
    print("grade c")
elif avr >=60 and avr <70:
    print("grade d")
elif avr>=40 and avr<60:
    print("grade e")
else:
    print("grade c")