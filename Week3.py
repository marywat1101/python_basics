# print(len("jamilla"))

# s = "meredith"
# print(s[4])
# print(s[3])
# print(s[-2])

# s = "zmrzlina"
# print(s[4:-1])

# s = "broo"

# print(s[2:])
# print(s[:2])


# s = "butterfly"

# print(s[0:5:2])
# print(s[5:0:-1])

# s = "slivrussnesharabenchevigem"

# print(s[::-1])

# l = [3, 5, 9, 11, 15]
# print(l[3])
# print(l[len(l)-1])

# l = [3, 5, 9, 11, 15]
# print(l[-1])

# print(77 in [2, 8, 77, 3, 1])

# l = [3, 5, 9, 11, 15]
# l.append(20)
# l.append(30)
# print(l)
# l += [100, 200, 30]
# print(l)

# l = [3, 5, 9, 11, 15]
# l.insert(4, 13)
# print(l)

# l = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'grape']
# del l[3]
# print(l)

# del l[1:3]
# print

# l = [3, 5, 7, 9]
# m = l
# n = l.copy()


# print(l == m)
# print(l == n)

# Double or nothing 

# string = input("string: ")
# is_double = False


# for i in range(0, len(list(string))-1):
#     if string[i] == string[i+1]:
#         is_double = True

# if is_double == True:
#     print("double")
# else:
#     print("nothing")


# Capitalizing Words simple method

# string = "laura"

# print(string.title())

# Capitalizing Words
# one

# input = input("Enter input: ").split()

# for word in input:
#     l = list(word) 
#     l[0] = chr(ord(l[0])-32)
#     l = ''.join(l)
#     print(l, end=" ")  

# Password Generator

# from random import randint

# vowels = ["a","e","i","o","u"]
# consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

# password = ""
# while len(password) <= 8:

#     vowel = vowels[randint(0, len(vowels)-1)]
#     consonant = consonants[randint(0, len(consonants)-1)]

#     password += consonant
#     password += vowel

# print(password)

# String Comparison

# S = input("Enter S: ")
# T = input("Enter T: ")

# if S > T:
#     print(S)
# else:
#     print(T)

# S = input("Enter S: ")
# T = input("Enter T: ")

# for i in range(len(S)):
#     if ord(S[i]) > ord(T[i]):
#         print(S)
#         break
#     elif ord(S[i]) < ord(T[i]):
#         print(T)
#         break

# Starts With

# S = input("Enter S: ")
# T = input("Enter T: ")
# starts_with = False

# for i in range(len(T)):
#     if T[i] == S[i]:
#         starts_with = True
#     else:
#         starts_with = False
#         break

# print(starts_with)

# Contains

# no knowledge of functions yet

N = int(input("Enter N: "))
T = int(input("Enter T: "))

for i in range (1, T):
    l = []
    for j in range (i, i+N):
        l.append(j)
    if sum(l) == T:
        print(l)
        break
    elif sum(l) > T:
        print("none")
        break

        




        


