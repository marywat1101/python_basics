# Week 2
# print(int("12"))

# print(int(12.5))

# print(int(True))
# print(int(False))

# print(bool(12))
# print(bool(0))

# print(bool("Mary"))
# print(bool(""))
# print(bool(" "))

# print(str(False) == False)

# from math import *

# print(abs(-1))
# print(sqrt(49))

# print(exp(12))

# print(sin(10))

# import random

# print(random.uniform(1, 10))
# print(random.randint(1, 10))

# from random import uniform, randint

# print(uniform(1, 13))
# print(randint(1, 13))

# print(f"the value of 13 in binary, {13:b}")
# print(f"The value of 18.45 in decimal, {18.45:.1F}")
# print(f"The value of 15 in hex is, {15:x}")


# print(f"{2345:10d}")
# print("      1")

# import sys
  
# sum = 0
# for line in sys.stdin:
#     n = int(line)    # convert string to integer
#     sum += n
  
# print('The sum is', sum)

# Rolling N Dice

# from random import randint

# tries = int(input("How many dice? "))
# rolls = 0

# for i in range (tries):
#     dice = randint(1, 7)
#     print(dice, end=" ")
#     rolls += dice

# print(f"total: {rolls}")

# Flipping a Coin

# from random import randint

# heads = 0
# flips = 0

# while heads != 3:
#     coinflip = randint(0, 1)
#     if coinflip:
#         print("H", end="")
#         heads += 1
#     else:
#         print("T", end="")
#     flips += 1
# print(flips)

# Average

# import sys 

# sum = 0
# count = 0

# for line in sys.stdin:
#     number = float(line)
#     sum += number
#     count += 1
# print(sum / count)

# Positive and Negative

# import sys

# positive_sum, negative_sum = 0

# for line in sys.stdin:
#     number = int(line)
#     if number > 0:
#         positive_sum += number
#     else:
#         negative_sum += number

# print(f"Positive sum is: {positive_sum}")
# print(f"Negative sum is: {negative_sum}")

# Equal To The First

# import sys

# equal_to_the_first = 0
# first_number = 0
# count = 0

# for line in sys.stdin:
#     number = int(line)
#     if count == 0:
#         first_number = number 
#     if first_number == number:
#         equal_to_the_first += 1
#     count += 1
# equal_to_the_first -= 1
# print(equal_to_the_first)

# Second Largest???????????????????

# import sys

# first_largest = 1
# second_largest = 0

# for line in sys.stdin:
#     number = int(line)
#     if number > second_largest:
#         second_largest = first_largest
#         first_largest = number


# print(second_largest)

# Square

# N = int(input("N: "))

# print(N * "*")

# for i in range(0, N-2):
#     print(f"*{(N-2)*' '}*")

# print(N * "*")

# Triangle

# N = int(input("N: "))
# asterisks = 1

# while N != 0:
#     print(f"{(N-1)*' '}{asterisks*'*'}")
#     asterisks += 1
#     N -=1

# N = int(input("Enter N: ")) chatgpt

# for i in range(N):
    
#     print(" " * (N - i - 1), end="")
    
#     print("*" * (i + 1))


# AEIOU

# string = input("string: ")

# for c in string:
#     if c in "aeiouAEIOU":
#         print("vowels")
#         break
#     else:
#         print("no vowels")

# ASCII or Unicode

# string = input("string: ")

# only_ascii = True

# for c in string:
#     if ord(c) > 128:
#         only_ascii = False   

# if only_ascii == True:
#     print("ASCII")
# else:
#     print("Unicode")

# Spaces In Between

# string = input("string: ")

# for c in string:
#     print(c, end=" ")