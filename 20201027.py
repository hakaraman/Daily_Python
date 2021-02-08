"""
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
"""

def non_duplicated_int(lst):
    return [i for i in lst if lst.count(i) == 1][0]

def non_duplicated_int1(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return list(filter(lambda x: (d[x] == 1), d))[0]
    #return [k for k,v in d.items() if v == 1][0]

def non_duplicated_int2(lst):
    return (sum(set(lst)) * 3 - sum(lst)) // 2

def non_duplicated_int3(lst):
    a, b = 0, 0
    for x in lst:
        a, b = (~x&a&~b)|(x&~a&b), ~a&(x^b)
    return b
    

lst = [6, 1, 3, 3, 3, 6, 6]
print(non_duplicated_int(lst))
print(non_duplicated_int3(lst))