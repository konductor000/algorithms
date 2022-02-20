from random import randint


def find_set(v):
    if parent[v] == v:
        return v
    parent[v] = find_set(parent[v])
    return parent[v]


def union_set(a, b, new_anc):
    a = find_set(a)
    b = find_set(b)
    if randint(0, 1):
        a, b = b, a
    parent[a] = b
    ancestor[b] = new_anc


def dfs(v):
    parent[v] = v
    ancestor[v] = v
    used[v] = 1
    for i in range(len(g[v])):
        to = g[v][i]
        if not used[to]:
            dfs(to)
            union_set(v, to, v)

    for i in range(len(q[v])):
        if used[q[v][i]]:
            print(q[v][i], v, ancestor[find_set(q[v][i])])


def solve():
    global g, q, used, parent, ancestor
    n = int(input())
    g = [[] for i in range(n + 1)]
    parent = [0 for i in range(n + 1)]
    used = [0 for i in range(n + 1)]
    ancestor = [0 for i in range(n + 1)]
    q = [[] for i in range(n + 1)]

    for i in range(n - 1):
        x, y = [int(i) for i in input().split()]
        g[x].append(y)
        g[y].append(x)

    m = int(input())
    for i in range(m):
        a, b = [int(i) for i in input().split()]
        q[a].append(b)
        q[b].append(a)

    dfs(1)


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
