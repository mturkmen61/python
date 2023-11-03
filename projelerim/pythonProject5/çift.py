number = int(input("bir sayı giriniz:"))

if number >= 0:
    for i in range(number, -1, -2):
        if i == 0:
            print("çift")
        elif i == 1:
            print("tek")
else:
    for i in range(number, 1, 2):
        if i == 0:
            print("çift")
        elif i == -1:
            print("tek")
