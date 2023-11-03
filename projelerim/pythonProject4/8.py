classes_held = int(input("enter number of classes held"))
classes_attented = int(input("enter number of classes attented "))
if classes_attented > classes_held:
    print("enter a valid number")
if classes_attented <= classes_held:
    print("percantage", "%", classes_attented / classes_held * 100)
elif classes_attented / classes_held * 100 > 75 and classes_attented < classes_held:
    print("student is allowed to sit in exam")
elif classes_attented / classes_held * 100 < 75 and classes_attented < classes_held:
    print("student is not allowed to sit in exam")
