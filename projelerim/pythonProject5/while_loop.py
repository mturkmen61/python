a = 0
while a < 5:
    print("Döngü çalışıyor")
    a = a + 1

print("Progrem sonu")

control = True
total = 0

while control == True:
    answer = input("Bir sayı giriniz:")
    if answer.isdigit():
        num = int(answer)
        total += num
    else:
        if answer == "ç":
            control = False
        print(total)

