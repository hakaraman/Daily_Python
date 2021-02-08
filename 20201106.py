"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

def twoSum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]

def twoSum1(nums, target):
    for i in range(len(nums)):
        if (target-nums[i] in nums) and nums.index(target-nums[i]) != i:
            return [i, nums.index(target-nums[i])]

def twoSum2(nums, target):
    return [[i] + [nums.index(target-nums[i])] for i in range(len(nums)) if (target-nums[i] in nums) and nums.index(target-nums[i]) != i][0]

def twoSum3(nums, target):
    for i in range(len(nums)):
        addup = target-nums[i]
        j = nums.index(addup)  
        if (addup in nums) and j != i:
            return [i, j]

def twoSum4(nums, target):
    d = {}
    for i in range(len(nums)):
        if target-nums[i] in d:
            return [d[target-nums[i]], i]
        d[nums[i]] = i

nums = [2,7,11,15]
print(twoSum4(nums,9))