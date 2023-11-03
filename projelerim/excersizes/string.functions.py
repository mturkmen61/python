# <metin>.lower()   verilen metnim tüm harflerini küçük harfe çevirir
# <metin>.upper()   metnin tüm harflerini büyük yapar
# <metin>.title()   metindeki kelimelerin baş harflerini büyük yapar
# <metin>.capitalize()   ilk harf büyük diğerleri küçük
# <metin>.swapcase()   metindeki büüyk harfleri küçük, küçük harfleri büyük yapar

print("BUGÜN HAVA ÇOK GÜZEL".lower())
orjinal="BUGÜN HAVA ÇOK GÜZEL"
print("Orjinal metin:",orjinal)
print("küçüğe çevrilmiş metin:",orjinal.lower())
print("küçüğe çevrilmiş metin:",str.lower(orjinal))
print("Orjinal metin:",orjinal)

print("BUGÜN HAVA ÇOK GÜZEL".capitalize())
orjinal="BUGÜN HAVA ÇOK GÜZEL"
print("Orjinal metin:",orjinal)
print("büyüğe çevrilmiş metin:",orjinal.capitalize())
print("büyüğe çevrilmiş metin:",str.capitalize(orjinal))
print("Orjinal metin:",orjinal)

print("BUGÜN HAVA ÇOK GÜZEL".swapcase())
orjinal="BUGÜN HAVA ÇOK GÜZEL"
print("Orjinal metin:",orjinal)
print(" çevrilmiş metin:",orjinal.swapcase())
print(" çevrilmiş metin:",str.swapcase(orjinal))
print("Orjinal metin:",orjinal)



