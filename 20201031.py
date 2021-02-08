"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""
import pandas as pd
from random import randint
import random


def rand5():
    return randint(1,5)

def rand7():
    x = 5*(rand5()-1) + rand5() - 1 
    return x % 7 + 1  if x < 21 else rand7()

def rand7z():
    x = rand5() + rand5() - 1
    return x if 1 <= x <= 7 else rand7()

d= {}
for i in range(100000):
  # a = (5*(rand5()-1) + rand5() - 1 )%7+1  
  a=(rand5() + rand5() + rand5()+ rand5())%7+1
  if a in d:
      d[a] += 1
  else: 
      d[a] = 1
x = dict(sorted(d.items(),key=lambda x:x[0]))
df3 = pd.DataFrame.from_dict(x, orient="index")
df3.plot(kind='bar')

print(rand7())
print(x)