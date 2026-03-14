# year=int(input("enter a year:"))
# if (year % 4==0):
#     print(year,"this is leap year")
# else:
#     print(year,"this is not leap year")




# def check_leap_year(year):
#     if   (year % 400 == 0):
#         print(year, "is a Leap Year")
#     else:
#         print(year, "is Not a Leap Year")

# year = int(input("Enter a year: "))
# check_leap_year(year)






# def my_largest(a, b, c):
#     if a >= b and a >= c:
#         print(a, "is largest")
#     elif b >= a and b >= c:
#         print(b, "is largest")
#     else:
#         print(c, "is largest")

# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# z = int(input("Enter third number: "))

# my_largest(x, y, z)




# num = 12
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)




# def multiplication_table(num):
#     print("Multiplication Table for", num)
    
#     for i in range(1, 11):
#         print(num, "x", i, "=", num * i)

# number = int(input("Enter a number: "))
# multiplication_table(number)





# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# terms = int(input("Enter number of terms: "))

# print("Fibonacci Sequence:")

# for i in range(terms):
#     print(fibonacci(i), end=" ")




def fibonacci(n):
    if n  <= 1:
        return n
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
terms = int(input("enter number of terms"))
print("fibonacci sequence")
for i in range(terms):
    print(fibonacci(i), end="")