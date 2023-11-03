sayi = int(input("tek sayı giriniz:"))

for i in range(sayi):
    i += 1
    if i <= sayi / 2 + 1:
        print(i * " *")
    else:
        print(((sayi + 1) - i) * " *")
