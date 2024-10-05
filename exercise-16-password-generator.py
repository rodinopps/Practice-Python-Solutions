import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "!@€£#$%^&*()-_=+[{]};:'\"|,<.>/?`~"


while True:
    enter = input("Weak or Strong? ")
    if enter.lower() == "weak":
        length = random.randint(4, 8)
        characters = lowercase + digits
        print("".join(random.choice(characters) for i in range(length)))
        print()
        
    elif enter.lower() == "strong":
        length = random.randint(12, 20)
        characters = lowercase + uppercase + digits + special
        print("".join(random.choice(characters) for i in range(length)))
        print()
        
    else:
        print("Pick a valid option: ")
