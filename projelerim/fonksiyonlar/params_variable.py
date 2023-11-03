def sayilari_topla(a, *sayilar):
    print(a, type(a))
    print(sayilar, type(sayilar))
    toplam = 0
    for i in sayilar:
        toplam += i

    return toplam


sonuc = sayilari_topla(1, 2, 3)
print(sonuc)

# önce pozisyonel parametreler, sonra değişen uzunlukta parametreler