number = int(input("Enter a number: "))

if number < 2:
    print("Not a prime number")
else:
    prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("Not a prime number")
            prime = False
            break
    if prime:
        print("Prime number")
