"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).
"""
def findMedianSortedArrays(nums1, nums2):
    lst = nums1 + nums2
    if lst == []:
        return 0
    lst.sort()
    mid = len(lst) // 2
    return lst[mid] if len(lst) % 2 != 0 else (lst[mid] + lst[mid-1]) / 2 

print(findMedianSortedArrays([],[]))