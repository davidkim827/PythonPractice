#!/usr/bin/env python3

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = list()
for i in b:
    for j in a:
        if i == j:
            for v in c:
                if v == i:
                    c.remove(v)
            c.append(i)
print(c)

#extra step 1

randList1 = list()
randList2 = list()

for i in range(0,5000):
    randList1.append(random.randint(0,100))
    randList2.append(random.randint(0,100))
d = list()
for i in randList1:
    for j in randList2:
        if i == j:
            for v in d:
                if v == i:
                    d.remove(v)
            d.append(i)
print(d)