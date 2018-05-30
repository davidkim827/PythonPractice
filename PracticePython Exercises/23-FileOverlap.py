#!/usr/bin/env python3

with open("23-happynumbers.txt", "r") as file1:
    happyList = file1.read().split('\n')
    
file1.close()

with open("23-primenumbers.txt", "r") as file2:
    primeNumList = file2.read().split('\n')
    
file2.close()

coincidingList = [i for i in happyList if i in primeNumList]
        
print(coincidingList)