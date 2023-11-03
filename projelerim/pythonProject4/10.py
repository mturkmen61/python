email = input("enter your email")

# 1. includes both @ and . (and 1 occurrence) 2. @ should precede ., and at least 1 character should be between them
# and @ should not be first char and . should not be last char

rule_1 = email.count('.') == 1 and email.count('@') == 1

if rule_1:
    rule_2 = email.index('@') + 1 < email.index('.') and email[0] != '@' and email[-1] != '.'
    if rule_2:
        print('valid')
else:
    print("not valid")
