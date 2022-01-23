def solve():
    global gr, g, path
    n, m = [int(i) for i in input().split()]
    g = [[0 for j in range(n + 1)] for i in range(n + 1)]
    deg = [0 for i in range(n + 1)]

    for i in range(m):
        x, y = [int(i) for i in input().split()]
        g[x][y] = 1
        g[y][x] = 1

    for i in range(n + 1):
        for j in range(n + 1):
            deg[i] += g[i][j]

    first = 0
    while not deg[first]:
        first += 1

    v1 = -1
    v2 = -1
    for i in range(1, n + 1):
        if deg[i] % 2:
            if v1 == -1:
                v1 = i
            elif v2 == -1:
                v2 = i
            else:
                print("no solution!")
                return

    if v1 != -1:
        g[v1][v2] += 1
        g[v2][v1] += 1

    res = []
    st = [first]

    while len(st):

        v = st[-1]
        i = 1
        while i < n + 1:
            if g[v][i]:
                break
            i += 1

        if i == n + 1:
            res.append(v)
            st.pop()
        else:
            g[v][i] = 0
            g[i][v] = 0
            st.append(i)

    if v1 != -1:
        for i in range(len(res) - 1):
            if (res[i] == v1 and res[i + 1] == v2) or (res[i] == v2 and res[i + 1] == v1):
                res = res[i + 1:] + res[1:i]
                break

    for i in g:
        if sum(i):
            print("no solution!")
            return

    print(*res)
    # ans gives n + 1 nums (first number of domino and the last element is the second element of last domino)


solve()
