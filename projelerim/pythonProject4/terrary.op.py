sayi = 10
if sayi % 2 == 0:
    print("çift")

else:
    print("Tek")

print("Çift") if sayi % 2 == 0 else print("Tek")

print("Çift" if sayi % 2 == 0 else "Tek")

a, b = 10, 20
if a == b:
    print("a sayısı b'den büyüktür")
elif a > b:
    print("a sayısı b'den büyüktür")
else:
    print("b sayısı a'dan büyüktür")

print("her iki sayı eşittir" if a == b else "a sayısı b'den büyüktür" if a > b else "b sayısı a'dan büyüktür")
