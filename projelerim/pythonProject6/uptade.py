ogrenci = {"isim": "mustafa", "not": 8.26, "donem": 1990, "sınıf": "11F"}
kaynak = {"adres": "istanbul", "sınıf": "9B"}

print(ogrenci)
ogrenci.update(kaynak)
print(ogrenci)
ogrenci = {"isim": "mustafa", "not": 8.26, "donem": 1990, "sınıf": "11F"}

must = [("sinif", "11F"), ("adres", "istanbul")]

ogrenci.update(kaynak)
print(kaynak)


print(ogrenci.keys())
ogrenci["isim"] = "must"


