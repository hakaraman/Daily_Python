"""
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""
def minInsertions(self, s: str) -> int:
    a,b = s,s[::-1]
    dp = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
    for i in range(1,len(s)+1):
        for j in range(1,len(s)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return len(s) - dp[-1][-1]


def f_min_insert4(s): 
  
    table = [["" for _ in range(len(s))] for _ in range(len(s))] 

    for k in range(1, len(s)): 
        i = 0
        for j in range(k, len(s)): 
            if s[i] == s[j]: 
                table[i][j] = s[i] + table[i + 1][j - 1] + s[j]
            else:
                sl = table[i][j - 1] + s[i]
                sr = s[j] + table[i + 1][j] 
            if len(sl) > len(sr):
                table[i][j] = sr
            elif len(sl) < len(sr):
                table[i][j] = sl
            else:
                table[i][j] = sl if sl < sr else sr
            i += 1 
    return table[0][-1]
  
def f_min_insert(s): 
    if s == s[::-1]: 
        return s
    if s[0] == s[-1]: 
        return s[0] + f_min_insert(s[1:-1]) + s[-1]
    else:
        sl = s[0] + f_min_insert(s[1:]) + s[0]
        sr = s[-1] + f_min_insert(s[:-1]) + s[-1]
        if len(sl) > len(sr):
            return sr
        elif len(sl) < len(sr):
            return sl
        return sl if sl < sr else sr
      
def findMinInsertions(str, l, h): 
    if (l == h): 
        return 0
    if (l == h - 1): 
        return 0 if(str[l] == str[h]) else 1
      
    if(str[l] == str[h]): 
        return findMinInsertions(str, l + 1, h - 1) 
    else: 
        return (min(findMinInsertions(str, l, h - 1), 
                    findMinInsertions(str, l + 1, h)) + 1) 

  
def f_min_insert1(str): 
  
    table = [[0 for i in range(len(str))] for i in range(len(str))] 

    for k in range(1, len(str)): 
        i = 0
        for j in range(k, len(str)): 
            if str[i] == str[j]: 
                table[i][j] = table[i + 1][j - 1] 
            else: 
                table[i][j] = min(table[i][j - 1], table[i + 1][j] ) + 1
            i += 1 
    return table[0][-1]



def f_min_insert2(str):
    table = [[0 for i in range(len(str))] for i in range(len(str))] 

    for k in range(1, len(str)): 
        i = 0
        for j in range(k, len(str)): 
            if str[i] == str[j]: 
                table[i][j] = table[i + 1][j - 1] 
            else: 
                table[i][j] = min(table[i][j - 1], table[i + 1][j] ) + 1
            i += 1 
    result = ""
    i, j = 0, len(str)-1
    while i < j:
        if table[i][j] == table[i+1][j-1]:
            result += str[i]
            i += 1
            j -= 1
        elif table[i][j] == table[i+1][j]:
            result += str[i]
            i += 1
        else:
            result = str[j] + result
            j -= 1
    return result

def f_min_insert3(str): 
    n = len(str)
    table = [[0 for i in range(n)] for i in range(n)] 
   
    for gap in range(1, n): 
        l = 0
        for h in range(gap, n): 
            if str[l] == str[h]: 
                table[l][h] = table[l + 1][h - 1] 
            else: 
                table[l][h] = (min(table[l][h - 1],  
                                   table[l + 1][h]) + 1) 
            l += 1
  
    return table[0][n - 1]

  
str = "google"
print(findMinInsertions(str,0,len(str)-1)) 
print(f_min_insert(str))
print(f_min_insert4(str))
