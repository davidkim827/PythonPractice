#!/usr/bin/env python3

#0 = empty space
#1 = player 1 moved
#2 = player 2 moved
def checkWinner(checkerBoard):
    
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
    
    if mid > 0:
        if topLeftCorner == mid and botRightCorner == mid:  #diagonal down top left to bot right
            print(f"{mid} is the winner")
            return
        elif botLeftCorner == mid and topRightCorner == mid:  #diagonal up bot left to top right
            print(f"{mid} is the winner")
            return
        elif leftMid == mid and rightMid == mid:   #horizontal mid
            print(f"{mid} is the winner")
            return
        elif topMid == mid and botMid == mid:   #vertical mid
            print(f"{mid} is the winner")
            return
    if mid >= 0:
        if topLeftCorner == topMid and topRightCorner == topMid and topMid != 0:   #horizontal top
            print(f"{topMid} is the winner")
            return
        elif topLeftCorner == leftMid and botLeftCorner == leftMid and leftMid != 0:   #vertical left side
            print(f"{leftMid} is the winner")
            return
        elif topRightCorner == rightMid and botRightCorner == rightMid and rightMid != 0:   #vertical right side
            print(f"{rightMid} is the winner")
            return
        elif botLeftCorner == botMid and botRightCorner == botMid and botMid != 0:  #horizontal bot
            print(f"{botMid} is the winner")
            return
    print("No winners here today! Try again.") #all other solutions which there aren't any left..
        
            
winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

checkWinner(winner_is_2)    
checkWinner(winner_is_1)
checkWinner(winner_is_also_1)
checkWinner(no_winner)
checkWinner(also_no_winner)


