#!/usr/bin/env python3

import random

def sortedNewSetList(listInput):
    newList = []
    for i in listInput:
        if i not in newList:
            newList.append(i)
    newList.sort()
    return newList

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(sortedNewSetList(a))

b = [random.randint(0,25) for i in range(0, 50)]
print(sortedNewSetList(b))
b = list(set(b))
print(b)
