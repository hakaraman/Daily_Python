"""
On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0) (1, 2) (2, 2) (4, 0) The board would look like this:

[b 0 0 0 0] [0 0 b 0 0] [0 0 b 0 0] [0 0 0 0 0] [b 0 0 0 0] You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
"""
from collections import defaultdict

TOP_LEFT_TO_BOTTOM_RIGHT = 0
TOP_RIGHT_TO_BOTTOM_LEFT = 1

def combos(num):
    return num * (num - 1) / 2

def pairs(bishops, m):
    counts = defaultdict(int)
    for r, c in bishops:
        top_lr, top_lc = (r - min(r, c), c - min(r, c))
        top_rr, top_rc = (r - min(r, m - c), c + min(r, m - c))

        counts[top_lr, top_lc, TOP_LEFT_TO_BOTTOM_RIGHT] += 1
        counts[top_rr, top_rc, TOP_RIGHT_TO_BOTTOM_LEFT] += 1
    return sum(combos(c) for c in counts.values())

def is_attacking(bishop0, bishop1):
    r0, c0 = bishop0
    r1, c1 = bishop1
    return abs(r1 - r0) == abs(c1 - c0)

def pairs1(bishops, m):
    count = 0
    for i, bishop0 in enumerate(bishops):
        for j, bishop1 in enumerate(bishops[i + 1:]):
            count += is_attacking(bishop0, bishop1)
    return count

def check_bishops1(bishops, m):
    result = 0
    for i, bs1 in enumerate(bishops):
        for _, bs2 in enumerate(bishops[i+1:]):
            result += abs(bs2[0] - bs1[0]) == abs(bs2[1] - bs1[1])
    return result

def check_bishops(bishops, m):
    result = 0
    for i in range(len(bishops)):
        for j in range(len(bishops[i+1:])):
            result += abs(bishops[i+1+j][0] - bishops[i][0]) == abs(bishops[i+1+j][1] - bishops[i][1])
    return result

def check_bishops2(bishops, m):
    return sum([1 for i in range(len(bishops)) for j in range(len(bishops[i+1:])) if abs(bishops[i+1+j][0] - bishops[i][0]) == abs(bishops[i+1+j][1] - bishops[i][1])])

bishops = [(0, 0), (1, 2), (2, 2), (4, 0)]
print(pairs(bishops,5))
print(pairs1(bishops,5))
print(check_bishops2(bishops,5))