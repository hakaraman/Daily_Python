"""
This is an interview question asked by Google.

The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

def distance(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return max(len(s1), len(s2))

    return min(distance(s1[1:], s2) + 1,
               distance(s1, s2[1:]) + 1,
               distance(s1[1:], s2[1:]) if s1[0] == s2[0]
               else distance(s1[1:], s2[1:]) + 1)

def distance2(s1, s2):
    x = len(s1) + 1 
    y = len(s2) + 1 

    A = [[-1 for i in range(x)] for j in range(y)]
    for i in range(x):
        A[0][i] = i

    for j in range(y):
        A[j][0] = j

    for i in range(1, y):
        for j in range(1, x):
            if s1[j-1] == s2[i-1]:
                A[i][j] = A[i-1][j-1]
            else:
                A[i][j] = min(A[i-1][j] + 1, A[i][j-1] + 1, A[i-1][j-1] + 1)
    return A[-1][-1] 


def compare(str1, str2):
    count = 0
    for a, b in zip(str1, str2):
        if a == b:
            count += 1
    return count

def compare2(str1, str2):
    intersection = set(str1).intersection(set(str2))
    items = []
    for i in str1:
        if i in intersection:
            items.append(i)
    return "".join(items)

def distance3(s1,s2):
    maxsame = 0
    if len(s1) < len(s2):
        smin, smax = s1, s2
    else:
        smin, smax = s2, s1
    for i in range(len(smax)):
        t1 = smax[i:]
        t2 = smax[:i]
        x = compare(smax[i:],smin)
        y = compare(smax[:i],smin)
        if max(x,y) > maxsame:
            maxsame = max(x,y)     
    return len(smax) - maxsame


def distance4(s1,s2):
    maxsame = 0
    if len(s1) < len(s2):
        smin, smax = s1, s2
    else:
        smin, smax = s2, s1
    intersection = set(s1).intersection(set(s2))
    items = []
    for i in s1:
        if i in intersection:
            items.append(i)
    tempstr = s2
    tempitems = items.copy()
    items = []
    for i in tempitems:
        if i in tempstr:
            items.append(i)
            pos = tempstr.find(i)
            tempstr = tempstr[:pos]+tempstr[pos+1:]
            
    maxsame = len(items)

    return len(smax) - maxsame

def distance5(s1,s2):
    maxsame = 0
    if len(s1) < len(s2):
        smin, smax = s1, s2
    else:
        smin, smax = s2, s1
    intersection = set(s1).intersection(set(s2))
    items1 = []
    items2 = dict()
    for i in s1:
        if i in intersection:
            if i in s2:
                pos = s2.find(i)
                items1.append(i)
                items2[pos] = i
                s2 = s2[:pos] + "0" + s2[pos+1:]
    for i in items1:
         
    tempstr = s2
    tempitems = items.copy()
    items = []
    for i in tempitems:
        if i in tempstr:
            items.append(i)
            pos = tempstr.find(i)
            tempstr = tempstr[:pos]+tempstr[pos+1:]
            
    maxsame = len(items)

    return len(smax) - maxsame    

s1 = "kiitten"
s2 = "sititin"
s1 = s1[::-1]
print(distance2(s1,s2))
print(distance3(s1,s2))
print(distance4(s1,s2))