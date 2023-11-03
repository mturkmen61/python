# a="merhaba"
# b="merhaba"
# print(a is b)
# # id a eşittir id b
# print(id(a),id(b))
# print(id(a)==id(b))

a=5.1
print(type(a) is float)

a="P"
a+="ython"
b="Python"
print("a değeri",a,"id değeri",id(a))
print("b değeri",b,"id değeri",id(b))
print("aynı mı?",a is b)

d=5
f=6
print(d is not f)