def solve():
    n, m = [int(i) for i in input().split()]
    inf = 10 ** 10
    d = [[inf if i != j else 0 for i in range(n + 1)] for j in range(n + 1)]

    for i in range(m):
        a, b, l = [int(i) for i in input().split()]
        d[a][b] = l

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if d[i][k] < inf and d[k][j] < inf:
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    q = int(input())
    for j in range(q):
        v, to = [int(i) for i in input().split()]
        print(d[v][to])


solve()

"""
4 5
1 2 1
1 3 3
2 3 1
2 4 7
3 4 1
3 
1 2 
1 3
2 4
"""