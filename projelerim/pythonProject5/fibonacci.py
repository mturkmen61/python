# 0 1 1 2 3 5 8 13

number = int(input("sayı adetini giriniz:"))
first = 0
second = 1
for i in range(number):
    i += 1
    third = first
    first = first + second
    second = third
    print(second)


