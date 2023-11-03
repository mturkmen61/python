total = int(input("Kaç satır olsun:"))

if total > 0:

    for num in range(total):
        count = ((num + 1) * 2) - 1
        star = "*" * count
        print(star.center(total*2))
