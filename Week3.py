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

input = input("Enter input: ").split()

for word in input:
    l = list(word) 
    l[0] = chr(ord(l[0])-32)
    l = ''.join(l)
    print(l, end=" ")  



