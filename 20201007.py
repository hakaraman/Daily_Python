"""
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

def f_mapping1(digits, mapping):
    return mapping[digits[0]] if len(digits) == 1 else [i+j for i in mapping[digits[0]] for j in f_mapping1(digits[1:], mapping)]

def f_mapping2(digits, mapping):

    if len(digits) == 1:
        return mapping[digits[0]]

    result = []
    for i in mapping[digits[0]]:
        for j in f_mapping2(digits[1:], mapping):
            result.append(i + j)
    return result

def get_permutations(digits, mapping):
    digit = digits[0]

    if len(digits) == 1:
        return mapping[digit]

    result = []
    for char in mapping[digit]:
        for perm in get_permutations(digits[1:], mapping):
            result.append(char + perm)
    return result

def f_mapping(digits, mapping):
    res=[""]
    for n in digits:
        res=[i+j for i in res for j in mapping[n]]
    return res

mapping =  {"2": ["a", "b", "c"], "3": ["d", "e", "f", "g"], "4": ["d", "e", "f", "g"] }
mapping =  {"2": ["a", "b", "c"], "3": ["d", "e"], "4": ["f", "g"] }

print(get_permutations("234", mapping))
print(f_mapping2("234", mapping))
print(f_mapping("234", mapping))
