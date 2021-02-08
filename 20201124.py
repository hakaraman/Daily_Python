"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""

def generate(numRows):
    if numRows < 3:
        return [] if numRows < 1 else ([[1]] if numRows == 1 else [[1],[1,1]])
    result = [[1],[1,1]]
    for i in range(3,numRows+1):
        result.append([1]+[result[-1][j]+result[-1][j+1] for j in range(len(result[-1])-1)]+[1])
    return result

def generate2(numRows): 
    result = [[1]]
    for i in range(1,numRows):
        result.append([1]+[result[-1][j]+result[-1][j+1] for j in range(len(result[-1])-1)]+[1])
    return [] if numRows < 1 else result

print(generate2(10))    