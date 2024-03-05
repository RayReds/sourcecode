#Problems at : https://leetcode.com/problems/sudoku-solver/description/

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

def FindEmpty():
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == '.':
                return y, x
    return None

def CheckValid(y, x, num):
    #Check Vertical
    for i in board[y]:
        if i == num:
            return False
    #Check Horizontal
    for i in board:
        if i[x] == num:
            return False
    #Checks 3x3 Availability
    y = y//3*3
    x = x//3*3
    for i in range(3):
        for j in range(3):
            if board[y+i][x+j] == num:
                return False
    return True

def Printboard():
    for i in board:
        print(i)
    print()

def Main():
    result = FindEmpty()
    if not result:
        return True
    y,x = result
    for i in range(1, 10):
        if CheckValid(y, x, str(i)):
            board[y][x] = str(i)
            if Main():
                return True
    board[y][x] = "."
    return False
if Main():
    Printboard()
else:
    print("sudoku is not valid")
