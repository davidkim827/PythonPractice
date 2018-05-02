#!/usr/bin/env python3

a = int(input("Please input a number and I will tell you all the divisors of that number: "))
b = range(1, a)

print([i for i in b if a%i==0])