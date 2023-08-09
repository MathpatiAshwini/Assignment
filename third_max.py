a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))
if a > b:
    max1 = a
    sec1 = b
else:
    max1 = b
    sec1 = a
if c > d:
    max2 = c
    sec2 = d
else:
    max2 = d
    sec2 = c
if max1 > max2:
    if max2 > sec1:
        third = sec1
    else:
        third = max2
else:
    if max1 > sec2:
        third= sec2
    else:
        third = max1

print( third)


a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
d = int(input("Enter the number: "))
if a > b:
    max1 = a
    sec1 = b
else:
    max1 = b
    sec1 = a
if c > d:
    max2 = c
    sec2 = d
else:
    max2 = d
    sec2 = c
if max1 > max2:
    if max2 > sec1:
        third = sec1
    else:
        third = max2
else:
    if max1 > sec2:
        third= sec2
    else:
        third = max1

print( third)


