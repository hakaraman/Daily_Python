"""
Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""
import numpy as np
from random import randrange
def process_list(n, l):
    all_nums_set = set()
    for i in range(n):
        all_nums_set.add(i)

    l_set = set(l)
    nums_set = all_nums_set - l_set
    return list(nums_set)

def random_number_excluing_list(n, l):
    nums_list = process_list(n, l)
    idx = randrange(0, len(nums_list))
    return nums_list[idx]

def rand_int(n, lst):
    a=np.random.choice(range(0,n))
    return a if a not in lst else rand_int(lst, n)

from random import choice
def r_int(n, l):
    return choice([i for i in range(n) if i not in l])

print(random_number_excluing_list(6, [1, 2, 5]))
#print(rand_int(4, [1, 2, 5]))
print(r_int(6, [1, 2, 5]))