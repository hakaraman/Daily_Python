"""
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. You can assume b can only be 1 or 0.
"""

def check(x,y,b):
    return x*b | y*(1-b)
    #return b*(x-y) + y 

print(check(0,8,1))
print(check(0,8,0))