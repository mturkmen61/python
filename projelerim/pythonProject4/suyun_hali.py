derece = int(input("suyun kaç derecede olduğunu giriniz"))
if derece >= 100:
    print("Su buhar haldedir")

if derece > 0 and derece < 100:
    print("Su sıvı haldedir")

if derece <= 0:
    print("Su katı haldedir")
