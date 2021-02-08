import numpy as np

def num_ways(n, m):
    A = np.zeros((n,m-1), int)
    A[0] = np.ones(m-1)
    A = np.hstack([np.ones((n,1),  int), A])
    print(n,m,'\n',A)
    for i in range(1, n):
        for j in range(1, m):
            A[i][j] = A[i - 1][j] + A[i][j - 1]
    return A

def num_ways1(n, m):
    if n == 1 or m == 1:
        return 1
    return num_ways1(n - 1, m) + num_ways1(n, m - 1)

def num_ways2(n, m):
    A = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        A[i][0] = 1
    for j in range(m):
        A[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            A[i][j] = A[i - 1][j] + A[i][j - 1]
    return A[-1][-1]

def num_ways3(n, m):
    i, j, k, r = 1, 1, 0, 0
    while (i != n) or (j != m):
        moved = False
        while not moved:
            if k:
                if j < m:
                    j += 1
                    moved = True
            else:
                if i < n:
                    i += 1
                    moved = True
            k = 1 -k
        r += 1
    return r       

             
for i in range(4,6):
    print(num_ways(i,i))
    print(num_ways2(i,i))
    #print(num_ways3(i,i))
    print(num_ways1(i,i))