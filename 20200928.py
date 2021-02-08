# Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
# For example, given the following matrix:
# [[1,  2,  3,  4,  5],
#  [6,  7,  8,  9,  10],
#  [11, 12, 13, 14, 15],
#  [16, 17, 18, 19, 20]]

def movespiral(matrix):
    borders = [len(matrix[0]), len(matrix), -1, -1]
    opr = [1,1,-1,-1]
    pos = [0 , 0]
    dir = 0
    while True:
        print(matrix[pos[1]][pos[0]])
        i = dir % 2
        if pos[i] + opr[dir] == borders[dir]:
            return
        else:    
            pos[i] += opr[dir]
            if pos[i] + opr[dir] == borders[dir]:
                borders[dir-1] = pos[1-i]
                dir = (dir + 1) % 4     


def movespiral2(matrix):
    x, y = 0 , 0
    #directions: 0 right, 1 down, 2 left, 3 up
    borders = [len(matrix[0])-1, len(matrix)-1, 0, 0]
    dir = 0
    while True:
        print(matrix[y][x])
        if dir == 0:
            if x == borders[dir]:
                return
            x += 1
            if x == borders[dir]:
                borders[3] = y + 1
                dir += 1               
        elif dir == 1:
            if y == borders[dir]:
                return
            y += 1
            if y == borders[dir]:
                borders[0] = x - 1
                dir += 1
        elif dir == 2:
            if x == borders[dir]:
                return
            x -= 1
            if x == borders[dir]:
                borders[1] = y - 1
                dir += 1
        elif dir == 3:
            if y == borders[dir]:
                return
            y -= 1
            if y == borders[dir]:
                borders[2] = x + 1
                dir += 1
        else:
            dir = 0                


def next_direction(direction):
    if direction == RIGHT:
        return DOWN
    elif direction == DOWN:
        return LEFT
    elif direction == LEFT:
        return UP
    elif direction == UP:
        return RIGHT

def next_position(position, direction):
    if direction == RIGHT:
        return (position[0], position[1] + 1)
    elif direction == DOWN:
        return (position[0] + 1, position[1])
    elif direction == LEFT:
        return (position[0], position[1] - 1)
    elif direction == UP:
        return (position[0] - 1, position[1])

def should_change_direction(M, r, c):
    in_bounds_r = 0 <= r < len(M)
    in_bounds_c = 0 <= c < len(M[0])
    return not in_bounds_r or not in_bounds_c or M[r][c] is None

def matrix_spiral_print(M):
    remaining = len(M) * len(M[0])
    current_direction = RIGHT
    current_position = (0, 0)
    while remaining > 0:
        r, c = current_position
        print(M[r][c])
        M[r][c] = None
        remaining -= 1

        possible_next_position = next_position(current_position, current_direction)
        if should_change_direction(M, possible_next_position[0], possible_next_position[1]):
            current_direction = next_direction(current_direction)
            current_position = next_position(current_position, current_direction)
        else:
            current_position = possible_next_position
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

DIRECTIONS = [RIGHT, DOWN, LEFT, UP]

data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
#data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21,22,23,24,25]]

#matrix_spiral_print(data)
movespiral(data)