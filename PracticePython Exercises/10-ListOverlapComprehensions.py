#!/usr/bin/env python3

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [i for i in set(b) for j in set(a) if i == j]

print(c)

#extra set 1

d = []
e = []
for i in range(0,50):
    d.append(random.randint(0,100))
    e.append(random.randint(0,100))

f = [i for i in set(d) for j in set(e) if i == j]
f.sort()
print(f)

