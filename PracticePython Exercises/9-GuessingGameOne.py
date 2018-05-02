#!/usr/bin/env python3

import random

while True:
    a = random.randint(1,9)
    print(a)

    b = int(input("Please guess what number is in the bag: "))
    
    if b == a:
        print("Good job! You guessed right.")
    else:
        print("Wrong.")
    
    c = input("Type exit if you want to leave. Otherwise type in anything else: ")
    
    if c.lower() == "exit":
        break
    else:
        continue
    
    