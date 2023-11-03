# ['araba', 'ev', 'çamur', 'otoban', 'güzellik', 'spor']
# C = uzunlukları
# sesli_dict = sesli harf sayısı
# print sesli harf / uzunluk
# araba: 0.5
# ev: 0.5
# çamur: 0.4

len_dict = {}
sesli_dict = {}
kelimeler = ['araba', 'ev', 'çamur', 'otoban', 'güzellik', 'spor']
sesli_harfler = ["a", "e", "ı", "i", "o", "ö", "u", "ü"]
sesli_harf = sesli_dict.values()
uzunluk = len_dict.values()

for i in kelimeler:
    a = len(i)
    len_dict[i] = a
    for s in i:
        sesli_dict[i] = i.count(s)

for i in kelimeler:
    print(i, sesli_dict[i] / len_dict[i])

print(len_dict, sesli_dict)
