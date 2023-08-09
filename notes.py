amount=int(input("enter the reppes:"))
notes=[2000,500,200,100,50,20,10,5,2,1]
count={}
for i in notes:
    if amount>=i:
        count[i]=amount//i
        amount = amount % i
    
print(count)
