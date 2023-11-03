sayilar = [10, 20, 30]
sayilar.append(35)

list.append(sayilar, 25)

sayilar = sayilar + [100, 200]
print(sayilar)

sayilar.insert(2, 25)
list.insert(sayilar, 11, 5)
print(sayilar)

eklenecek = [55, 65, 75, 86]

(sayilar.extend(eklenecek))
print(list.extend(sayilar, eklenecek))
print(sayilar)
