#!/usr/bin/env python3

names = dict()

with open("22-namesList.txt", 'r') as openFile:
    text = openFile.read().splitlines()
    for i in text:
        if i in names.keys():
            names[i] += 1
        elif i not in names.keys():
            names[i] = 1
openFile.close()

for k in names:
    print("{} : {}".format(k, names[k]))
    
print()

# extra set 1

print()

categoryDict = {}
with open('22-Training_01.txt', 'r') as f:
    for i in f:
        line = i.split("/")
        category = line[2]
        if category not in categoryDict.keys():
            categoryDict[category] = 1
        else:
            categoryDict[category] += 1
        
for i in categoryDict:
    print(f"{i}: {categoryDict[i]}")