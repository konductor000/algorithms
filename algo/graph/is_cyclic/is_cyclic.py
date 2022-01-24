def dfs(v, anc):
    cl[v] = 1
    for i in range(len(g[v])):
        to = g[v][i]
        if to == anc: continue

        if cl[to] == 0:
            p[to] = v
            if dfs(to, v): return True

        else:
            cycle_st[0] = v
            cycle_end[0] = to
            return True

    cl[v] = 2
    return False


def solve():
    global g, cl, p, cycle_st, cycle_end
    n, m = [int(i) for i in input().split()]
    g = [[] for i in range(n + 1)]
    p = [-1 for i in range(n + 1)]
    cl = [0 for i in range(n + 1)]
    cycle_st = [-1]
    cycle_end = [-1]

    for i in range(m):
        x, y = [int(i) for i in input().split()]
        g[x].append(y)
        g[y].append(x)

    for i in range(1, n + 1):
        if not cl[i]:
            if dfs(i, -1):
                break

    cycle_end = cycle_end[0]
    cycle_st = cycle_st[0]

    if cycle_st == -1:
        print("Acyclic!")
        return

    path = []
    v = cycle_st
    while v != cycle_end:
        path.append(v)
        v = p[v]

    path.append(cycle_end)
    path.reverse()

    print(*path)


solve()
