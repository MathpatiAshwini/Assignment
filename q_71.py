
dd=int(input("enter the date"))
mm=int(input("enter the moth"))
yy=int(input("enter the year"))

if dd>=1 and dd<=31:
    if mm==1 or mm==3 or mm==5 or mm==7  or mm==8 or mm==10 or mm==12:
        if yy%4!=0 or  yy%100==0 or yy%400!=0 :
            print(dd,'/',mm,'/',yy, "is valid date")
        else:
            print("not valid"


