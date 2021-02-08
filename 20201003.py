"""
Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

def longest_increasing_subsequence(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return 1

    max_ending_here = 0
    for i in range(len(arr)):
        ending_at_i = longest_increasing_subsequence(arr[:i])
        if arr[-1] > arr[i - 1] and ending_at_i + 1 > max_ending_here:
            max_ending_here = ending_at_i + 1
    return max_ending_here

def longest_increasing_subsequence2(arr):
    if not arr:
        return 0
    cache = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)
    return max(cache)

def find_longest_sub3(lst):
    stack = [1] * len(lst)
    for i, _ in enumerate(lst[1:],1):
        for j, _ in enumerate(lst):
            if lst[i] > lst[j]:
                stack[i] = max(stack[i], stack[j] + 1)
    return max(stack)

def find_longest_sub2(lst):
    stack = [1] * len(lst)
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] > lst[j]:
                stack[i] = max(stack[i], stack[j] + 1)
    return max(stack)

def find_longest_sub(lst):
    subs = [ [] for i in lst]
    subs[0] =[lst[0]]
    for i in range(1, len(lst)):
        for j in range(i):
            if (lst[i] > lst[j]) and (len(subs[j]) + 1 > len(subs[i])):
                subs[i] = subs[j].copy()
        subs[i].append(lst[i])
    return len(max(subs,key=len))

arr = []
arr.append([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
arr.append([3, 10, 2, 1, 20])
arr.append([50, 3, 10, 7, 40, 80])
arr.append([10, 22, 9, 33, 21, 50, 41, 60])
arr.append([10,9,2,5,3,7,101,18])
arr.append([15, 27, 14, 38, 26, 55, 46, 65, 85])

for i in arr:
    print(1, longest_increasing_subsequence(i))
    print(2, longest_increasing_subsequence2(i))
    print(3, find_longest_sub2(i))

