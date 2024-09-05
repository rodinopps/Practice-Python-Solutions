number = int(input("Enter a number: "))
check = int(input("Enter another number: "))

if number % 2 and number % 4== 0:
    print("FOUR FOUR FOUR FOUR")
elif number % check == 0:
    print("TADA!")
elif number % 2 == 0:
    print("EVEN")
else:
    print("ODD")
