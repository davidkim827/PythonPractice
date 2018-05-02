#!/usr/bin/env python3

userNumber = int(input("Please type in a number: "))

if userNumber % 4 == 0:
    print("This is divisible by 4.")
elif userNumber % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

num = int(input("Please type in two numbers to check if the first number divides evenly into the second: "))
check = int(input())

if num % check == 0:
    print("The two numbers divide evenly into each other.")
else:
    print("The two number do not divide evenly into each other.")