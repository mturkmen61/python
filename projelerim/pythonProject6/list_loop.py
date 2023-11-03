a = [10, 20, 30, 40, 50, 10]
b = ["b"]

for i in a:
    if i not in b:
        b.append(i)
print(b)

a = [3,4,5,6,7,8,9 ]

last_number = a[len(a) - 1]
a[len(a)-1] = a[0]
a[0] = last_number

print(a)



a = [1, 2, 3, 4, 5, 6, 7]
pos1 = 4
pos2 = 3

# tek değişkenli

b = a[pos2]
a[pos2] = a[pos1]
a[pos1] = b



print(a)







a = [1, 2, 3, 4, 5, 6, 7]
s = 0
for i in a:
    s += 1
print(s)



a = [1, 2, 3, 4, 5, 6, 7]
input = 7
for i in a:
    if i == input:
        print("True")
        break



a = [1, 2, 3, 4, 5, 6, 7]
a.reverse()
print(a)


a = [1, 2, 3, 3, 4, 5, 6, 7]
number = 3
a.count(3)



a = [1, 2, 3, 4, 5, 6, 7]
s = 0
for i in a:
    s += i
print("sum =",s)
print("average =",s/len(a) )



a = [3, 6, 3, 2, 5, 6, 2]

a.sort()
print(a[0])




a = [1, 2, 3, 4, 5, 6, 7]

a.sort()
print(a[len(a)-1])



a = [1, 1, 3, 4, 4, 7, 7, 7]
b = a[len(a) - 1]
a.sort()
for i in range( b,0,-1 ):
    if i != b:
        print(i)
        break

