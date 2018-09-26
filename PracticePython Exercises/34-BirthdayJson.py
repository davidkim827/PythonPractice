#!/usr/bin/env python3

import json, os

realPath = os.path.realpath("famousPeopleBirthday.json")

with open(realPath, 'r') as f:
    info = json.load(f)

def addPeopleToJSON():
    scientistAddToDict = str(input("Please input a scientist's first and last name to add to the dictionary: \n")).title()
    scientistBirthday = str(input("Please input the scientist's birthday to add to the dictionary in this format MM/DD/YYYY: \n"))
    
    mustBe10chars = len(scientistBirthday)
    while mustBe10chars != 10:
        print("You input the scientist's birthday in the wrong format. Please follow the formatting guidelines.")
        scientistBirthday = str(input("Please input the scientist's birthday to add to the dictionary in this format MM/DD/YYYY: \n"))
        mustBe10chars = len(scientistBirthday)
    
    info[scientistAddToDict] = scientistBirthday
    with open(realPath, 'w') as f:           #dumps json object back to file
        json.dump(info, f)
    print(f"{scientistAddToDict} has been added.\n")

keepAdding = str(input("Would you like to add a person to the birthday JSON? Y or N\n"))

while keepAdding.capitalize() == "Y":
    addPeopleToJSON()
    keepAdding = str(input("Would you like to add another person? Y or N\n"))

print(info)