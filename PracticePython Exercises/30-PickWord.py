#!/usr/bin/env python3

import random

dictList = []

def createDict(file):
    try:    
        with open(file, 'r') as dictFile:
            line = dictFile.readline().strip()      #strips new line char
            dictList.append(line)                   #adds the first line to the dictList
            while line:                             #grabs each line until the end of the file and adds it to the dictList
                line = dictFile.readline().strip()  
                dictList.append(line)
    except IOError as e:                #handles exception for file
        print(e)

def pickRandomWord():
    r = random.randint(0, len(dictList)-1)          #chooses a random number between 0 and the 1 less from the size of the dictList to be able to access the element from the dictList
    return(dictList[r])
    
file = 'sowpods.txt'
createDict(file)
print(pickRandomWord())
