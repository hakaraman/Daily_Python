"""
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.
For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""

def longestpalindrom(text):
    result = ""
    for i in range(len(text)):
        for j in range(len(text),i,-1):
            if (text[i:j] == text[i:j][::-1]) and len(result) < len(text[i:j]):
                result = text[i:j]
    return result

def longestpalindrom2(text):
    return max([text[i:j] for i in range(len(text)) for j in range(len(text),i,-1) if (text[i:j] == text[i:j][::-1])], key = len)

print(longestpalindrom2("bananas"))
