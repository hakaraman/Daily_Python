def max_subarray(lst, k):
    lst_max_subarray = list()
    for i in range(len(lst)-(k-1)):
        lst_max_subarray.append(max(lst[i:i+k]))
    return lst_max_subarray

from itertools import combinations

def find_max1(lst, k):
    temp = combinations(lst, k)
    result = set()
    for i in temp:
        result.add(sum(i))        
    return list(result)

def find_max(lst, k):
    result = []
    for i in range(len(lst)- k +1):
        result.append(max(lst[i:i+k]))
    return result

def find_max2(lst, k):
    return [max(lst[i:i+k]) for i in range(len(lst)- k +1)]

def max_of_subarrays1(lst, k):
    for i in range(len(lst) - k + 1):
        print(max(lst[i:i + k]), lst[i:i + k])

from collections import deque

def max_of_subarrays(lst, k):
    q = deque()
    for i in range(k):
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)

    # Loop invariant: q is a list of indices where their corresponding values are in descending order.
    for i in range(k, len(lst)):
        print(lst[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    print(lst[q[0]])
    
lst = [10, 5, 2, 7, 8, 7]
k = 3
#print(max_subarray(lst, k))
print(find_max2(lst, k))
#print(max_of_subarrays1(lst, k))
#print(max_of_subarrays(lst, k))