"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
 
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:
Input: s = "A", numRows = 1
Output: "A"
"""
from itertools import chain
def convert(s, numRows):
    r,c,dir = 0,0,1
    table = [[False for i in range(len(s)//2+1)] for j in range(numRows)]
    for i in range(len(s)):
        table[r][c] = s[i]
        if dir:            
            r += 1
            if r == numRows:
                r -= 2
                dir = 1-dir
                c += 1
        else:
            c += 1
            r -= 1
            if r == -1:
                r = 1
                c -= 1
                dir = 1-dir
    return "".join(item for rows in table for item in rows if item) 

def convert2(s, numRows):
    if len(s) <= numRows or numRows == 1:
        return s
    table = [""]*numRows
    r,dir = 0,0
    for i in s:
        if (r == numRows-1) or (r == 0):
            dir = 1 - dir
        table[r] += i
        if dir:
            r += 1
        else:
            r -= 1
    return "".join(table)

def convert3(s, numRows):
    if len(s) <= numRows or numRows == 1:
        return s
    table = [""]*numRows
    r,dir = 0,-1
    for i in s:
        if (r == numRows-1) or (r == 0):
            dir *= -1
        table[r] += i
        r = r + dir
    return "".join(table)

def convert4(s, numRows):
    if len(s) <= numRows or numRows == 1:
        return s
    r,c,dir = 0,0,0
    table = [["" for i in range(len(s)//2+1)] for j in range(numRows)]
    for i in s:
        if (r == numRows-1) or (r == 0):
            dir = 1-dir
        table[r][c] = i

        if dir:
            r += 1
        else:
            c += 1
            r -= 1
    return "".join(chain(*table))


s = "PAYPALISHIRING"
print(convert4(s,3))

