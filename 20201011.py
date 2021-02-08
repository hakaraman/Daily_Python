"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix. A 1 represents land and 0 represents water, so an island is a group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.
1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""
def checkislands(matrix):
    def checksurroundings(matrix,x,y):
        status = [True for _ in range(4)]
        
        if x>0 and matrix[y][x-1] == 1:
            status[2] = False
        if x < len(matrix[y])-1 and matrix[y][x+1] == 1:
            status[0] = False 
        if y>0 and matrix[y-1][x] == 1:
            status[3] = False
        if y < len(matrix)-1 and matrix[y+1][x] == 1:
            status[1] = False
        if all(status):
            return 1
        elif any(status):
            return 2
        else:
            return 0
    count = 0
    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
        #for x in range(len(matrix[y])):
            if matrix[y][x] == 1:
                status = checksurroundings(matrix,x,y)
                if status == 1:
                    count += 1
                elif status == 2:
                    matrix[y][x]=0
    return count

matrix = [[1, 0, 0, 0, 0],
[0, 0, 1, 1, 0],
[0, 1, 1, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 0, 0, 1],
[1, 1, 0, 0, 1]]

print(checkislands(matrix))