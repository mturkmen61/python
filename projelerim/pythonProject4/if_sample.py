# a = int(input("Enter a number"))
# if (a % 2) == 0:
#     print("Even number")
# if a % 2 == 1:
#     print("Odd number")

sayi = int(input("Bölünecek sayıyı giriniz"))
bolen = int(input("Bölen sayıyı giriniz"))

kalan = sayi % bolen

if kalan == 0:
    print("{} sayısı {} sayısına tam bölünüyor".format(sayi,bolen))
else:
    print("{} sayısı {} sayısına tam bölünmüyor".format(sayi,bolen))
