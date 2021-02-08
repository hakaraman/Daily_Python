"""
Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.
For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""

def m_profit(prices):
    result = 0
    for i in range(len(prices)-1):
        result = max(result, max(prices[i+1:]) - prices[i])
    return result

def m_profit2(prices):       
    return 0 if len(prices) < 2 else max(0,max([max(prices[i+1:]) - prices[i] for i in range(len(prices)-1)]))

def m_profit6(prices):
    result = 0
    for i in range(len(prices)-1):
        temp = max(prices[i+1:]) - prices[i]
        if temp > result:
            result = temp
    return result

def m_profit4(prices):
    result = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            temp = prices[j] - prices[i]
            if temp > result:
                result = temp
    return result

def m_profit5(prices):
    result = 0
    sell = 0
    for i in range(len(prices)-1,-1,-1):
        if sell < prices[i]:
            sell = prices[i]
        if sell - prices[i] > result:
            result = sell - prices[i]
    return result

def m_profit3(prices):
    result = 0
    sell = 0
    for i in range(len(prices)-1,-1,-1):
        sell = max(sell, prices[i])
        result = max(result, sell - prices[i])
    return result

def m_profit7(prices):
    result = 0
    buy = float("inf")
    for i in prices:
        buy = min(buy, i)
        result = max(result, i - buy)
    return result

lst = [9, 11, 8, 5, 7, 10]

# maxdif = 0
# for i in range(len(lst)):
# 	for y in range(len(lst)):
# 		if lst[y]-lst[i] > maxdif and y > i:
# 			maxdif = lst[y]-lst[i]            
# print(maxdif)

print(m_profit7(lst))