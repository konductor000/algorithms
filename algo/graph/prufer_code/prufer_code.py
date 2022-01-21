def dfs(v):
    for i in range(len(g[v])):
        to = g[v][i]
        if parent[v] != to:
            parent[to] = v
            dfs(to)


def prufer_code():
    global parent, g
    n, m = [int(i) for i in input().split()]
    g = [[] for i in range(n + 1)]
    for i in range(m):
        x, y = [int(i) for i in input().split()]
        g[x].append(y)
        g[y].append(x)

    parent = [-1 for i in range(n + 1)]
    dfs(n)
    degree = [0 for i in range(n + 1)]
    ptr = -1
    for i in range(1, n + 1):
        degree[i] = len(g[i])
        if len(g[i]) == 1 and ptr == -1:
            ptr = i

    leaf = ptr
    result = []
    for i in range(n - 2):
        nxt = parent[leaf]
        result.append(nxt)
        degree[nxt] -= 1
        if degree[nxt] == 1:
            leaf = nxt
        else:
            ptr += 1
            while ptr < n and degree[ptr] != 1:
                ptr += 1
            leaf = ptr

    return result


def prufer_decode():
    code = prufer_code()
    print(code)
    n = len(code) + 2
    degree = [1 for i in range(n + 1)]

    for i in range(n - 2):
        degree[code[i]] += 1

    ptr = 0
    while ptr < n and degree[ptr] != 1:
        ptr += 1
    leaf = ptr

    result = []
    for i in range(n - 2):
        v = code[i]
        result.append([v, leaf])
        degree[leaf] -= 1
        degree[v] -= 1
        if degree[v] == 1 and v < ptr:
            leaf = v
        else:
            ptr += 1
            while ptr < n and degree[ptr] != 1:
                ptr += 1
            leaf = ptr

    for v in range(n - 1):
        if degree[v] == 1:
            result.append([v, n - 1])

    print(result)


prufer_decode()
