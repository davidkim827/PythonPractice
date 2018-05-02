#!/usr/bin/env python3
# This project was an idea I came up with while seeing how fast I can type so that I can see my speed without having to go online to check.

import shelve, time, random, logging, os

logging.basicConfig(level = logging.DEBUG, format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-8s]  %(message)s",
    handlers=[
        logging.FileHandler("{0}/{1}.log".format(os.getcwd(), os.path.basename(__file__))),
        logging.StreamHandler()# This project was an idea I came up with while seeing how fast I can type so that I can see my speed without having to go online to check.

        ])

class WPM(object):
    def randomString():
        """ returns a string that correlates to a random number that is a key for the dictionary inside the shelf"""
        r = random.randint(1, 10)
        if r == 1:
            return 's1'
        elif r == 2:
            return 's2'
        elif r == 3:
            return 's3'
        elif r == 4:
            return 's4'
        elif r == 5:
            return 's5'
        elif r == 6:
            return 's6'
        elif r == 7:
            return 's7'
        elif r == 8:
            return 's8'
        elif r == 9:
            return 's9'
        elif r == 10:
            return '10'
        
    def countWords(string):
        """counts the number of words so that it can be calculated later as WPM"""
        countWords = 0
        for a in string.split():
            countWords += 1
        return countWords
    
    def WPMcalculator(wordcount, time):
        return wordcount / (time/60)
    
    def mistakes(textString, userString):
        """Compares the user input to what the string was actually supposed to be, counts the number of mistakes user made, and returns the number"""
        a = list(textString)
        b = list(userString)
        numCharOriginalStr = len(a) - 1 #for the extra space at the end of the original string 
        numCharUserCorrect = [i for i, j in zip(a,b) if i == j]
        return (numCharOriginalStr - len(numCharUserCorrect))
    
    #opens the shelf to retrieve 'setOne'
    shelfFile = shelve.open('randomTextTypingTestShelf')
    logging.info("opened shelf")
    
    #retrieves the random dictionary value in a single string for the user to read as they type
    stringToType = "".join(list(shelfFile['setOne'][randomString()]))
    logging.info("Number of words in text is: {}".format(countWords(stringToType)))
    
    #The user is prompted to press the Enter key when ready
    input("Welcome to the typing test!\n\nWhen you're ready to type, please press the 'Enter' key'\n")
    logging.info("Starting Timer")
    
    #Starts the timer and user is allowed to start typing as they read. When done, user is prompted to press the Enter key once more.
    startTime = time.time()
    print(stringToType)
    print("\n When you're all done, please press the 'Enter' key to calculate your WPM\n")
    
    logging.info("User is now typing..")
    
    #Logs the time that the user stopped the typing test
    userInput = input()
    endTime = time.time()
    logging.info("Time taken was: {} seconds".format(endTime-startTime))
    
    #Prints out the user's WPM
    print("Congratulations your WPM is: {:.2f}".format(WPMcalculator(countWords(stringToType), (endTime - startTime))))
    print("You made {} mistakes in your input.".format(mistakes(stringToType, userInput)))
    logging.info("Program terminated")
