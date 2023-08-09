basic_salary=int(input("entre the number:--"))
if basic_salary<=10000:
    print(basic_salary+basic_salary*20/100+basic_salary*80/100)
elif basic_salary>10000 and basic_salary<=20000:
    print(basic_salary+basic_salary*25/100+basic_salary*90/100)
elif basic_salary>20000:
    print(basic_salary+basic_salary*30/100+basic_salary*95/100)