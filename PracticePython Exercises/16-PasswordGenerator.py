#!/usr/bin/env python3

import random

def passwordGenerator():
    a = []
    for i in range(0,20):
        a.append(chr(random.randint(32,126)))
    
    a = "".join(a)
    print(a)

passwordGenerator()

