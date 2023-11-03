# def must():
#     global number1, number2
#
#     number1, number2 = 10, 20
#     print(number1, number2)
#
#
# number1, number2 = 20, 5
# print(number1, number2)
# must()
# print(number1, number2)
# a = int(input())
# b = []
# c = []
# for i in range(a + 1):
#     b.append(list(input()))
# d = b[0].index("R")
# for i in range(1, a + 1):
#     if b[i][d - 1] != " " and b[i][d] == " ":
#         c.append(b[i][d - 2:d])
#     elif b[i][d] != " ":
#         c.append(b[i][d - 2:d + 1])
#     else:
#         c.append(b[i][d - 2])
#
# for i in range(len(c)):
#     c[i] = int("".join(c[i]))
#
# result = sum(c) / len(c)
# print(f"{result:.2f}")

# from collections import Counter
#
# purchase_list = []
# a = []
# b = []
# len_shoe = int(input())
# sizes = input().split(" ")
# len_custom = int(input())
# print(Counter(sizes))
# for i in range(len_custom):
#     a.append(input())
# for i in a:
#     if i.split(" ")[0] in Counter(sizes).keys():
#         if Counter(sizes)[i.split(" ")[0]] != 0:
#             b.append(i.split(" ")[1])
#             Counter(sizes)[i.split(" ")[0]] = Counter(sizes)[i.split(" ")[0]] - 1
#
# print(b)

# 10
#   4  6 7 8 9 2 3 4 1
# 15
# remove 1
# pop
# pop
# discard 2
# discard 3
# discard 4
# discard 1
# remove 5
# pop
# discard 6
# discard 1
# discard 8
# discard 0
# discard 9
# pop


# len_set = int(input())
# set1 = set((input().strip()).split(" "))
# print(set1)
# len_sets = int(input())
# a = []
# for i in range(len_sets * 2):
#     a.append((input().strip()).split(" "))
# print(a)
#
# for i in range(len(a)):
#     if a[i][0] == "intersection_update":
#         set1.intersection_update(set(a[i + 1]))
#         print(set1)
#     elif a[i][0] == "uptade":
#         set1.uptade(set(a[i + 1]))
#         print(set1)
#     elif a[i][0] == "symmetric_difference_uptade":
#         set1.symmetric_difference_update(set(a[i + 1]))
#         print(set1)
#     elif a[i][0] == "difference_uptade":
#         set1.difference_update(set(a[i + 1]))
#         print(set1)
# print(set1)

# try:
#     print(1/0)
# except ZeroDivisionError as e:
#     print("Error Code:",e)
# import re
# m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
# m.groups()
#
# print(type(m.groups()))
# for i in m.groups():
#     print(i)

a = int(input())
liste = []
for i in range(a):
    b = input().split(".")
    if len(b)==1:
        print("False")
    else:
        for i in b:
            if b[1].isdecimal() == True:
                    if b[0][0] == "+" or b[0][0] == "-":
                        if b[0][1:].isdecimal() == True:
                            print(True)
                        else:
                            print(False)
                    else:
                        if b[0].isdecimal() == True:
                            print(True)
                        else:
                            print(False)
            else:
                  print(False)