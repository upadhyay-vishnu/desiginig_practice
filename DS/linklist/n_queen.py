"""
Given 4 queen, place them in 2-D matrix so that they can't attack
"""

move_x = [0, 0, 1, -1, 1, 1, -1, -1]
move_y = [1, -1, 0, 0, 1, -1, 1, -1]

def is_safe(q1_x, q1_y, q2_x, q2_y):
    if max([q1_x, q1_y, q2_x, q2_y]) < n and \
        min([q1_x, q1_y, q2_x, q2_y]) >= 0 and \
            abs(q1_x-q2_x) == abs(q1_y- q2_y) and \
            q1_x != q2_x and q1_y != q2_y:
        return True
    return False


def n_queen_util(q, q1_x, q1_y, q2_x, q2_y, mat, arr):
    """
    0, 1, 1, 1, 2, 1
    """
    
    if not is_safe(q1_x, q1_y, q2_x, q2_y):
        n_queen_util(q1_x, q1_y, q2_x, q2_y + 1)
    else:
        arr.append(q)


def n_queen(arr):
    queens = ['q2', 'q3', 'q4']
    arr.append('q1')
    q1_x = 0
    q1_y = 0
    for q in queens:
        if n_queen_util(q, 0, 0, q1_x, q1_y):
            arr.append(q)
        else:
            arr.pop()


