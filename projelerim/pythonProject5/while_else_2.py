metin = input("Bir metin giriniz:")
uzunluk = len(metin)
indeks = 0


while indeks < uzunluk:

    harf = metin[indeks]
    print(harf)
    if harf == "t":
        print("Bulundu")
        break
    indeks += 1


else:
    print("Bulunamadı")

