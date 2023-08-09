y=int(input("enter the year:"))

if  y%400==0 or y%100!=0:
    if y%4==0 :
        print(y,"leap year")
    else:
        print(y,"not leap year")
else:
    print(y,"not leap year")    