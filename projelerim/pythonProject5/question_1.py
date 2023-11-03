word = "araba"
while True:
    guess = input("enter your letter:")
    for i in word:
        a = list(i)
        if i == guess:
            print(a, end=" ")
        else:
            print(" ", end=" ")


