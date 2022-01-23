def solve():
    n, m = [int(i) for i in input().split()]
    e = []
    inf = 10 ** 10
    d = [inf for i in range(n + 1)]
    p = [-1 for i in range(n + 1)]
    for j in range(m):
        e.append([int(i) for i in input().split()])  # a b l

    s, to = [int(i) for i in input().split()]
    d[s] = 0
    x = -1

    for i in range(n):
        change = 0
        # if i == n - 1 .. negative cycle exists
        x = -1
        for j in range(m):
            a, b, l = e[j][0], e[j][1], e[j][2]
            if d[a] < inf:
                if d[a] + l < d[b]:
                    change = 1
                    p[b] = a
                    d[b] = d[a] + l
                    x = b

        if not change:
            break

    if d[to] == inf:  # doesn't work if there is negative cycle
        print("No path!")
    else:
        path = []
        v = to
        while v != -1:
            path.append(v)
            v = p[v]

        path.reverse()
        print(path)

    # if you need to find negative cycle

    if x == -1:
        print("No negative cycle")
    else:
        path = []
        v = x
        for i in range(1, n + 1):
            v = p[v]

        cur = v
        while len(path) <= 1 or cur != v:
            path.append(cur)
            cur = p[cur]

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