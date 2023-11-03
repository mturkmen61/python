baslangic = int(input("Başlangıç değeri:"))
bitis = int(input("Bitiş değeri:"))

toplam = 0
for sayi in range(baslangic + 1, bitis):
    toplam += sayi
print("{} ile {} arasındaki sayıların toplamı {}".format(baslangic, bitis, toplam))
