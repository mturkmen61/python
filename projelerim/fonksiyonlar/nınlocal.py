def must():
    def harun():
        global number
        number = 5
        print("harun in", number)

    number = 10
    print("must in", number)
    harun()
    print("must out", number)


number = 20
print("ana kapsam", number)
must()
print("ana kapsam", number)


def must():
    def harun():
        nonlocal number
        number = 5
        print("harun in", number)

    number = 10
    print("must in", number)
    harun()
    print("must out", number)


number = 20
print("ana kapsam", number)
must()
print("ana kapsam", number)
