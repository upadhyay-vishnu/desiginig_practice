maze = [[1, 0, 1, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]


i, j = 0, 0
source = i, j


def rat_maze(maze, i, j):
    while True:
        print(i, j, maze[i][j])
        if maze[i][j]:
            j += 1
        else:
            i += 1
        if i == 3 and j == 3:
            return True
        # rat_maze(maze, i, j + 1)
        # print(i, j, maze[i][j])
        # rat_maze(maze, i + 1, j)

    else:
        return False
