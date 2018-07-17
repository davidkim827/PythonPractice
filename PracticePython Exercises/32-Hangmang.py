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

def displayFxn(letterGuessedRight):
    """This function updates and replaces the blank spaces of the word to display what letters have been guessed correctly and how many spaces are left"""
    for element in range(0, len(word)):                 # iterates through the element of the word to seek the position of the letter
        if word[element] == letterGuessedRight:
            displayList[element] = letterGuessedRight   # replaces the specific position of the blanks with the letter that was guessed correctly
            continue
        else:
            continue
    print(" ".join(displayList))                        # joins up the display list to form a cohesive print statement but instead replaced with letters if it was guessed correctly. Otherwise it will remain blank.
    print()
    
    
def checkComplete(letter):
    """This function serves the purpose of checking to make sure if the word has been guessed correctly in its entirety. """
    if len(lettersLeft) > 0:                #last letter that is guessed correctly should trigger the reversal of the guessed Correctly flag
        for element in lettersLeft:         #checks each letter in the list that contains the letters that haven't been matched correctly
            if letter == element:
                lettersLeft.remove(element) #removes the letter from the list of unique letters that haven't been matched completely
                if len(lettersLeft) == 0:   #checks to see if there are still any letters left in the list of unique letters that haven't been matched
                    return True             #if there aren't any letters left, it returns a True value that will then be used to complete the game
                else:
                    return False
            else:
                continue                    #continues loop over the list of letters that haven't been matched yet if the letter doesn't match
    else:
        return True
        
        
file = 'sowpods.txt'
createDict(file)
word = pickRandomWord()              #word to be used for guessing
lettersLeft = list(set(word))   #provides a unique list of letters of the word to be guessed
wordGuessedCorrectly = 0        #a boolean flag to see if word has been guessed correctly or not. 0 = false 1 = True
lettersGuessedCorrectly = []    #a data structure to hold the letters that have already been guessed correctly to provide a statement that says user has already guessed a specific letter

print("Welcome to Hangman! You have 6 tries to get the word before the man dies! \n")
displayList = "_ "*len(word)
print(displayList)
displayList = displayList.strip().split()

numberOfTries = 0
while wordGuessedCorrectly == 0:                    # loops until the user gets it right      
    
    letterGuess = input("Try #{}. \nGuess your letter: \n".format(numberOfTries+1))
    letterGuess = letterGuess.capitalize()          # makes sure all letters input are capitalized to handle any mismatches of capitalization issues
    letterFound = False                             # flag to make sure if a letter is found to be correct, it will go through checking completion of word and updating the display

    for letter in lettersLeft:                      # iterates through the letters left list to see if a letter has been matched and appends the letter to the letters guessed correctly list to handle any repeat letters
        if letter == letterGuess:
            letterFound = True
            lettersGuessedCorrectly.append(letterGuess)
            break
        else:
            continue
 
    if letterFound == True:                         # checking to see if the word is complete and display what has been changed
        numberOfTries += 1
        displayFxn(letterGuess)
        if checkComplete(letterGuess) == True:      # checks to see if the word has been guessed in its entirety which ends the entire while loop
            wordGuessedCorrectly = 1
        else:
            if numberOfTries > 5:
                break        
        
    else:                                           # determines which response to give based on a repeat letter or if the letter doesn't exist in the word     
        response = 0 
        for element in lettersGuessedCorrectly:     
            if element == letterGuess:
                print("You already guessed that. Try again!\n")
                response = 1                        # flips the flag to skip the wrong letter portion of the error checking
            else:
                continue
        
        if response == 0:                           # Because there hasn't been a repeat, should mean that the letter did not exist in the word and prints out an incorrect statement
            print("Incorrect!\n")
            numberOfTries += 1
            if numberOfTries > 5:
                break

if wordGuessedCorrectly == 1:
    print("Good job! You got the word!")
else:
    print("Sorry the man has been hanged.\n")
    print("The word was {}".format(word))

    

