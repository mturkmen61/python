def kimlik_goster(**kimlik):
    print(kimlik, type(kimlik))
    # for k in kimlik.items():
    #     print(k[0], k[1])
    for k, v in kimlik.items():
        print(k, v)


kimlik_goster(adi="mustafa", soyadi="türkmen", dogumyeri="istanbul")


def looker(a, *numbers, b, **identity):
    print(a)
    print(numbers)
    print(b)
    print(identity)


looker(10, 20, 20, 30, 40, 50, b=13, name="must", surname="türkmen", birth="trabzon")

# önce pozisyonel parametreler, sonra değişken uzunlukta isimsiz parametreler,isimli parametreler, değişken uzunlukta isimli parametreler
