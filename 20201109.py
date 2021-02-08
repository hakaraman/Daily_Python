"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
"""
def removeDuplicates(nums):
    try:
        i = 0
        while True:
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
            else:
                i += 1
    except:
        return len(nums)

def removeDuplicates2(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.pop(i+1)
        else:
            i += 1
    return len(nums)

def removeDuplicates4(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.remove(nums[i+1])
        else:
            i += 1
    return len(nums)

def removeDuplicates3(nums):
    i,j,c = 0,0,1
    for i in range(len(nums)):
        if nums[i] != nums[j]:
            c+=1
            j+=1
            nums[j]=nums[i]
    return c

def removeDuplicates5(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        i += 1
    return j+1
    
lst = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates5(lst), lst)