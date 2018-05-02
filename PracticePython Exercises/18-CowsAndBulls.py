#!/usr/bin/env python3

import random
def cowsAndBulls(number):
    r = random.randint(1000,9999)
    print(r)
    cows = 0
    for i in str(r):
        for j in str(number):
            if i == j:
                cows+=1
    
    bulls = 4 - cows
    print(f"{cows} cows, {bulls} bulls")


cowsAndBulls(1234)