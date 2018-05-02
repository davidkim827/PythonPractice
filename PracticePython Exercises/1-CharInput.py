#!/usr/bin/env python3

import time, datetime

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
now = datetime.datetime.now()

addToYear = 100-age
print("Hello, {}. You will turn 100 in the year {}".format(name, (now.year+addToYear)))

numTimesMessage = int(input("Input a number to repeat the message that number of times: "))

for i in range(0, numTimesMessage+1):
    print("Hello, {}. You will turn 100 in the year {}".format(name, (now.year+addToYear)))