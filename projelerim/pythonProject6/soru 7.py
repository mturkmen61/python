def swap_case(s):
    for i in s:
        if i.isupper() == True:
            i = i.lower()

        else:
            i = i.upper()

     



s = "MNjnqd GD KHHhdg"
result = swap_case(s)
print(result)
