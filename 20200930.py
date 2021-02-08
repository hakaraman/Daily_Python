"""
Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""
from math import inf

def maximum_product_of_three(lst):
    max1, max2, max3, min1, min2 = -inf, -inf, -inf, inf, inf

    for x in lst:
        if x > max1:
            max3 = max2
            max2 = max1
            max1 = x
        elif x > max2:
            max3 = max2
            max2 = x
        elif x > max3:
            max3 = x

        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2:
            min2 = x

    return max(max1 * max2 * max3, max1 * min1 * min2)

def maximum_product_of_three2(lst):
    lst.sort()
    third_largest, second_largest, first_largest = lst[-3], lst[-2], lst[-1]
    first_smallest, second_smallest = lst[0], lst[1]
    return max(third_largest * second_largest * first_largest,
    first_largest * first_smallest * second_smallest)

def max_product(lst):
    lst.sort(reverse = True)
    return max(lst[0]*lst[1]*lst[2], lst[0]*lst[-1]*lst[-2])


from math import inf

def max_product2(lst):
    maxn = [-inf, -inf, -inf, -inf]
    minn = [inf, inf, inf]
    for i in lst:
        for j in range(3):
            if i > maxn[j]:
                for k in range(j+1,3):
                    maxn[k] = maxn[k-1]
                maxn[j] = i
                break
        for j in range(2):
            if i < minn[j]:
                for k in range(j+1,2):
                    minn[k] = minn[k-1]
                minn[j] = i
                break
    return max(maxn[0]*maxn[1]*maxn[2], maxn[0]*minn[0]*minn[1])            

lst = [-10, -10, 5, 2, 0, 100, -100, 3]
print(maximum_product_of_three(lst))
print(maximum_product_of_three2(lst))
print(max_product(lst))
lst = [-10, -10, 5, 2, 0, 100, -100, 3]
print(max_product2(lst))