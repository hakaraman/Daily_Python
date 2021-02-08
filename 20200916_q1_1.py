def matches_first_char(s, r):
    return  (r[0] == '.' and len(s) > 0) or s[0] == r[0]

def matches(s, r):
    if r == '':
        return s == ''

    if len(r) == 1 or r[1] != '*':
        # The first character in the regex is not proceeded by a *.
        if matches_first_char(s, r):
            return matches(s[1:], r[1:])
        else:
            return False
    else:
        # The first character is proceeded by a *.
        # First, try zero length.
        if matches(s, r[2:]):
            return True
        # If that doesn't match straight away, then try globbing more prefixes
        # until the first character of the string doesn't match anymore.
        i = 0
        while matches_first_char(s[i:], r):
            if matches(s[i+1:], r[2:]):
                return True
            i += 1

def FindMatch(text, pattern):
    if not pattern:
        return not text
    first_match = bool(text) and pattern[0] in {text[0], '.'}
    if len(pattern) >= 2 and pattern[1] == '*':
        return (FindMatch(text, pattern[2:]) or first_match and FindMatch(text[1:], pattern))
    else:
        return first_match and FindMatch(text[1:], pattern[1:])            

def f_match(text, pattern):
    i, j = 0, 0
    while i < len(text):
        if pattern[j] == '.' or pattern[j] == '*' or pattern[j] == text[i]:
            i += 1       
        else:
            return False
        if pattern:
            pass    

 

#s= "ray" 
#s= "raymond"
#r= "ra."
r= ".*at"
s= "chat"

print(FindMatch(s,r))