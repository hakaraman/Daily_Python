"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
def majorityElement(nums):
    return max(set(nums),key=nums.count)

def majorityElement2(nums):
    d = dict()
    maxitem = nums[0]
    for i in nums:
        if i in d.keys():
            d[i] += 1
            if d[maxitem] < d[i]:
                maxitem = i
        else:
            d[i] = 1
    return maxitem

def majorityElement4(nums):
    if len(nums) == 1:
        return nums[0]
    d = dict()
    for i in nums:
        if i in d.keys():
            d[i] += 1
            if d[i] >= len(nums)/2:
                return i
        else:
            d[i] = 1

def majorityElement3(nums):
    for i in set(nums):
        if nums.count(i) >= len(nums)/2:
            return i
from collections import deque  

def majorityElement5(nums):
    dq = deque(nums)
    return max(set(dq),key=dq.count)

def majorityElement6(nums):
    if len(nums) == 1:
        return nums[0]
    dq = deque(nums)
    for i in set(dq):
        if dq.count(i) >= len(dq) / 2:
            return i

def majorityElement7(nums):
    nums.sort()
    j = 1
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            j += 1
            if j >= len(nums)/2:
                return nums[i]
        else:
            j = 1
    return nums[0]

lst =[3,2,3]
print(majorityElement7(lst))