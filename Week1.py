# Paint
# width = int(input("Width: "))
# length = int(input("Length: "))
# height = int(input("Height: "))
# # Width*length+Width*height*2+length*height*2
# paint_needed = width*length+2*height*(width+length)
# print(paint_needed)

# The Greater Number
# x = int(input("x: "))
# y = int(input("y: "))

# if x > y:
#     print("x is greater")
# elif x == y:
#     print("x is equal to y")
# else:
#     print("y is greater")

# Quotient
# x = int(input("x: "))
# y = int(input("y: "))

# if x % y == 0:
#     print(f"{x} divided by {y} is {x//y}")
# else:
#     print("indivisible")

# Largest of Three
# x = int(input("x: "))
# y = int(input("y: "))
# z = int(input("z: "))

# if x > y and x > z:
#     print(f"largest is {x}")
# elif y > x and y > z:
#     print(f"largest is {y}")
# elif z > x and z > y:
#     print(f"largest is {z}")

# Numbers from 2 to 20
# for i in range(2,21):
#     if i % 2 == 0:
#         print(i)

# Factorial

# n = int(input('Enter n: '))
# factorial = 1

# for i in range(1, n + 1):
#     factorial *= i

# print('The factorial is', factorial)

# Exponentiation

# A = int(input("A: "))
# B = int(input("B: "))

# exponent = 1

# while B > 0:
#     exponent *= A 
#     B -= 1

# print("exponent is", exponent)

# All Divisors

# N = int(input("N: "))
# number_of_divisors = 0

# for i in range(1, N+1):
#     if N % i == 0: 
#         print(i)
#         number_of_divisors += 1

# print(f"number of divisors is {number_of_divisors}")

# Making change

# price = int(input("price: "))

# if price // 20 >= 0:
#     print(f"20 kc: {price // 20}")
#     price -= (price // 20) * 20
# if price // 10 >= 0:
#     print(f"10 kc: {price // 10}")
#     price -= (price // 10) * 10
# if price // 5 >= 0:
#     print(f"5 kc: {price // 5}")
#     price -= (price // 5) * 5
# if price // 1 >= 0:
#     print(f"1 kc: {price // 1}")

# Power of Two

# N = int(input("Enter Number: "))

# for i in range(0, N):
#     if 2 ** i == N:
#         print("pow")
#         break

#     if 2 ** i > N:
#         print("no")
#         break

# # Smallest Power

# N = int(input("Enter: N "))

# pow = 0

# while pow ** 2 >= N:


# Number Guessing

# print("Think of a number from 1 to 1000.")

# low_range = 1
# high_range = 1000

# X = (high_range + low_range) // 2
# c = input(f"My Guess: {X}. Is this (h)igh, (l)ow, or (c)orrect? ")
# total_guess = 0

# while c != "c":

#     if c == "h":
#         high_range = X
#         X = (high_range + low_range) // 2
#     if c == "l":
#         low_range = X
#         X = (high_range + low_range) // 2

#     c = input(f"My Guess: {X}. Is this (h)igh, (l)ow, or (c)orrect? ")   
#     total_guess += 1

# print(f"Total guess is {total_guess - 1}") 

# Leap Years

# year = int(input("Enter Year: "))

# if year % 4 == 0 and year % 100 != 0:
#     print("leap")
# elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#     print("leap")
# else:
#     print("no leap")

# Smallest Power

# N = int(input("Enter N: "))

# for i in range (0, N):
#     if 2 ** i >= N:
#         print(2 ** i)
#         break

# Largest Power

# N = int(input("Enter N: "))

# if N >= 1:
#     pow = 0

#     while 2 ** pow <= N: 
#         pow +=1

#     pow -= 1    
#     print(2 ** pow)

# ??????????????????Number of Digits

# Multiples of 3 and 5

# sum = 0

# for i in range(1, 1001):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i

# print(sum)

# ??????????????????Even Fibonacci numbers









