cars = ["ferrari", "bmw", "toyota"]
colors = ["red", "blue", "yellow"]

zipped = list(zip(cars, colors))
print(zipped)

print(list(zip(*zipped)))

print(list(enumerate(zipped, 10)))

a = (1, 2, 3, 4, 5, 0)
print(all(a))

b = "     must     türk    "
print(b.strip())

a = ["must", 123, 0]
print(any(a))

# "" un karşılığı false'dur


print(set(reversed(a)))