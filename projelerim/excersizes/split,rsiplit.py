# split metinleri ayırır
a="bugün -hava çok -güzel-anne"
b=a.split()
c=a.rsplit("-")
d=a.split("-",2)
print(b,c,d)
hikaye="""yağmurlu bir günde
camdan süzülen damlaları izlerken
yudumladığım espresso 
çatlak bardaktan sızmıştı
"""

print(hikaye.splitlines())
print(hikaye.split("\n"))