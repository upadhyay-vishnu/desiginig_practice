n = 8
board = [[-1 for i in range(8)] for i in range(8)]

move_x = [2, 2, 1, 1, -2, -2, -1, -1]
move_y = [1, -1, 2, -2, 1, -1, 2, -2]
pos = 1


def printSolution(n, board):
    '''
        A utility function to print Chessboard matrix
    '''
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def is_safe(x, y):
    if (x < n and y < n and board[x][y] == -1 and x >= 0 and y >= 0):
        return True
    return False


def knight_util(n, x, y, move_x, move_y, pos, board):
    if(pos == n**2):
        return True

    for i in range(n):
        next_x = move_x[i]
        next_y = move_y[i]

        if is_safe(next_x, next_y):
            board[next_x][next_y] = pos
            if (knight_util(n, next_x, next_y, move_x, move_y, pos + 1, board)):
                return True
            board[next_x][next_y] = -1
        return False
