number = int(input("Enter a number: "))
list = []
for i in range(1, number + 1):
    if number % (i) == 0:
        list.append(i)
print(list)
