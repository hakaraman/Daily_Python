def isvalid(text):
    pairsopen = {'(':')', '[':']','{':'}'}
    pairsclose = {')':'(', ']':'[','}':'{'}
    match = {'(':0, '[':0,'{':0}
    for i in text:
        if i in pairsopen.keys():
            match[i] += 1
        elif i in pairsclose.keys():
            if match[pairsclose[i]] > 0:
                match[pairsclose[i]] -= 1
            else:
                return False #parantez açılmadan kapanmış
        else:
            return False #geçersiz karakter     
    return True if sum(match.values()) == 0 else False

def checkform(text):
    pairs = {')':'(', ']':'[','}':'{'}
    que = []
    for i in text:
        if i in pairs.values():
            que.append(i)
        elif i in pairs.keys():
            if que[-1] == pairs[i]:
                que.pop(-1)
            else:
                return False #parantez açılmadan kapanmış
        else:
            return False #geçersiz karakter     
    return False if que else True #que de eleman varsa False

def is_wellformed(data):
    lst = [i for i in ["()","{}","[]"] if i in data]
    while lst:
        for i in lst:
            data = data.replace(i,"")
        lst = [i for i in ["()","{}","[]"] if i in data]
    return not bool(data)

def checkform1(text):
    pairs = {')':'(', ']':'[','}':'{'}
    que = [] 
    for i in text: 
        if i in pairs.values():
            que.append(i) 
        elif (i in pairs.keys()) and que and (que[-1] == pairs[i]):
            que.pop(-1)
        else:
            return False 
    return False if que else True 

def checkform3(text):
    lst = [i for i in ["()","{}","[]"] if i in text]
    while lst:
        for i in lst:
            text = text.replace(i,"")
        lst = [i for i in ["()","{}","[]"] if i in text]
    return not bool(text)    

from collections import deque
def checkform4(s):
    pairs = {')':'(', ']':'[','}':'{'}
    que = deque()
    for i in s:
        if (i in pairs.keys()) and que and (que[-1] == pairs[i]):
            que.pop()
        else:
            que.append(i)
    return len(que) == 0 

s = ["([)]", "([])", "((()[]{()})())"]

for i in s:
    print(i, is_wellformed(i))
    print(i, checkform4(i))
