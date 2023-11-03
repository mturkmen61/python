# def change_fn(s, i, c):
#     s = s[:i] + c + s[i + 1:]
#     return s
#
#
# s = "Harun"
# print(change_fn(s,0,s[0].lower()))
#
# # for i in range(len(s)):
# #     c = s[i]
# #
# #     c = c.upper()
# #     s = change_fn(s, i, c)
# #
# # print(s)
#
# print(s[0].lower())


#
# s = "MjdsqjkqÖmdq"
# print(s[0].islower())
# length = len(s)
# for i in range(length):
#     if s[i].islower:
#         print(True)
#
#     else:
#         print(False)


# def split_and_join(line):
#     a = input().split(" ")
#     for i in a:
#         print(i, end="-")
#
#
# line = input()
# result = split_and_join(line)
# print(result)

#
# def print_full_name(first, last):
#     print(first)
#
#
# first_name = input()
# last_name = input()
# print_full_name(first_name, last_name)
#
#
# def summer(a, b):
#     c = a + b
#     return c

# c = "ab"
# s = "aab"
#
# for i in s:
#     if i not in c:
#         c += i
# print(c)

#
# a = [["a","b"],["c","d"]]
# b = []
# for i in a:
#     b.append("".join(i))
# print(b)
#

# from itertools import combinations
#
# a = input().split(" ")
# liste = []
# yeni_liste  = []
# letters = a[0]
# number = int(a[1])
# for i in letters:
#     liste.append(i)
# for i in range(number+1):
#     i += 1
#     a=(list(combinations(liste,i)))
#     for s in a:
#         s = list(s)
#         s = "".join(s)
#         yeni_liste.append(s)
#     print(yeni_liste)
# print(a)

from itertools import combinations

# l = "HACK 3"
# l, n = l.split(' ')
# n = int(n)
# l = sorted(l)
#
# for comb_n in range(1, n + 1):
#     comb_list = list(combinations(l, comb_n))
#     for i in comb_list:
#         # print(i)
#         for j in i:
#             print(j, end='')
#         print()
#
# a = [[1, 2, 3], [3, 4, 5]]
# for i in range(len(a)):
#     for s in a[i]:
#         print(s, end="")
#
#     if i < len(a) - 1:
#         print()
#
# print('qwe')

# b = "112223331"
# a = [int(i) for i in b]
#
# liste = []
# print(a)
# ctr = 0
# for i in range(1, len(a)):
#     if a[i] != a[i - 1]:
#         liste.append(a[i - (ctr + 1): i])
#         ctr = 0
#     else:
#         ctr += 1
#
#     # if last element
#     if i == len(a) - 1:
#
#         # if last element is same as left
#         if a[i] == a[i - 1]:
#             print(i, ctr)
#             liste.append(a[i - ctr:])
#         # if last element is different as left
#         else:
#             liste.append([a[i]])
#
# for i in liste:
#     d = (len(i),i[0])
#     print(tuple(d))
#

s = "h ar u n"
s = s.replace(' ', '')
print(s)
let_num = 10
letters = "a z e i o a f g h k "
letters = letters.replace(" ","")
print(letters)
group_num = 5
list1 =[]
list2 = []
list3 = []
for i in range(let_num):
    list1.append(i+1)

for i in letters:
    list2.append(i)

for i in list(combinations(list1, group_num)):
    print(i)
    for s in i:
        if letters[s-1] == "a":
            if i not in list3:
                list3.append(i)
print(list3)

print(len(list3)/len(list(combinations(list1, group_num))))

d = 12.161357531651
print(round(d,4))









