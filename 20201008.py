"""
This is an interview question asked by Two Sigma.
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""
from random import randint

def rand7():
    return randint(1,7)

def rand5():
    x = rand7()
    return x if 1 <= x <= 5 else rand5()

def rand5x():
    r = rand7()
    if 1 <= r <= 5:
        return r
    return rand5()

print(rand5())