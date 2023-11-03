import os
import io
import random

words = io.open("words.txt", mode="r", encoding="utf-8").read().split('\n')
words = [i for i in words if ' ' not in i and len(i) >= 5]
number = random.randrange(0, len(words))
word = words[number]

clear = lambda: os.system('cls')
clear()
s = "-" * len(word)
lives = 5
print(s)
while True:
    print('lives:', lives)
    guess = input("enter your letter:")
    clear()

    is_found = False
    for i in range(len(word)):
        if word[i] == guess:
            is_found = True
            c = guess
            s = s[:i] + c + s[i + 1:]

    if not is_found:
        lives -= 1
    if lives <= 0:
        print('game over!')
        print('word is:', word)
        break

    print(s)
    if s == word:
        print("congratulations!")
        break
