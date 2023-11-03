# a = [10, 20, 30, 40]
# b = a
# c = b
# a[1] = 50
# print(c)
# a[len(a)-1] = a[0]
# a[0] = a[len(a) - 1]
# print(c)
#
# t = len(a)
# print(t)
#
# sayilar = [10, 20, 30, 40, "z"]
# print(min(sayilar, key=str))
# print(max(sayilar, key=str))
#
# numbers = []
# print(min(numbers, default=0))
#
# h = [10, 20, 30, 40, 50]
# toplam = sum(h, 100)
# print(toplam)

# del a[2]
# del a[0:3]
# print(a)
#
# numb = [1, 3, 5, 7, 6, 8]
# print(sorted(numb))
# print(sorted(numb, reverse=True))
#
# numb = ["must", "türkmen", "trabzon"]
# print(sorted(numb, key=len, reverse=True))


line_number = 10
star_number = 4
a = [(line_number - star_number) * "-"]
print(a)
s = 0

if star_number <= line_number / 2:
    for i in range(0, star_number):
        s += 1

print(s * "*", a[0], sep="")


a
