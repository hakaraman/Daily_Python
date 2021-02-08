from collections import defaultdict

def num_encodings1(s):
    # On lookup, this hashmap returns a default value of 0 if the key doesn't exist
    # cache[i] gives us # of ways to encode the substring s[i:]
    cache = defaultdict(int)
    cache[len(s)] = 1 # Empty string is 1 valid encoding

    for i in reversed(range(len(s))):
        if s[i].startswith('0'):
            cache[i] = 0
        elif i == len(s) - 1:
            cache[i] = 1
        else:
            if int(s[i:i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]

def num_encodings(s):
    if s.startswith('0'):
        return 0
    elif len(s) <= 1: 
        return 1

    total = 0

    if int(s[:2]) <= 26:
        total += num_encodings(s[2:])

    total += num_encodings(s[1:])
    return total

def numDecodings(s: str) -> int:  
    return numDecodingsHelper(s,len(s))  
  
def numDecodingsHelper(s:str, n:int) -> int:  
    if n == 0 or n == 1 :  
        return 1
    count = 0
    if s[n-1] > "0":  
        count = numDecodingsHelper(s,n-1)  
    if (s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7') ) :  
        count += numDecodingsHelper(s, n - 2)  
    return count

def num_encodings2(s):    
    if len(s) == 0:
        return 1
        
    result = 0    
    if int(s[:2]) in range(10,27):
        result += num_encodings2(s[2:])
    result += num_encodings2(s[1:])
    return result 

def num_encodings3(s):  
    lst = [0] * (len(s) + 1)
    lst[0], lst[1] = 1, 1
  
    for i in range(2, len(s) + 1):  
        lst[i] = 0
        if (s[i-1] > '0'):  
            lst[i] = lst[i-1]
        if (s[i-2] == '1' or (s[i-2] == '2' and s[i-1] < '7')):  
            lst[i] += lst[i-2]  
    return lst[-1] 

lst = ['1111', '121','1234', '12345','10000000']
for i in lst:
    print(i, num_encodings(i))
    print(i, num_encodings1(i))
    print(i, numDecodings(i))
    print(i, num_encodings3(i))

