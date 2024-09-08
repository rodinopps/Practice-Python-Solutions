import random
length1 = random.randint(5, 15)
length2 = random.randint(5,15)
list1 = []
list2 = []

for i in range(length1):
    str(list1.append(random.randint(1, 100)))

for i in range(length2):
    str(list2.append(random.randint(1, 100)))

total = []
for i in list1:
    if i in list2:
        total.append(i)

print(total)
print()
print(list1)
print()
print(list2)
