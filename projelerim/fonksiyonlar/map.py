numbers = [1, 2, 3, 45, 6]


def calculate_power(num):
    return num ** 2


# powers = list(map(calculate_power, numbers))

cities = [
    ("istanbul", 25),
    ("izmir ", 30),
    ("ankara", 20),
]

# def c_to_f(temp):
#     f = (temp * (9 / 5)) + 32
#     return f
#
#
# cities_f = []
# for c in cities:
#     results = c[0], c_to_f(c[1])
#     cities_f.append(results)

# print(cities_f)

c_to_f = lambda city: (city[0], (city[1] * (9 / 5) + 32))
cities_f = list(map(c_to_f, cities))
print(cities_f)

values = [0, " ", None, 15]
new_values = tuple(filter(None, values))
print(new_values)
