#!/usr/bin/env python3

def drawGameBoard(size):
    
    for x in range(0, size):
        for dashes in range(0, size):
            print("  ---  ", end = "")
        print()
        for columns in range(0, size):
            print("|      ", end = "")
        print("|")
    for dashes in range(0,size):
        print("  ---  ", end = "")
