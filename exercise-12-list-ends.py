list = []
while True:
    num = input("Enter a number. Enter n if you want to finish: ")
    if num == "n":
        if len(list) <= 2:
            print(list)
        elif len(list) > 2:
            print([list[0], list[-1]])
        break
    else:
        list.append(num)
