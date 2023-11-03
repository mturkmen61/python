for s in range(10):
    print(s+1)
    if s == 3:
        break
    print("Döngü devam ediyor")
print("program sonu")

s = 0

while s < 10:
    s += 1
    print(s)
    if s == 3:
        break
    print("döngü devam ediyor")

# print("Program sonu")

for s in range(5):
    if s == 3:
        continue
    print(s)

s = 0
while s < 5:
    s += 1
    if s == 3:
        continue
    print(s)
