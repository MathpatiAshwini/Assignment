# selling_p=int(input("enter the number:--"))
# cost_p=int(input("enter the number:--"))
# total=selling_p-cost_p
# if selling_p>cost_p:
#     print(total/cost_p*100)
# else:
#     print("invalid")



selling_p=int(input("enter the number:--"))
cost_p=int(input("enter the number:--"))
total=cost_p-selling_p
if selling_p<cost_p:
    print(total/cost_p*100)
else:
    print("invalid")
