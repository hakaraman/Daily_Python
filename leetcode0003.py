"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
"""
def lengthOfLongestSubstring(s):
    smax = ""
    temp = ""
    for i in s:
        if i in temp:
            if len(temp) > len(smax):
                smax = temp
            while i in temp:
                temp = temp[1:]
        temp += i
    return smax if len(smax) >= len(temp) else temp


def lengthOfLongestSubstring(s):
    smax = ""
    temp = ""
    for i in s:
        if i in temp:
            if len(temp) > len(smax):
                smax = temp
            while i in temp:
                temp = temp[1:]
        temp += i
    return max(len(smax),len(temp))

def lengthOfLongestSubstring(s):
    smax, temp = 0, ""
    for i in s:
        if i in temp:
            smax = max(smax, len(temp))
            while i in temp:
                temp = temp[1:]
        temp += i
    return max(smax,len(temp))
        

s = "pwwkew"
print(lengthOfLongestSubstring(s))