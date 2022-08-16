"""
Rat can move in all direction
"""


def is_safe(x, y, rows, cols, res, mat):
    if x < rows and y < cols and mat[x][y] == 1 and res[x][y] != 1:
        return True
    return False


def rat_in_maze(x, y, rows, cols, res, mat):
    if x == rows - 1 and y == cols - 1:
        res[x][y] = 1
        return True
    if is_safe(x, y, rows, cols, res, mat):
        res[x][y] = 1
        if rat_in_maze(x + 1, y, rows, cols, res, mat):
            return True
        if rat_in_maze(x - 1, y, rows, cols, res, mat):
            return True
        if rat_in_maze(x, y + 1, rows, cols, res, mat):
            return True
        if rat_in_maze(x, y - 1, rows, cols, res, mat):
            return True
        res[x][y] = 0
        return False


if __name__ == '__main__':

    mat = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1],
    ]

    rows = len(mat[0])
    cols = len(mat)
    res = [[0 for j in range(cols)]for i in range(rows)]
    if rat_in_maze(0, 0, rows, cols, res, mat):
        print(res)
