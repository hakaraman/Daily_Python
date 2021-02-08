"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
from itertools import combinations
from math import factorial

def climbStairs(n):
    count=0
    for i in range(n,1,-2):
        count += factorial(i+(n-i)//2) / factorial(i) / factorial((n-i)//2)
    return int(count)    

print(climbStairs(3))