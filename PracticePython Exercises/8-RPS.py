#!/usr/bin/env python3

import random

print("Welcome to Rock Paper Scissors. You will be playing against a computer!\n")

while True:
    a = input("Rock, Paper, Scissors: ")
    a = a.lower()
    b = random.randint(0,2)
    
    if b == 0:
        b = "rock"
        print(b)
        print()
    elif b == 1:
        b = "paper"
        print(b)
        print()
    else:
        b = "scissors"
        print(b)
        print()
    
    if a == b:
        print("It's a tie!\n")
    elif (a == "rock" and b == "paper") or (a == "paper" and b == "scissors") or (a == "scissors" and b == "rock"):
        print("You Lose\n")
    elif (b == "rock" and a == "paper") or (b == "paper" and a == "scissors") or (b == "scissors" and a == "rock"):
        print("You Win\n")
    
    
    c = input("Play again? Yes or No: ")
    
    if c.lower() == "yes":
        continue
    elif c.lower() == "no":
        break
    else:
        print("Sorry, Not a valid input. Let's play again. \n")