from collections import deque


def solve():
    n, m = [int(i) for i in input().split()]
    g = [[] for i in range(n + 1)]
    inf = 10 ** 10
    d = [inf for i in range(n + 1)]
    p = [-1 for i in range(n + 1)]
    id = [0 for i in range(n + 1)]
    q = deque()

    for i in range(m):
        x, y, l = [int(i) for i in input().split()]
        g[x].append([l, y])

    s, s1 = [int(i) for i in input().split()]
    d[s] = 0
    q.append(s)

    while len(q):
        v = q.popleft()
        id[v] = 1
        for i in range(len(g[v])):
            to, l = g[v][i][1], g[v][i][0]
            if d[v] + l <= d[to]:
                d[to] = d[v] + l
                if id[to] == 0:
                    q.append(to)
                elif id[to] == 1:
                    q.appendleft(to)
                p[to] = v
                id[to] = 1

    print(d[s1])


solve()
