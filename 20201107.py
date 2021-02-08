"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(strs):
    strs.sort()
    result = ""
    index = 0
    try:
        while index < len(strs[0]):
            for i in range(1,len(strs)):
                if strs[i][index] != strs[0][index]:
                    return result
            result += strs[0][index]
            index += 1
    except:
        return result
    return result

def longestCommonPrefix1(strs):
    if len(strs) == 0:
        return ""
    elif len(strs) == 1:
        return strs[0]
    else:
        short = min(strs,key = len)
        result = ""
        index = 0
        while index < len(short):
            for i in range(len(strs)):
                if strs[i][index] != short[index]:
                    return result
            result += short[index]
            index += 1
        return result


def longestCommonPrefix2(strs):
    result = ""
    index = 0
    try:
        short = min(strs,key = len)
        result = ""
        i = 0
        while i < len(short):
            for item in strs:
                if item[i] != short[i]:
                    return result
            result += short[i]
            i += 1
    except:
        return result
    return result

def longestCommonPrefix3(strs):
    if len(strs) < 2:
        return strs[0] if strs else ""
    lst = [i for i in range(len(min(strs,key = len))) for j in range(len(strs)) if strs[j][i] != strs[0][i]]
    return strs[0][:min(lst)] if lst else min(strs,key = len)


strs = ["flower","flow","flight"]
print(longestCommonPrefix3(strs))

print(bool(""))
