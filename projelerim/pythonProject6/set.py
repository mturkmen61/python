degerler = [1, 2, 3, 4, 5, (10, 20, 10), 1, (10, 20, 39), 2, 3]
print(set(degerler))

a = {1, 2, 3, 4}
b = {1, 0, 4, 5}

# birlesim = a|b
# kesisim = a & b
# fark = a - b
# simetrik_fark = a ^ b

# fonksiyonlar = len, sum, min, max, del, sorted
c = (1, 2, 3, 4)
print(type(c))

# d = [1, 2, 3, 4, 5, 6, 1, 2, 3]
# d = set(d)
# print(d)
# print(d[0])

a.add(123)
print(a)

a.update(b)
print(a)

# isdisjoint = ayrık küme,issubset = alt küme mi ,issuperset = üst küme mi
# difference kümeleri birbirinden çıkarır