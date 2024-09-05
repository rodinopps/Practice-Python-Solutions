'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list = []
for i in a:
    if i < 5:
        list.append(i)
print(list)'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

number = int(input("Enter a number: "))

list = []
for i in a:
    if i < number:
        list.append(i)
print(list)
