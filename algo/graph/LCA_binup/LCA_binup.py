def dfs(v, p, s):
    timer[0] += 1
    tin[v] = timer[0]
    up[v][0] = p
    for i in range(1, s + 1):
        up[v][i] = up[up[v][i - 1]][i - 1]
    for i in range(len(g[v])):
        to = g[v][i]
        if to != p:
            dfs(to, v, s)

    timer[0] += 1
    tout[v] = timer[0]


def upper(a, b):
    return tin[a] <= tin[b] and tout[a] >= tout[b]


def lca(a, b, l):
    if upper(a, b):
        return a

    if upper(b, a):
        return b

    for i in range(l, -1, -1):
        if not upper(up[a][i], b):
            a = up[a][i]

    return up[a][0]


def solve():
    global up, g, tin, tout, timer
    n = int(input())
    g = [[] for i in range(n + 1)]
    tin = [0 for i in range(n + 1)]
    tout = [0 for i in range(n + 1)]
    s = 1
    timer = [1]

    for i in range(n - 1):
        x, y = [int(i) for i in input().split()]
        g[x].append(y)
        g[y].append(x)

    while 1 << s <= n:
        s += 1

    up = [[0 for i in range(s + 1)] for j in range(n + 1)]

    dfs(1, 1, s)

    q = int(input())
    for i in range(q):
        a, b = [int(i) for i in input().split()]
        print(a, b, lca(a, b, s))


solve()

"""
14
1 2
1 3
2 4
4 6
2 5
5 7
5 8
3 9
9 14
3 10
10 11
11 12
11 13
4
14 12
14 3
5 6
7 8
"""
