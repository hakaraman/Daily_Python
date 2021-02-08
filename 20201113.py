"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""
def lengthOfLastWord(s):
    lst = s.split()
    return len(lst[-1]) if lst else 0

def lengthOfLastWord1(s):
    s = s.strip()
    pos = s.rfind(" ")
    return len(s[pos+1:]) if pos>-1 else (len(s) if s else 0)

s = "a "
print(lengthOfLastWord1(s))