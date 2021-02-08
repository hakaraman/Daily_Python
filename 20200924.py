"""
Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.
For example, given the following matrix:
[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
"""

def find_word(table, word):
    for i in range(len(table)):
        for j in range(len(table[0])):
            if "".join(table[i][j:len(word)]) == word: 
                return True # yatay kontrol
            if ''.join([table[x][j] for x in range(i, min(len(table), len(word)))]) == word:
                return True # dikey kontrol
    return False

def check(matrix, word):
    pool = []
    for i in range(len(matrix)):
        temp = ""
        for j in range(i, len(matrix[i])):
            temp += matrix[i][j]
        pool.append(temp)
    temp = ""
    counter = 0
    while len(matrix[0])>counter:
        temp = ""
        for i in range(len(matrix)):
            temp += matrix[i][counter]
            pool.append(temp)
        counter += 1
    return (word in pool)   

table = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

print(find_word(table,'CQOS'))
print(check(table,'ACI'))