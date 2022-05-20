from ast import Return
import random

Board = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

def Random_2_Generator(board):    #Generates a 2 in a random location every turn
    empty = []
    for i in range(0,4): 
        for j in range(0,4):
            if board[i][j] == 0: empty += (i,j)     #Finds an empty cell and adds it to empty[]
    if len(empty) <= 2: board[empty[0]][empty[1]] = 2   #if there is only one empty cell, that cell will be filled
    else: 
        x = random.randint(0,(len(empty)-2))    #Else randomly pick a cell and fill it
        board[empty[x]][empty[x+1]] = 2
    return board

Random_2_Generator(Board)    #Generates the first 2 at the start of the game
Random_2_Generator(Board)

def Print_Board(board):   #Prints board to console, Will be removed once GUI is implimented

    Temp_board =[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]

    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == 0: Temp_board[i][j] = " "
            else: Temp_board[i][j] = board[i][j]

    print("\n" + str(Temp_board[0][0]) + " | " + str(Temp_board[0][1]) + " | " + str(Temp_board[0][2]) + " | " + str(Temp_board[0][3]))
    print("-   -   -   -")
    print(str(Temp_board[1][0]) + " | " + str(Temp_board[1][1]) + " | " + str(Temp_board[1][2]) + " | " + str(Temp_board[1][3]))  
    print("-   -   -   -") 
    print(str(Temp_board[2][0]) + " | " + str(Temp_board[2][1]) + " | " + str(Temp_board[2][2]) + " | " + str(Temp_board[2][3]))
    print("-   -   -   -")
    print(str(Temp_board[3][0]) + " | " + str(Temp_board[3][1]) + " | " + str(Temp_board[3][2]) + " | " + str(Temp_board[3][3]) +"\n")

def Board_Limits(a):    #Check to make sure numbers dont end up in the -1st or 4th index
    if a >= 3: a = 3
    if a <= 0: a = 0
    return(a)

def Move_Direction(i,j,move):   #Outputs direction that numbers need to move depending on W/A/S/D
    if move == "w": y, x = i-1, j     #Move Upwards
    elif move == "a": y, x = i, j-1   #Move to the left
    elif move == "s": y, x = i=1, j   #Move Downwards
    elif move == "d": y, x = i, j+1   #Move to the right
    return(y,x)

def Move_Numbers(move, board):     #Moves characters in the required direction
    for i in range(0,4):
        for j in range(0,4):
            y, x = Move_Direction(i,j,move)
            x = Board_Limits(x)
            y = Board_Limits(y)
            if board[i][j] != 0 and board[y][x] == 0:
                board[y][x] = board[i][j]
                board[i][j] = 0
                Move_Numbers(move, board)      #Recursively calls itself till all characters have moved
    return board

def Addition(move, board):     #Adds characters together once moved
    for i in range(0,4):
        for j in range(0,4):
            y, x = Move_Direction(i, j, move)
            if x != Board_Limits(x) or y != Board_Limits(y): pass
            elif board[i][j] != 0 and board[y][x] == board[i][j]:
                    board[i][j] = 0
                    board[y][x] *= 2
    return board

def Game_over(board):   #Checks if Game is over
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == 0: return False
            elif board[i][j] == board[Board_Limits(i+1)][j] or board[i][Board_Limits(j+1)]: return False    #if there are cells that can be combined, return false
    return True

while Game_over(Board) == False:
    Print_Board(Board)
    move = input()
    if (move == "w" or move == "a" or move == "s" or move == "d"): 
        Random_2_Generator(Board)
        Board = Move_Numbers(move, Board)
        Board = Addition(move, Board)
        Board = Move_Numbers(move, Board)
    else: pass

print("Game over")