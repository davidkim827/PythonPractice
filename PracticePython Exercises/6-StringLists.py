#!/usr/bin/env python3
import copy

palindromeInput = str(input("Please type in a word to see if it is a palindrome: "))

a = list(palindromeInput.lower())
print(a)
b = copy.copy(a)
b.reverse()
print(b)
if a == b:
    print("This is a palindrome!")
else:
    print("Sorry not a palindrome.")