   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.

import random, os


   # The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York':'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}




# Generate 35 quiz files.
def create_quiz(capitalsDict):
    """This function will take a dictionary as an input. The function will first take a look to see if there is already a folder that exists
    with the same name as the variable quizFolderName that the user had input their quiz folder name into. If there already exists a folder with
    the same name, then the program quits after writing that the user should create a new directory name.
    
    If the folder name is unique, then it goes through the algorithm to create a randomized quiz with the correlating answers in separate text files
    for each student that the user says there is. The user also can vary the number of questions that the quizzes will have and does not have to strictly
    be the entire length of the dictionary."""
    
    #prompts the user to name the folder that they will create their quizzes in   
    quizFolderName = str(input("What is your quiz folder going to be called?: "))
    
    #prompts the user to write down the number of questions they want on their quiz but has to be less than the size of the dictionary
    quizQuestionNumbers = int(input("How many questions do you want on your quiz?: "))
    while quizQuestionNumbers > len(capitals) or quizQuestionNumbers <= 0:
        quizQuestionNumbers = int(input("Not valid. How many questions do you want on your quiz?: "))
    
    #number of quizzes to make
    numberOfStudents = int(input("How many quizzes should this program make?: "))
    
    #directory verification
    try:
        if os.path.exists('{}\{}'.format(os.getcwd(), quizFolderName)) == False:
            os.makedirs(f".\{quizFolderName}")
            os.chdir(f'.\{quizFolderName}')
        else:
            print("make a new folder")
            quit()
    except Exception as e:
        print(f"wut is going on {e}")
    
    #quizmaking algorithm
    for quizNum in range(numberOfStudents):
        print("hello")      #to make sure that the creation is not working to prevent any overwrites for previous quiz creations
       
       # Creates the quiz and answer key files.
        try:
            fileQuiz = open('quiz%d' % (quizNum + 1), 'w')
            fileAnswers = open('answers%d' % (quizNum + 1), 'w')
        except Exception as e:
            print("You're wrong. this is the exception {}".format(e))

       # Writes out the header for the quiz.
        fileQuiz.write("Name: \nDate: \nClass: \n\n%s" % "States/Capitals Quiz Form {}\n\n".format(quizNum + 1))
        fileAnswers.write("Answers\n")
       # Shuffles the order of the states.
        states = list(capitalsDict.keys())
        random.shuffle(states)
        
       # Loops through number of questions that user wanted to create quiz for and creates that many questions.
        try:
           for qitem in range(quizQuestionNumbers):
                fileQuiz.write("{}. The capital of {} is: \n".format(qitem + 1, states[qitem]))
                try:
                    for a in capitalsDict:
                        if a == states[qitem]:
                            rightAnswer = capitalsDict.get(a)
                            break
                    fileAnswers.write("\n\t{}. {}".format(qitem + 1, rightAnswer))
                except Exception as ex:
                    print("You're wrong. this is the exception {}".format(ex))
        except Exception as e:
            print("You're wrong. this is the exception {}".format(e))
        fileQuiz.close()
        fileAnswers.close()
    print("Finished successfully")
    
create_quiz(capitals)