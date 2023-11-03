# equation = input("enter an equation")
# a = int(equation[0])
# b = (equation[4])
# c = (equation[7])
#
# second_coefficient = int(equation[3]+b)
# third_coefficient = int(equation[6]+c)
# import math
#
# delta = second_coefficient ** 2 - 4 * a * third_coefficient
# delta_sqrt = math.sqrt(delta)
# x1 = (-second_coefficient + delta_sqrt) / (2 * a)
# x2 = (-second_coefficient - delta_sqrt) / (2 * a)
#
# print(x1, x2)

# -4x2-2x-8

equation = input("enter an equation")

i_ = len(equation) == 9
print(i_)
print(equation[0 + i_])
a = (equation[0 + i_])
b = (equation[4 + i_])
c = (equation[7 + i_])

first_coefficient =  int(a)
second_coefficient = int(equation[3 + i_]+b)
third_coefficient = int(equation[6 + i_]+c)
import math

delta = second_coefficient ** 2 - 4 * a * third_coefficient
delta_sqrt = math.sqrt(delta)
x1 = (-second_coefficient + delta_sqrt) / (2 * a)
x2 = (-second_coefficient - delta_sqrt) / (2 * a)

print(x1, x2)


s = "harun"
print(s[0])







