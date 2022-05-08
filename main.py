#TODO: 
#   GUI 
#   Ensure that movement must occur for an extra 2 to be added to the board
#   README.md

import random

board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

def Random_2_Generator():    #Generates a 2 in a random location every turn
    empty = []
    for i in range(0,4): 
        for j in range(0,4):
            if board[i][j] == 0: empty += (i,j)     #Finds an empty cell and adds it to empty[]
    if len(empty) <= 2: board[empty[0]][empty[1]] = 2   #if there is only one empty cell, that cell will be filled
    else: 
        x = random.randint(0,(len(empty)-2))    #Else randomly pick a cell and fill it
        board[empty[x]][empty[x+1]] = 2

Random_2_Generator()    #Generates the first 2 at the start of the game

def Print_Board():   #Prints board to console, Will be removed once GUI is implimented
    print("\n" + str(board[0][0]) + " | " + str(board[0][1]) + " | " + str(board[0][2]) + " | " + str(board[0][3]))
    print("-   -   -   -")
    print(str(board[1][0]) + " | " + str(board[1][1]) + " | " + str(board[1][2]) + " | " + str(board[1][3]))  
    print("-   -   -   -") 
    print(str(board[2][0]) + " | " + str(board[2][1]) + " | " + str(board[2][2]) + " | " + str(board[2][3]))
    print("-   -   -   -")
    print(str(board[3][0]) + " | " + str(board[3][1]) + " | " + str(board[3][2]) + " | " + str(board[3][3]) +"\n")


def Board_Limits(a):    #Check to make sure numbers dont end up in the -1st or 4th index
    if a >= 3: a = 3
    if a <= 0: a = 0
    return(a)

def Move_Direction(i,j,move):   #Outputs direction that numbers need to move depending on W/A/S/D
    if move == "w": y, x = i-1, j     #Move Upwards
    elif move == "a": y, x = i, j-1   #Move to the left
    elif move == "s": y, x = i=1, j #Move Downwards
    elif move == "d": y, x = i, j+1  #Move to the right
    return(y,x)

def Move_Numbers(move):     #Moves characters in the required direction
    for i in range(0,4):
        for j in range(0,4):
            y, x = Move_Direction(i,j,move)
            x = Board_Limits(x)     #Checks to ensure they are within limits
            y = Board_Limits(y)
            if board[i][j] != 0 and board[y][x] == 0:    #Checks if cell is empty
                board[y][x] = board[i][j]
                board[i][j] = 0
                Move_Numbers(move)      #Recursively calls itself till all characters have moved
                #Print_Board()

def Addition(move):     #Adds characters together once moved
    for i in range(0,4):
        for j in range(0,4):
            y, x = Move_Direction(i, j, move)
            if x != Board_Limits(x) or y != Board_Limits(y): pass    #Check for Limits
            elif board[i][j] != 0 and board[y][x] == board[i][j]:     #Checks if the two numbers are equal
                    board[i][j] = 0
                    board[y][x] *= 2

def Game_over(board):
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == 0: return False
            elif board[i][j] == board[Board_Limits(i+1)][j] or board[i][Board_Limits(j+1)]: return False
    return True

while Game_over(board) == False:
    Random_2_Generator()
    Print_Board()
    move = input()
    if (move == "w" or move == "a" or move == "s" or move == "d"):
        Move_Numbers(move)
        Addition(move)
        Move_Numbers(move)
    else: pass

print("Game over")