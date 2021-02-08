"""
This is an interview question asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

"""
Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
"""

def f_nonadj(x):
    if not x:
        return 0
    return max(f_nonadj(x[1:]), x[0] + f_nonadj(x[2:]))

def f_nonadj2(x):
    nonadj = max(x[0], 0)
    adj = max(x[1], nonadj)
    for i in x[2:]:
        temp = adj
        nonadj = max(adj, nonadj + x[i])
        adj = temp + x[i]   
    return max(adj, nonadj)

def largest_non_adjacent(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    max_excluding_last = max(0, arr[0])
    max_including_last = max(max_excluding_last, arr[1])

    for num in arr[2:]:
        prev_max_including_last = max_including_last

        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)

numbers = [[2, 4, 6, 2, 5], [5, 1, 1, 5], [5, 1, 1, 5, -1, 6, 5, 1, 1, -1], [2, 4, 6, 2, 5,-1,1,100,21,56]]
for i in numbers:
    print(largest_non_adjacent(i))
    print(f_nonadj(i))
