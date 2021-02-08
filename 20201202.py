"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""
def rob2(nums):
    if len(nums) < 3:
        return max(nums) if nums else 0
    mx_nonadj, mx_adj = nums[0], nums[1]
    for i in nums[2:]:
        mx_adj, mx_nonadj = max(mx_adj, mx_nonadj+i), max(mx_adj, mx_nonadj)
    return  max(mx_adj, mx_nonadj)

def rob(nums):
    mx_nonadj = mx_adj = 0
    for i in nums:
        mx_adj, mx_nonadj = max(mx_adj, mx_nonadj+i), max(mx_adj, mx_nonadj)
    return  max(mx_adj, mx_nonadj)

lst = [2,1,1,2]
print(rob2(lst))