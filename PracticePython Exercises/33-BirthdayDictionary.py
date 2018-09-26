#!/usr/bin/env python3

famousPeopleBirthdayDict = {"Elon Musk" : "6/28/1971",
                            "Jeff Bezos" : "1/12/1964",
                            "Bill Gates" : "10/28/1955",
                            "Nikola Tesla" : "7/10/1856",
                            "Sundar Pichai" : "7/12/1972"}

print("Welcome to the birthday dictionary. We know the birhtdays of: ")
for element in famousPeopleBirthdayDict.keys():
    print(element)

personFound = 0
while personFound == 0:

    birthdayPerson = str(input("\nWhose birthday do you want to look up?\n"))
    birthdayPerson = birthdayPerson.title()

    try:
        print("\n{}'s birthday is {}.".format(birthdayPerson, famousPeopleBirthdayDict[birthdayPerson]))
        personFound = 1
    except:
        print("That person doesn't exist or maybe you spelled it wrong. Please try again.")