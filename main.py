#TODO: 
# A better implimentation of Random_2_Generator()
# Impliment a Game Over state
# GUI 
# Fix multiple combination in 1 turn while adding horizontally bug (2 2 4 8 => 16 : in 1 turn instead of 3)
# Ensure that movement must occur for an extra 2 to be added to the board
# README.md

import random

board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

def Random_2_Generator():    #Generates a 2 in a random location every turn
    i = random.randint(0,3)
    j = random.randint(0,3)
    if board[i][j] != 0:    #Checks to ensure generated slot is empty
        Random_2_Generator() 
    else:
        board[i][j] = 2

Random_2_Generator()    #Generates the first 2 at the start of the game

def Print_Board():  #Prints board to console, Will be removed once GUI is implimented
    print("\n" + str(board[0][0]) + " | " + str(board[0][1]) + " | " + str(board[0][2]) + " | " + str(board[0][3]))
    print("-   -   -   -")
    print(str(board[1][0]) + " | " + str(board[1][1]) + " | " + str(board[1][2]) + " | " + str(board[1][3]))  
    print("-   -   -   -") 
    print(str(board[2][0]) + " | " + str(board[2][1]) + " | " + str(board[2][2]) + " | " + str(board[2][3]))
    print("-   -   -   -")
    print(str(board[3][0]) + " | " + str(board[3][1]) + " | " + str(board[3][2]) + " | " + str(board[3][3]) +"\n")


def Board_Limits(a):    #Check to make sure numbers dont end up in the -1st or 4th index
    if a >= 3:
        a = 3
    if a <= 0:
        a = 0
    return(a)

def Move_Direction(i,j,move):   #Outputs direction that numbers need to move depending on W/A/S/D
    if move == "w":     #Move Upwards
        y = i-1
        x = j
    elif move =="a":    #Move to the left
        y = i
        x = j-1
    elif move == "s":   #Move Downwards
        y = i+1
        x = j
    elif move == "d":   #Move to the right
        y = i
        x = j+1
    return(y,x)

def Move_Numbers(move):     #Moves characters in the required direction
    for i in range(0,4):
        for j in range(0,4):
            y, x = Move_Direction(i,j,move)
            x = Board_Limits(x)     #Checks to ensure they are within limits
            y = Board_Limits(y)
            if board[i][j] != 0 and board[y][x] == 0:   #Checks if cell is empty
                board[y][x] = board[i][j]
                board[i][j] = 0
                Move_Numbers(move)      #Recursively calls itself till all characters have moved
                #Print_Board()

def Addition(move):     #Adds characters together once moved
    for i in range(0,4):
        for j in range(0,4):
            y, x = Move_Direction(i,j,move)
            if x != Board_Limits(x) or y != Board_Limits(y):    #Check for Limits
                pass
            else:  
                if board[i][j] != 0 and board[y][x] == board[i][j]:     #Checks if the two numbers are equal
                    board[i][j] = 0
                    board[y][x] *= 2

while True:
    Random_2_Generator()
    Print_Board()
    move = input()
    Move_Numbers(move)
    Addition(move)