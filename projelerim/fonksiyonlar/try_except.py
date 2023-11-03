# try:
#     sayi1 = int(input("first"))
#     sayi2 = int(input("second"))
#     result = sayi1 / sayi2
#
# except:
#     print("olmadı mlsf")
#
# print("try again")

#
# try:
#     sayi = int(input("sayı giriniz:"))
#     if sayi < 0:
#         raise ValueError("lütfen 0'dan büyük bir sayı giriniz")
#
#     print("congrats")
# except ValueError as hata:
#     print("hata mesajı", hata)


while True:
    a = input("enter a name")
    a.split(",")
    b = a[0]
    c = a[1]
    print(b,c)