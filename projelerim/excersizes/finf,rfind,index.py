a = "bugün hava çok güzel"
# print(a.find("hava"))
# print(str.find(a,"a"))
# print(str.find(a,"a",7))
# print(str.find(a,"a",10,14))
# # find , index soldan sağa tarar    rfind, rindex sağdan sola
print(str.rindex(a, "l"))
print(a.index("bugün"))


# adın: harun
# soyadın: türkmen
# yaşın: 24
# harun_turkmen_1998@gmail.com


# mailini gir: asdawdasddas@hdfgotmail.cogfdfm
# gmail

# name= input("enter your name")
# surname= input("enter your surname")
# age= int(input("enter your age"))
# year=str(2022-age)
# mail=name+surname+year+"@gmail.com"
# print(mail)

# mail=input("enter your mail")
# a= mail.split("@")
# b= a[1]
# c= b.rsplit(".")
# d= c[0]
# print(d)
# a=mail.find("@")
# b=mail.find(".")
# print(mail[int(a)+1:int(b)])

def get_diff(a, b):
    diff = ''
    for i, j in enumerate(a):
        if j != b[i]:
            diff += j
    return diff


# a = 'abcdefgpi'
# b = 'abcdefphi'
#
# print(get_diff(b, a))

# a= input("enter a name ")
# b= a.upper()
# c= a.lower()
# small_words= get_diff(a,b)
# big_words= get_diff(a,c)
# print("küçük harfler:", small_words)
# print("büyük harfler:", big_words)

# s = 'asd@gmail.com'
#
# print(s[s.find('@') + 1: s.find('.')] + '@' + s[0: s.find('@')] + '.com')
