"""
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ] exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""
def search(board, row, col, word, index, visited):
    def is_valid(board, row, col):
        return row >= 0 and row < len(board) and col >= 0 and col < len(board[0])

    if not is_valid(board, row, col):
        return False
    if (row, col) in visited:
        return False
    if board[row][col] != word[index]:
        return False
    if index == len(word) - 1:
        return True

    visited.add((row, col))

    for d in ((0, -1), (0, 1), (-1, 0), (1, 0)):
        if search(board, row + d[0], col + d[1], word, index + 1, visited):
            return True

    visited.remove((row, col))  # Backtrack

    return False

def find_word(board, word):
    M = len(board)
    N = len(board[0])

    for row in range(M):
        for col in range(N):
            visited = set()
            if search(board, row, col, word, 0, visited):
                return True


def f_word(board, word):
    def check_adj(r,c,pos,visited):
        if not (r>=0 and r < len(board) and c >= 0 and c < len(board[0]) and pos < len(word)): return False
        if (r,c) in visited: return False
        if board[r][c] != word[pos]: return False
        if pos == len(word) - 1: return True
        visited.add((r,c))
        for i in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            if check_adj(r+i[0],c+i[1],pos+1,visited):
                return True
        visited.remove((r,c))
        return False

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == word[0]:
                if check_adj(r,c,0,set()):
                    return True
    return False

def f_word2(board, word):
    def check_adj(r,c,word):
        if board[r][c] != word[0]: return False
        for i in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            check = True
            r1, c1 = r + i[0], c + i[1]
            for j in range(1, len(word)):
                if r1 >=0 and r1 < len(board) and c1 >= 0 and c1 < len(board[0]) and word[j] == board[r1][c1]:
                #if r1 >=0 and c1 >= 0 and word[j] == board[r1][c1]:    
                    r1, c1 = r1 + i[0], c1 + i[1]
                else:
                    check = False
                    break
            if check:
                return True
        return False

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == word[0]:
                if check_adj(r,c,word):
                    return True
    return False


b = [ ['A','B','C','E'], ['S','F','C','S'], ['A','D','E','E'] ]
lst = ["ABCCED", "SEE", "ABCB"]

for i in lst:
    print(find_word(b,i))
    print(f_word(b,i))
    print(f_word2(b,i))