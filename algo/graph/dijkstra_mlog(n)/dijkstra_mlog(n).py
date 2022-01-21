from heapq import *


def solve():
    n, m = [int(i) for i in input().split()]
    g = [[] for i in range(n + 1)]
    h = []
    p = [-1 for i in range(n + 1)]
    heapify(h)
    inf = 10 ** 10
    d = [inf for i in range(n + 1)]
    for i in range(m):
        x, y, l = [int(i) for i in input().split()]
        g[x].append([l, y])
        g[y].append([l, x])

    s, s1 = [int(i) for i in input().split()]
    d[s] = 0
    h.append([0, s])

    while len(h):
        v = h[-1][1]
        cur_d = -h[-1][0]
        h.pop()
        if d[v] < cur_d:
            continue
        for i in range(len(g[v])):
            to, l = g[v][i][1], g[v][i][0]
            if d[v] + l < d[to]:
                d[to] = d[v] + l
                p[to] = v
                h.append([-d[to], to])

    if d[s1] == inf:
        print(-1)
    else:
        print(d[s1])


solve()

