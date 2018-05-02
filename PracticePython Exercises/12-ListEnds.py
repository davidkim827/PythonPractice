#!/usr/bin/env python3

def listEnds(numList):
    return [numList[0], numList[(len(numList)-1)]]

a = [5, 10, 15, 20, 25]
print(listEnds(a))
