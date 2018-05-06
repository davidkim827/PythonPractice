#!/usr/bin/env python3

import random

def elementSearch(listInput, number):
    
    for i in listInput:
        if i == number:
            return True
    
    return False

def bSearchElement(listInput, number):

    L = 0
    R = len(listInput)
    

    while True:
        mid = (L + R) // 2
        if number > len(listInput) or number < listInput[0] or mid < 0:
            return False
        if listInput[mid] < number:
            L = mid + 1
        elif listInput[mid] > number:
            R = mid - 1
        elif listInput[mid] == number:
            return True
    return False

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,]

print(elementSearch(a, 52))
print(bSearchElement(a, 51))
print(bSearchElement(a, 49))
print(bSearchElement(a, 1))
print(bSearchElement(a, 25))
print(bSearchElement(a, 0))
print(bSearchElement(a, 101))

# random numbers populating a list to bsearch
b = [random.randint(0,10000) for i in range(0,100)]
b.sort()
print(b)
print(bSearchElement(b, 800))