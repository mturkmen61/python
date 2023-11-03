kontrol = True
while kontrol:
    secim = input("Yapmak istediğiniz işlemi giriniz:")

    if secim == "q":
        kontrol = False
        print("Program sonu")
    elif secim == "Topla":
        topla1 = int(input("ilk sayıyı giriniz:"))
        topla2 = int(input("İkinci sayıyı giriniz:"))
        print(f"{topla1} + {topla2} = {topla1 + topla2}")


