# queastion_1

# n=int(input("enter the number:"))
# if n%5==0 and n%11==0:
#     print("both")
# elif n%5==0:
#     print("5")
# elif n%11==0:
#     print("11")
# else:
#     print("none")

# queastion_2

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))

# if a+b>c or b+c>a or c+a>b:
#     print("validate tringle")
# elif a==b or b==c or c==a:
#     print("equilateral ")
# elif a!=b or b!=c or c!=a:
#     print("scalene")
# elif (a==b and a!=c) or (b==c and c!=a) or (c==a and c!=b):
#     print("isosceles ")
# if a*a+b*b==c or b*b+c*c==a*a or c*c+a*a==b*b:
#     print("right-angled triangle")

# queastion_3

# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=int(input("enter the number:"))
# if a>b:
#     max=a
#     sec=b
# else:
#     max=b
#     sec=a
# if max>c:
#     if sec<c:
#         print(c)
#     else:
#         print(sec)
# else:
#     print(max)

# queastion__4
# n = int(input("enter the number:"))
# s = 0
# while n > 0:
#     r = n % 10
#     s += r
#     n //= 10
#     if  s > 9:
#         s = s % 10 + s // 10
# print(s)


# queastion_5
# n=int(input("enter the number:"))
# x=n*2
# i=1
# while i<=x+1:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c>2:
#         print(i)
#     i+=1


# queastion_6
# n=int(input("enter the number:"))
# i=1
# x=2
# p=x
# s=0
# while i<=n:
#     s+=p
#     p=p*10+x
#     i+=1
# print(s)

# queastion_7
# n=int(input("enter the number:-"))
# i=1
# k=i
# while i<=n:
#     j=1
#     while j<=i:
#         print(k,end=" ")
#         j+=1
#         k+=1
#     i+=1
#     print()

# queastion_10
# l=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
# i=0
# while i<len(l):
#     if l[i]<0:
#         r=l[i]
#         print(r,end=" ")
#     i+=1
# k=0
# while k<len(l):
#     if l[k]>0:
#         p=l[k]
#         print(p,end=" ")
#     k+=1