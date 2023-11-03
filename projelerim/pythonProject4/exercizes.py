# 1
year = int(input("Enter year number"))
salary = int(input("enter salary amount"))

if year > 5:
    print(int(salary * 5 / 100))
else:
    print("no bonus")

# 2
length = int(input("enter lenghth of rectangle"))
breadth = int(input("enter breadth of rectangle"))
if length == breadth:
    print("it is a square")
else:
    print("it is not a square")

# 3
n1 = int(input("enter number one"))
n2 = int(input("enter number two"))
if n1 > n2:
    print("first number greater than second number")
elif n2 > n1:
    print("second number is greater than first number")
else:
    print("numbers are equal")

# 4
quantity = int(input("enter quantity"))
if quantity > 1000:
    print(str(quantity * 90) + " dollar")
else:
    print("there is a no discount")

# 5
grade = int(input("enter a grade"))
if grade>80:
    print("A")
elif grade>60:
    print("B")
elif grade>50:
    print("C")
elif grade>45:
    print("D")
elif grade>25:
    print("E")
elif grade>25
    print("F")
