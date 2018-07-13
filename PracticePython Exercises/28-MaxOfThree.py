#!/usr/bin/env python3

def maxNum(val1, val2, val3):
        
    tmp = -1000000
    if val1 > tmp:
        tmp = val1
    if val2 > tmp:
        tmp = val2
    if val3 > tmp:
        tmp = val3
    
    return tmp

print(maxNum(5000,5001,-49999))