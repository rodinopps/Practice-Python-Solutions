import random
number = random.randint(1,9)
turn = 0
while True:
    guess = input("Enter a guess: ")
    if str(guess) == "exit":
        break
    elif int(guess) > number:
        print("Too high. ")
        turn += 1
    elif int(guess) < number:
        print("Too low. ")
        turn += 1
    else:
        print("Exactly right. ")
        print(turn)
        
