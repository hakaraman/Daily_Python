"""
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

def sum_of_digits(n):
    current_sum = 0
    while n > 0:
        current_sum += n % 10
        n = n // 10
    return current_sum

def perfect(n):
    i, current = 0, 0
    while current < n:
        i += 1
        if sum_of_digits(i) == 10:
            current += 1
    return i

def find_perfect_num1(n):
    x = n // 10 + 1
    return (n+x) * 9 + 1

def find_perfect_num(n):
    number, count = 0, 0
    while count < n:
        number += 1
        if sum([int(i) for i in str(number)]) == 10:
            count += 1
    return number

def find_perfect_num2(n):
    number, count = 10, 0
    while count < n:
        number += 9
        if sum([int(i) for i in str(number)]) == 10:
            count += 1
    return number

import math 

def find_perfect_num3(n):  
    nthElement = 19 + (n - 1) * 9
    outliersCount = int(math.log10(nthElement)) - 1
    # find the nth perfect number  
    nthElement += 9 * outliersCount  
    return nthElement  


for i in range(10,110):
    x = perfect(i)
    print(i, x)
    print(find_perfect_num2(i))
    print(find_perfect_num3(i))
    #print(i, x // 9)