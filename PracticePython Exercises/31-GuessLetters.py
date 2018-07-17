#!/usr/bin/env python3
word = "EVAPORATE"
lettersLeft = list(set(word))
wordGuessedCorrectly = 0
lettersGuessedCorrectly = []

def displayFxn(letterGuessedRight):
    for element in range(0, len(word)):
        if word[element] == letterGuessedRight:
            displayList[element] = letterGuessedRight
            continue
        else:
            continue
    print(" ".join(displayList))
    print()
    
    
def checkComplete(letter):
    if len(lettersLeft) > 0:        #last letter that is guessed correctly should trigger the reversal of the guessed Correctly flag
        for element in lettersLeft:
            if letter == element:
                lettersLeft.remove(element)
                if len(lettersLeft) == 0:
                    return True
                else:
                    return False
            else:
                continue
    else:
        return True
        
        
print("Welcome to Hangman!")
displayList = "_ "*len(word)
print(displayList)
displayList = displayList.strip().split()

while wordGuessedCorrectly == 0:
    letterGuess = input("Guess your letter: ")
    letterGuess = letterGuess.capitalize()
    letterFound = False
    for letter in lettersLeft:
        if letter == letterGuess:
            letterFound = True
            lettersGuessedCorrectly.append(letterGuess)
            break
        else:
            continue
    if letterFound == True:
        displayFxn(letterGuess)
        if checkComplete(letterGuess) == True:
            wordGuessedCorrectly = 1
        else:
            continue
    else:
        response = 0
        for element in lettersGuessedCorrectly:
            if element == letterGuess:
                print("You already guessed that. Try again!\n")
                response = 1
            else:
                continue
        if response == 0:
            print("Incorrect!\n")
        else:
            continue
    
    
print("Good job! You got the word!")

    