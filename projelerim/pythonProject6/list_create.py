# cities = ["istanbul", "İzmir", "Ankara", "Antalya"]
# print(cities)
#
# a = [10, 20, 30]
# print(a[1])
#
# a[1] = 100
# print(a)

b = [10, 20, 30]
c = b

print("b değişkeninin değeri", b, "adresi", id(b))
print("c değişkeninin değeri", c, "adresi", id(c))

b[0] = 20
print("b değişkeninin değeri", b, "adresi", id(b))
print("c değişkeninin değeri", c, "adresi", id(c))

