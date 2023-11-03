import random
import os
clear = lambda: os.system('cls')

number = random.randrange(0, 100)

while True:
    guess = int(input("enter your guess:"))
    clear()
    print(guess)
    if guess > number:
        print("lower")
    elif guess < number:
        print("upper")
    else:
        print("correct guess")
        break
