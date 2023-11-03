num = int(input("Sıfırdan büyük bir sayı giriniz :"))

if num > 0:
    max_odd = num - 1 if num % 2 == 0 else num
    n = (max_odd + 1) / 2
    total = n ** 2
    print(f"1 ile {num} arasındaki tek sayıların toplamı {total}")
else:
    print("lütfen 0'dan büyük bir sayı giriniz")

n = 1
match n:
    case 1:
        print("sayı ")
    case 2:
        print("sayi")
