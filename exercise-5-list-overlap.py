'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]'''

import random

one = []
two =[]

for i in range(1, 11):
    one.append(random.randint(1,10))
    two.append(random.randint(1,10))

new = []

for i in one:
    if i in two:
        new.append(i)

print(one)
print(two)
print(new)
        
