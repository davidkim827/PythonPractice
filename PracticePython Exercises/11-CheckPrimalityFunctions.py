#!/usr/bin/env python3

def isPrime(integer):
    prime = True

    for i in range(2, integer):
        if integer % i == 0:
            prime = False
            break
        else:
            continue
    if prime == True:
        return True
    else:
        return False
    
    

a = int(input("Let's determine whether your input is prime or not: "))

print(isPrime(a))

