# def print_cube(n):
#     for i in range (1,n+1):
#         print("cube of",n,"is:",i**3)
# num =int(input("enter the value"))
# print("cube numbers up to",num,"are")
# print_cube(num)




# def my_si(p,t,r):
#     print((p*t*r)/100)
# my_si(10000,12,2)
# my_data= lambda p,t,r:((p*t*r)/100)
# print(my_data(10000,12,2)) 
 



# def my_ci (p,t,r):
#     return p*(1+(r/100))**t
# x=my_ci(1000,12,2)
# print(x)
# y=lambda p,t,r:(p(1+(r/100)))**t
# y=(1000,12,2)




# a=153
# b=len(str(a))
# c=a
# result=0
# while c>0:
#     digit= c%10
#     result +=(digit)**b
#     c=c//10
# if result==a:
#     print("this is a armstrong number")
# else:
#     print("this is not am  armstrong number")




# a=234
# b=len(str(a))
# c=a
# result=0
# while c>0:
#     digit= c%10
#     result+=(digit)**b
#     c=c//10
# if result==a:
#     print("THIS IS A ARMSTRONG NUMBER")
# else:
#     print("THIS IS AM ARMSTRONG NUMBER")



# a=567
# b=len(str(a))
# c=a
# result=0
# while c>0:
#  digit=c%4
#  result+=(digit)**b
#  c=c//4
# if result==a:
#  print("this is armstrong number")
# else:
#  print("this is not a am armstrong number")





# a= int(input("enter your number"))
# if a>1:
#     for i in range(2,a):
#         if a%2==0:
#             print("this is not a prime number")
#             break
#     else:
#        print("this is a prime number")
    





# a= int(input("enter your number"))
# if a>1:
#     for i in range(2,a):
#         if a%2==0:
#             print("this is not a prime number")
            
#     else:
#        print("this is a prime number")




# x=int(input("enter your first number"))
# y=int(input("enter your second number"))
# for a in range(x,y+1):
#     if a>1:
#         for i in range(2,a):
#             if a%i==0:
#                 break
#         else:
#            print(a)






# n=int(input("enter a number"))
# sum=0
# for i in range(1,n+1):
#     sum=sum+(i**2)
# print(sum)

    


# a=[1,5,50,500,22,-3]
# sum=0
# for i in  a:
#         sum=sum+(i**2)
# print(sum)





# a=[1,5,50,400,22,-3]
# b=[]
# for i in a:
#     b.append(i**2)
# print(b)



# a=[3,2,5,99,100]
# b=[]
# for i in a:
#     b.append(i**3)
# print(b)




# a=[2,22,222,2222,22222]
# def my_cube(a):
#     b=[]
#     for i in a:
#         b.append(i**3)
#     return b
# result =my_cube(a)
# print(result)





# a=[10,20,30,-40]
# def my_cube(a):
#     b=[]
#     for i in a:
#         b.append(i**3)
#     return b
# sum=my_cube(a)
# print(sum)
    





# a=[44,88,99,100,200,5,10]
# def my_sqr(a):
#     avg=0
#     for i in a:
#      avg=avg+(i**2)
#      return avg
# result=my_sqr(a)
# print(result)






# n=int(input("enter your fibonacci number"))
# a=0
# b=1
# if n==1:
#     print(a)
# elif n==2:
#     print(b)
# else:
#     print(a)
#     print(b)
#     for i in range(3,n+1):
#         c=a+b
#         a=b
#         b=c
#     print(b)






# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c #= float(input("Enter side c: "))
# s = (a + b + c) / 2
# area = (s * (s - a) * (s - b) * (s - c))**0.5
# print("area of the triangle=",area)






# a=4
# b=6
# temp=a
# a=b
# b=temp
# print(a,b)




# a=7
# b=5
# print("before using swap:",a,b)





# a=10
# b=4
# b,a=a,b
# print("after swap:",a,b)




# import random as gayee
# a=gayee.randint(2,9)
# print(a)









