def must():
    def harun():
        number = 20
        print("harun begin", number)
        print("harun finish", number)

    print("must begin", number)
    harun()
    print("must finish", number)


number = 10
print("before must", number)
must()
print("after must", number)
