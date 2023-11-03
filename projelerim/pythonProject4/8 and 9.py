a = 100
b = 69

percentage = b / a * 100
print("percantage", percentage)

if percentage > 75:
    print("girebilirsin")

else:
    c = input("has student any medical cause? 'Y' or 'N'")
    if c == 'Y':
        print('girebilirsin')
    elif c == 'N':
        print('giremezsin')

