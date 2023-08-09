units =int(input("enter the units:--"))
if units==50:
    bill=units*0.50
elif units==100:
    bill=units*0.75
elif units ==200:
    bill=units*1.20
elif units==250:
    bill=units*1.50
total=units+bill
print(total)
