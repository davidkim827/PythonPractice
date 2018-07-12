#!/usr/bin/env python3

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]


def askMove(player):
    boolean = False
    
    if player == 'X': 
        while boolean == False:    #continues to loop back to player1's turn if they hit an error in their input
            
            try:
                moveXrow = int(input("What is your move player 1? (row ENTER col ENTER) \nNumbers 1-3 accepted. \n"))
                moveXcol = int(input())
                
                while game[moveXrow-1][moveXcol-1] != 0:    #checks to see if spot has already been filled
                    print("Not valid. There is already something there.")
                    moveXrow = int(input("What is your move player 1? (row ENTER col ENTER) \nNumbers 1-3 accepted. \n"))
                    moveXcol = int(input())

                while moveXcol < 1 or moveXcol > 3 or moveXrow < 1 or moveXrow > 3:     #checks to see if the user input is valid for square locations
                    print("Not valid. Please try again.")
                    moveXrow = int(input("What is your move player 1? (row ENTER col ENTER) \nNumbers 1-3 accepted. \n"))
                    moveXcol = int(input())
                game[moveXrow-1][moveXcol-1] = 'X'      #marks location with player1's symbol
                boolean = True                          #allows for the loop to end
            except:                                     #any other entries besides numbers will result in a recycle of the loop
                print("wtf")
    
    elif player == 'O':
        while boolean == False:                         #continues to loop back to player1's turn if they hit an error in their input
            
            try:
                moveOrow = int(input("What is your move player 2? (row ENTER col ENTER) \nNumbers 1-3 accepted.\n"))
                moveOcol = int(input())
                
                while game[moveOrow-1][moveOcol-1] != 0:    #checks to see if spot has already been filled
                    print("Not valid. There is already something there.")
                    moveOrow = int(input("What is your move player 2? (row ENTER col ENTER) \nNumbers 1-3 accepted. \n"))
                    moveOcol = int(input())

                while moveOcol < 1 or moveOcol > 3 or moveOrow < 1 or moveOrow > 3:     #checks to see if the user input is valid for square location
                    print("Not valid. Please try again.")
                    moveOrow = int(input("What is your move player 2? (row ENTER col ENTER) \nNumbers 1-3 accepted. \n"))
                    moveOcol = int(input())
                    
                game[moveOrow-1][moveOcol-1] = 'O'
                boolean = True
  
            except:
                print("wtf")

player1 = 'X'
player2 = 'O'

moveCounter = 0
while moveCounter < 9:
    if moveCounter % 2 == 0:
        askMove(player1)
        print(game)
    else:
        askMove(player2)
        print(game)
    moveCounter+=1
print("Board is now full. The game is now complete.")
