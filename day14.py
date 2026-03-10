# a=int(input("enter the one values"))
# b=int(input("enter the two values"))
# c=a+b
# def add(a,b):
#     return a+b
# d=lambda a,b:a+b
# print(30,50) 




# from math import sqrt 
# def nthFib(n):
#     res = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
#     print(int(res),'is',str(n)+'th fibonacci number')
# nthFib(12)




# import math
# def is_perfect_square(x):
#     s = int(math.sqrt(x))
#     return s * s == x
# def is_fibonacci(n):    
#     return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)
# num = 1
# if is_fibonacci(num):
#     print(f"{num} is a Fibonacci number.")
# else:
#     print(f"{num} is NOT a Fibonacci number.")






# import math
# r=4
# area=math.pi*math.pow(r,2)
# print(area)


# x, y = 3,9 
# primes = [True] * (y + 1)
# primes[0], primes[1] = False, False

# for i in range(2, int(y ** 0.5) + 1):
#     if primes[i]:
#         for j in range(i * i, y + 1, i):
#             primes[j] = False

# res = [i for i in range(x, y + 1) if primes[i]]
# print(res if res else "No")



# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# maximum = num1 if num1 > num2 else num2
# print("Maximum number is:", maximum)




# n, m = 4, 3
# a, b, count = 0, 1, 0

# while True:
#     a, b = b, a + b
#     if b % m == 0:
#         count += 1
#         if count == n:
#             print(b)
#             break



# def fun(n, m):
#     fib = [0, 1]
#     count = 0
    
#     while True:
#         fib.append(fib[-1] + fib[-2])
#         if fib[-1] % m == 0:
#             count += 1
#             if count == n:
#                 return fib[-1]

# n, m = 4, 3
# print(fun(n, m))




# def fib(n, memo={0: 0, 1: 1}):
#     if n not in memo:
#         memo[n] = fib(n - 1, memo) + fib(n - 2, memo) 
#     return memo[n]

# def fun(n, m):
#     count, idx = 0, 2 
#     while True:
#         value = fib(idx)  
        
#         if value % m == 0: 
#             count += 1
#             if count == n:  
#                 return value  
#         idx += 1  

# n, m = 4, 3  
# print(fun(n,m))



# def fib(n):
#     F = [[1, 1],
#          [1, 0]]
#     if (n == 0):
#         return 0
#     power(F, n - 1)

#     return F[0][0]


# def multiply(F, M):
#     x = (F[0][0] * M[0][0] +
#          F[0][1] * M[1][0])
#     y = (F[0][0] * M[0][1] +
#          F[0][1] * M[1][1])
#     z = (F[1][0] * M[0][0] +
#          F[1][1] * M[1][0])
#     w = (F[1][0] * M[0][1] +
#          F[1][1] * M[1][1])

#     F[0][0] = x
#     F[0][1] = y
#     F[1][0] = z
#     F[1][1] = w

# Optimized version of
# power() in method 6


# def power(F, n):
#     if(n == 0 or n == 1):
#         return
#     M = [[1, 1],
#          [1, 0]]

#     power(F, n // 2)
#     multiply(F, F)

#     if (n % 2 != 0):
#         multiply(F, M)


# # Driver Code
# if __name__ == "__main__":
#     n = 5
#     print(fib(n))




# n = int(input("Enter a number: "))

# sum_of_cubes = (n * (n + 1) // 2) ** 2

# print("Sum of cubes of first", n, "natural numbers is:", sum_of_cubes)








# n=int(input("enter a number " ))
# print("cube number up to",n,"are")
# for i in range (1,n+1):
#     print("cube of",i,"is:",i**3)
