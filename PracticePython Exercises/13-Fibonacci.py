#!/usr/bin/env python3

def fibonacci(number):
    fibList = [1,1]
    if number == 0 or number < 0:
        print( "Not Valid." )
    elif number == 1:
        print ([fibList[0]])
    else:
        for i in fibList:
            if len(fibList) < a:
                i = fibList[-1] + fibList[-2]
                fibList.append(i)
        print(fibList)
        

a = int(input("How many fibonacci numbers should I generate?: "))
fibonacci(a)