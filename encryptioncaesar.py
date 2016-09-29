exitTicket = False
while not exitTicket:
    original = input("Enter a string to encrypt").upper()
    rotation = int(input("How many to shift by ==>"))

    encrypted = ""
    for i in original:
        value = ord(i) - 65
        value = value + rotation
        value = value % 26
        encrypted += chr(value + 65)

    print(encrypted)