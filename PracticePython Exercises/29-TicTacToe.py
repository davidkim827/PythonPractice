#!/usr/bin/env python3

game = [[' ' for row in range(0,3)] for col in range(0,3)]     #list comprehension to make a 3x3 game board filled with blanks

def drawGameBoard(size): 
    """This function draws out a checkerboard and filled in with the values
    from the global game array that the game is actually played on"""
    
    print("    ---     ---     ---  \n")
    print(f" |   {game[0][0]}   |   {game[0][1]}   |   {game[0][2]}   |\n")
    print("    ---     ---     ---  \n")
    print(f" |   {game[1][0]}   |   {game[1][1]}   |   {game[1][2]}   |\n")
    print("    ---     ---     ---  \n")
    print(f" |   {game[2][0]}   |   {game[2][1]}   |   {game[2][2]}   |\n")
    print("    ---     ---     ---  \n")

def checkWinner(checkerBoard):
    """This function checks for the winner after every turn.
    Returns the values 0 and 1 for whether the player has won or not."""
    
    row = 1
    column = 1
    mid = checkerBoard[row][column]
    topMid = checkerBoard[row-1][column]
    botMid = checkerBoard[row+1][column]
    leftMid = checkerBoard[row][column-1]
    rightMid = checkerBoard[row][column+1]
    topRightCorner = checkerBoard[row-1][column+1]
    botLeftCorner = checkerBoard[row+1][column-1]
    botRightCorner = checkerBoard[row+1][column+1]
    topLeftCorner = checkerBoard[row-1][column-1]
    
    if mid == 'X' or mid == 'O':
        if topLeftCorner == mid and botRightCorner == mid:  #diagonal down top left to bot right
            print(f"{mid} is the winner")
            return 1
        elif botLeftCorner == mid and topRightCorner == mid:  #diagonal up bot left to top right
            print(f"{mid} is the winner")
            return 1
        elif leftMid == mid and rightMid == mid:   #horizontal mid
            print(f"{mid} is the winner")
            return 1
        elif topMid == mid and botMid == mid:   #vertical mid
            print(f"{mid} is the winner")
            return 1
    if (mid == ' ' and (rightMid != ' ' and topMid != ' ' and leftMid != ' ' and botMid != ' ')) or (mid == 'X' or mid == 'O'):
        if topLeftCorner == topMid and topRightCorner == topMid and topMid != ' ':   #horizontal top
            print(f"{topMid} is the winner")
            return 1
        elif topLeftCorner == leftMid and botLeftCorner == leftMid and leftMid != ' ':   #vertical left side
            print(f"{leftMid} is the winner")
            return 1
        elif topRightCorner == rightMid and botRightCorner == rightMid and rightMid != ' ':   #vertical right side
            print(f"{rightMid} is the winner")
            return 1
        elif botLeftCorner == botMid and botRightCorner == botMid and botMid != ' ':  #horizontal bot
            print(f"{botMid} is the winner")
            return 1
        else:
            return 0

def askMove(player):
    """This function asks the respective player to input their choice on the board.
    Then it marks the global game array which is then reflected in the drawGameBoard function."""
    
    boolean = False
    
    if player == 'X': 
        while boolean == False:    #continues to loop back to player1's turn if they hit an error in their input
            
            try:
                moveX = input("What is your move player 1? (row,col) \nNumbers 1-3 accepted. \n")
                moveX = moveX.strip().split(',')
                moveXrow = int(moveX[0])
                moveXcol = int(moveX[1])                
                
                while game[moveXrow-1][moveXcol-1] != ' ':    #checks to see if spot has already been filled
                    print("\nNot valid. There is already something there.\n")
                    moveX = input("What is your move player 1? (row,col) \nNumbers 1-3 accepted. \n")
                    moveX = moveX.strip().split(',')
                    moveXrow = int(moveX[0])
                    moveXcol = int(moveX[1])
                
                while moveXcol < 1 or moveXcol > 3 or moveXrow < 1 or moveXrow > 3:     #checks to see if the user input is valid for square locations
                    print("\nNot valid. Please try again.\n")
                    moveX = input("What is your move player 1? (row,col) \nNumbers 1-3 accepted. \n")
                    moveX = moveX.strip().split(',')
                    moveXrow = int(moveX[0])
                    moveXcol = int(moveX[1])
                
                game[moveXrow-1][moveXcol-1] = 'X'      #marks location with player1's symbol
                boolean = True                          #allows for the loop to end
            except:                                     #any other entries besides numbers will result in a recycle of the loop
                print("wtf")
    
    elif player == 'O':
        while boolean == False:                         #continues to loop back to player1's turn if they hit an error in their input
            
            try:
                moveO = input("What is your move player 2? (row,col) \nNumbers 1-3 accepted. \n")
                moveO = moveO.strip().split(',')
                moveOrow = int(moveO[0])
                moveOcol = int(moveO[1])
                
                while game[moveOrow-1][moveOcol-1] != ' ':    #checks to see if spot has already been filled
                    print("\nNot valid. There is already something there.\n")
                    moveO = input("What is your move player 2? (row,col) \nNumbers 1-3 accepted. \n")
                    moveO = moveO.strip().split(',')
                    moveOrow = int(moveO[0])
                    moveOcol = int(moveO[1])
                    
                while moveOcol < 1 or moveOcol > 3 or moveOrow < 1 or moveOrow > 3:     #checks to see if the user input is valid for square location
                    print("\nNot valid. Please try again.\n")
                    moveO = input("What is your move player 2? (row,col) \nNumbers 1-3 accepted. \n")
                    moveO = moveO.strip().split(',')
                    moveOrow = int(moveO[0])
                    moveOcol = int(moveO[1])
                    
                game[moveOrow-1][moveOcol-1] = 'O'
                boolean = True
  
            except:
                print("wtf")



drawGameBoard(3)  #draws the beginning game board
player1 = 'X'
player2 = 'O'

moveCounter = 0
while moveCounter < 9 and checkWinner(game) != 1:     #this loop is to keep the game going until all spaces are filled or until the winner is declared
    if moveCounter % 2 == 0:        #The first player will go
        askMove(player1)
        drawGameBoard(3)
    else:
        askMove(player2)            #The second player will go
        drawGameBoard(3)
    moveCounter+=1                  #increments the move counter to determine how many moves are left
if moveCounter == 9:                #to determine if the board is full. If it is then it should be a draw.
    print("Board is now full. It was a draw. The game is now complete.  Thank you for playing.")
else:
    print("Game is now complete. Thank you for playing.")
