import decimal
import locale
locale.setlocale(locale.LC_ALL,"tr")

a=decimal.Decimal("15000000.15")
print("a değişkeninin tipi",type(a),"değeri",a)
print(locale.format_string("%.2f",a,grouping=True))