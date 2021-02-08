"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
"""
def convertToTitle(n):
    result = ""
    while n > 26:
        result = chr(65+(n-1)%26)  + result  
        n = (n-1) // 26
    return chr(64+n) + result  

def convertToTitle(n):
    result = ""
    n-=1
    while n > 25:
        result = chr(65+n%26)  + result  
        n = n // 26 - 1
    return chr(65+n) + result  

print(convertToTitle(701))