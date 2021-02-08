def find_longest(s, k):
    for i in range(len(s),1,-1):
        for j in range(0,len(s)-i):
            if len(set(s[j:i])) == k:
                return len(s[j:i])
    return None

def find_longest2(s, k):
    temp = [len(s[j:i]) for i in range(len(s),1,-1) for j in range(0,len(s)-i) if len(set(s[j:i])) == k]
    return temp[0] if temp != [] else None

def longest_substr(s, k):
    current_longest = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if len(set(substring)) <= k and len(substring) > len(current_longest):
                current_longest = substring
    return len(current_longest)

s = "abcbdbdbbdcdabd"
for i in range(7,1,-1):
    print(i, find_longest2(s,i))
