"""
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8 ), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
[[6, 8], [1, 9], [2, 4], [4, 7]]   -------> [1,9]
[[1,3],[2,6],[8,10],[15,18]]  ------------> [[1,6],[8,10],[15,18]] (edited) 
"""

def fix_overlap(lst):
    lst.sort(key = lambda x:x[0])
    result = [list(lst[0])]
    for i in lst[1:]:
        if i[0] > result[-1][1]:
            result.append(list(i))
        else:
            result[-1][1] = max(result[-1][1], i[1])
    return [tuple(i) for i in result]

def fix_overlap2(lst):
    lst.sort(key = lambda x:x[0])
    start, end = lst[0]
    result = []
    for i in lst[1:]:
        if i[0] > end:
            result.append((start,end))
            start, end = i
        else:
            end = max(end, i[1])
    result.append((start,end))
    return result

def merge(intervals):
    result = []
    for start, end in sorted(intervals, key=lambda i: i[0]):
        # If current interval overlaps with the previous one, combine them
        if result and start <= result[-1][1]:
            prev_start, prev_end = result[-1]
            result[-1] = (prev_start, max(end, prev_end))
        else:
            result.append((start, end))
    return result    

lst = []
lst.append([(1, 3), (5, 8 ), (4, 10), (20, 25)])
lst.append([(6, 8), (1, 9), (2, 4), (4, 7)])
lst.append([[1,3],[2,6],[8,10],[15,18]] )
for i in lst:
    print(fix_overlap(i))
    print(fix_overlap2(i))