"""
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""
def f_subsets1(s):
    result = []
    for i in s:
        result += [j + [i] for j in result]
        result.append([i])
    return [[]] + sorted(result, key = len)

def f_subsets(s):
    result = []
    for i in s:
        result += [j.union({i}) for j in result]
        result.append({i})
    return [{}] + sorted(result, key = len)

def f_subsets2(s):
    return [[s[j] for j in range(len(s)) if i & (1 << j)] for i in range(2**len(s))]

def findPowerSet(S):

	# N stores total number of subsets
	N = int(pow(2, len(S)))
	s = set()

	# generate each subset one by one
	for i in range(N):
		# check every bit of i
		for j in range(len(S)):
			# if j'th bit of i is set, print S[j]
			if i & (1 << j):
				s.add(S[j])

		print(list(s))
		s.clear()

from itertools import combinations

newlist = [[]]
l = [1,2,3]
for i in range(1,len(l)+1):
    c = combinations(l,i)
    for i in c:
        newlist.append(list(i))
print(newlist)

s = {1, 2, 3}
print(f_subsets(s))
print(f_subsets2(list(s)))
#findPowerSet(list(s))

