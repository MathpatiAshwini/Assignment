n=int(input("enter the number:"))
x=input("enter the number:")
i=1
j=5
s=0
while i<=n:
    s+=j
    i+=1
    print(j,end="+")
    j=j*10+5
print("=",s)


# i=0
# str="5"
# while i<n:
#     print(str,end="+")
#     str+="5"
#     i+=1