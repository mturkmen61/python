a = 1
b = 1
print(a == b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
# print(a !=b)  a b'ye eşit değildir'

import math

a=5.0
b=4.99998
print(math.isclose(a,b,abs_tol=0.0001))
