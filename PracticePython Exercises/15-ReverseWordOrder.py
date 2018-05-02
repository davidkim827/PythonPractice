#!/usr/bin/env python3

def reverseWordOrder(string):
    a = string.split(" ")
    a = a[::-1]
    print(" ".join(a))
    
a = input("Type in a phrase you would like for me to reverse: ")
reverseWordOrder(a)