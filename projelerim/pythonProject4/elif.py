n1=int(input("Birinci sayıyı giriniz"))
n2=int(input("İkinci sayıyı giriniz"))
n3=int(input("Üçüncü sayıyı giriniz"))

if n1==n2 and n1==n3:
    print("Sayılar eşittir")
elif n1>n2 and n1>n3:
    print("Birinci sayı büyüktür")
elif n2>n1 and n2>n3:
    print("İkinci sayı büyüktür")
else:
    print("Üçüncü sayı büyüktür")