#!/usr/bin/env python3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = list()
for i in a:
    if i < 5:
        c.append(i)
print(c)

#extra step 1

print([i for i in a if i < 5])

#extra step 2

b = int(input("Tell me a number and I will return a list of numbers from a that contain all numbers less than your number: "))
print([i for i in a if i < b])