baslangic = int(input("Başlangıç değeri:"))
bitis = int(input("Bitiş değer:"))

toplam = 0
for sayi in range(baslangic, bitis + 1):
    if sayi % 2 == 0:
        toplam += sayi
print(toplam)
