def solve():
    n, m = [int(i) for i in input().split()]
    e = []
    inf = 10 ** 10
    d = [inf for i in range(n + 1)]
    p = [-1 for i in range(n + 1)]
    for i in range(m):
        e.append([int(i) for i in input().split()])

    s, to = [int(i) for i in input().split()]
    d[s] = 0

    for i in range(n):
        if i == n - 1:
            print(-1)
            return
        change = 0
        for j in range(m):
            a, b, l = e[j][0], e[j][1], e[j][2]
            if d[a] < inf:
                if d[a] + l < d[b]:
                    change = 1
                    p[b] = a
                    d[b] = d[a] + l

        if not change:
            break

    if d[to] == inf:
        print(-2)
        return
    path = []
    v = to
    while v != -1:
        path.append(v)
        v = p[v]

    path.reverse()
    print(path)


solve()

"""
5 7
1 4 15
2 3 3
1 2 2
1 5 4
5 3 1 
3 4 1
2 4 3
1 4
"""