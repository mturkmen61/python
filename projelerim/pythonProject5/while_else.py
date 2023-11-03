# 1.Program döngü içerisine girmezse
# 2.Döngü içerisine girdikten sonra break deyimi ile sonlanmayıp tüm iterasyon tamamlanırsa

metin = "python"


for harf in metin:

    if harf == "t":
       print("Bulundu")
       break
else:

 print("Bulunmadı")
