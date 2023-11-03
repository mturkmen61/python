grade = int(input("enter a grade"))
if grade > 100 or grade < 0:
    print("enter a valid grade")
elif grade > 80:
    print("A")
elif grade > 60:
    print("B")
elif grade > 50:
    print("C")
elif grade > 45:
    print("D")
elif grade > 25:
    print("E")
else:
    print("F")
