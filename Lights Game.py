def board_is_happy(board):
    locs = []
    board = [list(i) for i in board]
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 'L':
                locs.append((y, x))
    for i in locs:
        y, x = i[0], i[1]
        if y+1 < len(board):
            if board[y+1][x] not in 'LX.':
                board[y+1][x] = str(int(board[y+1][x])-1)
        if y-1 >= 0:
            if board[y-1][x] not in 'LX.':
                board[y-1][x] = str(int(board[y-1][x])-1)
        if x+1 < len(board):
            if board[y][x+1] not in 'LX.':
                board[y][x+1] = str(int(board[y][x+1])-1)
        if x-1 >= 0:
            if board[y][x-1] not in 'LX.':
                board[y][x-1] = str(int(board[y][x-1])-1)
    for i in board:
        for x in i:
            if x not in 'LX.' and int(x) < 0:
                return False
    return True
def board_is_solved(board):
    locs = []
    board = [list(i) for i in board]
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 'L':
                locs.append((y, x))
    for item in locs:
        y, x = item[0], item[1]
        block = False

        for i in range(x+1, len(board), 1):
            if board[y][i] in '.F' and block == False:
                board[y][i] = 'F'
            if board[y][i] == 'L':
                print(board, y, i)
                return False
            else:
                block = True
        block = False
        for i in range(x-1, -1, -1):
            if block == False:
                if board[y][i] == '.' or board[y][i] == 'F':
                    board[y][i] = 'F'
                if board[y][i] == 'L':
                    print(y, i)
                    return False
                else:
                    block = True
        block = False
        for i in range(y+1, len(board), 1):
            if block == False:
                if board[i][x] == '.' or board[y][i] == 'F':
                    board[i][x] = 'F'
                if board[y][i] == 'L':
                    print(board, y, i)
                    return False
                else:
                    block = True
        block = False
        for i in range(y-1, -1, -1):
            if block == False:
                if board[i][x] == '.' or board[y][i] == 'F':
                    board[i][x] = 'F'
                if board[y][i] == 'L':
                    print(board, y, i)
                    return False
                else:
                    block = True
    board = [''.join(i) for i in board]
    if len(board) == 1 and board[0] not in 'XF0':
        return False
    elif '.' not in ''.join(board) or len(board) == 1:
        return True
    else:
        return False
def get_board_state(board):
    if board_is_happy(board):
        if board_is_solved(board):
            return 'solved'
        else:
            return 'happy'
    else:
        return 'unhappy'
if __name__ == '__main__':
  # Example board, happy state.
  print(get_board_state('''
...1.0..X.
X.....X...
..X.X...0.
X.....X..X
..X.3.....
..X...X..2
.3.2......
X....3....
X..X.1..2.
..X...2...'''.strip().split('\n')))
  # Example board, solved state.
