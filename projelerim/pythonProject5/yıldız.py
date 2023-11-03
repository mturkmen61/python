satir = int(input("satır sayısını giriniz"))

s = -1
if satir > 0:
    for i in range(1, satir + 1):
        s += 2
        star = "*" * s
        print(star.center(satir * 2))

s = -1


satir = int(input("satır sayısını giriniz:"))

for i in range(1, satir + 1):
    d = int((satir - 1) / 2 - i)
    print(" " * d, i * "*")
