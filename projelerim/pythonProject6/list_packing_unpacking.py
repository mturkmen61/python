liste = [1, 2, 3]
a, b, c = liste
print(a)

list = [1, 2, 3, 4, 5]

x, y, *z = list
print(x, y, z)

*_, t = list
print(_)

word = "python"
l1, *l2, l3 = word
print(l1, l2, l3)
