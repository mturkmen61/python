"""a = 19
name = 'haruna'

if a > 15:
    print("15'ten büyük")
    if len(name) % 2 == 0:
        tc = name + '_123_cift'

    else:
        tc = name + '_123_tek'
    print('tc no:', tc)
else:
    print("15'ten küçük")"""


a = 'harun turk men'

if len(a) > 10:
    print('uzun')
    if a.count(' ') == 0:
        print('boşluk yok')
    else:
        if a.count(' ') == 1:
            name = a.split(' ')[0]
            surname = a.split(' ')[1]
            print('name:', name, 'surname:', surname)
        elif a.count(' ') == 2:
            name1 = a.split(' ')[0]
            name2 = a.split(' ')[1]
            surname = a.split(' ')[2]
            print('name 1:', name1, 'name 2:', name2, 'surname:', surname)
        else:
            print('c')
else:
    print('kısa')
    if len(a) % 2 == 0:
        print('çift')
    else:
        print('tek')