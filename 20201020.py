"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.
"""
def longest_consecutive(nums):
    max_len = 0
    bounds = dict()
    for num in nums:
        if num in bounds:
            continue
        left_bound, right_bound = num, num
        if num - 1 in bounds:
            left_bound = bounds[num - 1][0]
        if num + 1 in bounds:
            right_bound = bounds[num + 1][1]
        bounds[num] = left_bound, right_bound
        bounds[left_bound] = left_bound, right_bound
        bounds[right_bound] = left_bound, right_bound
        max_len = max(right_bound - left_bound + 1, max_len)
    return max_len

def longest1(nums):
    nums.sort()
    prev = nums[0]
    result = 1
    temp = 1
    for i in range(1,len(nums)):
        if nums[i] == prev + 1:
            temp += 1
        else:
            temp = 1
        if result < temp:
            result = temp
        prev = nums[i]
    return result

def longest(nums):
    nums.sort()
    d = dict()
    for i in nums:
        d[i] = i
        if i-1 in d.keys():
            d[i] = d[i-1]           
    return (lambda y: y[0]-y[1]+1)(max(d.items(), key = lambda x: x[0]-x[1]))

def longest3(nums):
    d = dict()
    for i in nums:
        d[i] = i
        j = i
        while j-1 in d.keys():
            d[j] = d[j-1]
            j -= 1
        k = i
        while k+1 in d.keys():
            d[k+1] = j
            k += 1
    return (lambda y: y[0]-y[1]+1)(max(d.items(), key = lambda x: x[0]-x[1]))

def longest2(nums):
    mx = 0
    adj = dict()
    for i in nums:
        if i in adj:
            continue
        lst = [i]*3
        if i - 1 in adj:
            lst[0] = adj[i - 1][0]
        if i + 1 in adj:
            lst[2] = adj[i + 1][1]
        for j in lst:
            adj[j] = lst[0], lst[2]
        mx = max(lst[2] - lst[0] + 1, mx)
    return mx

lst = [100,5, 4, 200, 1, 3, 2]
print(longest2(lst))
print(longest_consecutive(lst))
print(longest(lst))
