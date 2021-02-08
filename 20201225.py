# Group Anagrams
# Given a list of strings, group anagrams together.
# Example:
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

def groupAnagrams(strs):
    anagrams = {}
    for i in strs:
        item = "".join(sorted(i))
        if item in anagrams:
            anagrams[item].append(i)
        else:
            anagrams[item]=[i]
    return anagrams.values()

def groupAnagrams1(strs):
    result = dict()
    for i in strs:
        result["".join(sorted(i))] = result.get("".join(sorted(i)), []) + [i]
    return result.values()

from collections import defaultdict

def groupAnagrams2(strs):
    anagrams = defaultdict(list)
    for s in strs:
        anagrams[tuple(sorted(s))].append(s)
    return anagrams.values()

def groupAnagrams3(strs):
    anagrams = dict()
    for s in strs:
        anagrams[tuple(sorted(s))].append(s)
    return anagrams.values()

strs=["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams3(strs))



