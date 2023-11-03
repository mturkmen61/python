liste = [1, 2, 3, 4, 5, 6]

yeni = [i for i in liste]
print(yeni)

must = [i for i in range(1, 51) if i % 5 == 0]
print(must)

movies = [
    ("the matrix", 1999),
    ("the matrix reloaded", 2003),
    ("the matrix revolutions", 2003),
    ("star trek beyond", 2016)
]

filtered = [(name) for (name, year) in movies if year > 2000]

print(filtered)

liste = [("ali", 30), ("veli", 10), ("memo", 12)]

yeni = {n: a for n, a in liste}
print(yeni)
