"""
This is an interview question asked by Facebook.
Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input, write a function that shuffles a deck of cards represented as an array using only swaps.
"""
from random import randint

def shuffle(cards, k):
    for i in range(k):
        pos = i + randint(0,k-i-1)
        cards[i], cards[pos] = cards[pos], cards[i]

lst = [i for i in range(1,53)]
shuffle(lst,52)
print(lst)

