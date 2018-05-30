#!/usr/bin/env python3

size = int(input("What size N of a N x N board would you like me to draw? \n"))
print()

for x in range(0, size):
    for dashes in range(0, size):
        print("  ---  ", end = "")
    print()
    for columns in range(0, size):
        print("|      ", end = "")
    print("|")
for dashes in range(0,size):
    print("  ---  ", end = "")
