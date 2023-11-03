age1 = int(input("enter age one"))
age2 = int(input("enter age two"))
age3 = int(input("enter age three"))

if age1 > age2 > age3:
    print("greatest age is first one")
    print("youngest age is third one")
elif age1 > age3 > age2:
    print("greatest age is first one")
    print("youngest age is second one")
elif age2 > age1 > age3:
    print("greatest age is second one")
    print("youngest age is third one")
elif age2 > age3 > age1:
    print("greatest age is second one ")
    print("youngest age is first one ")
elif age3 > age1 > age2:
    print("greatest age is third one")
    print("youngest age is second one")
elif age3 > age2 > age1:
    print("greatest age is third one")
    print("youngest age is first one")
