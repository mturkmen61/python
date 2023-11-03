# sınıf dictionarysini oluştur
# class_dict -> toplam kişi sayısı ve sınıf ortalaması
# >= 50 dict'i
# greater_than_50_dict
# < 50 dict'i
# lower_than_50_dict
class_dict = {}
greater_than_50_dict = {}
lower_than_50_dict = {}

while True:
    name = input("enter name:")
    if name == "exit":
        break
    grade = int(input("enter grade:"))
    class_dict[name] = grade

keys = class_dict.keys()
values = class_dict.values()
for i in keys:
    if class_dict[i] >= 50:
        greater_than_50_dict[i] = class_dict[i]

    else:
        lower_than_50_dict[i] = class_dict[i]

print("greater than 50", greater_than_50_dict)
print("lower than 50", lower_than_50_dict)

total = 0
print('type:', type(values))
for i in values:
    total += i
print("total number :", len(class_dict), "  class average:", total / len(class_dict))
