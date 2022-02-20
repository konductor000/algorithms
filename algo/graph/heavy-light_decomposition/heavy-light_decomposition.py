def build_tree(tree, a, v, tl, tr):
    if tl == tr:
        tree[v] = a[tl]
    else:
        tm = (tl + tr) // 2
        build_tree(tree, a, v * 2, tl, tm)
        build_tree(tree, a, v * 2 + 1, tm + 1, tr)
        tree[v] = tree[v * 2] + tree[v * 2 + 1]


def tree_sum(tree, v, tl, tr, l, r):
    if l > r:
        return 0
    if l == tl and r == tr:
        return tree[v]
    tm = (tr + tl) // 2
    x = tree_sum(tree, v * 2, tl, tm, l, min(tm, r))
    y = tree_sum(tree, v * 2 + 1, tm + 1, tr, max(tm + 1, l), r)


def tree_update(tree, v, tl, tr, pos, new_val):
    if tl == tr:
        tree[v] = new_val
    else:
        tm = (tr + tl) // 2
        if pos <= tm:
            tree_update(tree, v * 2, tl, tm, pos, new_val)
        else:
            tree_update(tree, v * 2 + 1, tm + 1, tr, pos, new_val)

        tree[v] = tree[v * 2] + tree[v * 2 + 1]


def rqm(tree, v, tl, tr, l, r):
    if l > r:
        return 0
    if tl == l and tr == r:
        return tree[v]
    tm = (tl + tr) // 2
    m1 = rqm(tree, v, tl, tm, l, min(r, tm))
    m2 = rqm(tree, v, tm + 1, tr, max(tm + 1, tl), tr)

    return max(m1, m2)


def dfs_col(g, amounts, depth, parents, v, pr):
    amounts[v] = 1
    parents[v] = pr
    for to in g[v]:
        if to == pr:
            continue

        depth[to] = depth[v] + 1
        dfs_col(g, amounts, depth, parents, to, v)
        amounts[v] += amounts[to]


def dfs_heavy_light(a, poses, top, g, amounts, v, pr, tp):
    top[v] = tp
    poses[v] = len(a)
    a.append(v)
    ind = -1
    for to in g[v]:
        if to == pr:
            continue
        if ind == -1 or amounts[to] > amounts[ind]:
            ind = to

    if ind == -1:
        return

    dfs_heavy_light(a, poses, top, g, amounts, ind, v, tp)
    for to in g[v]:
        if to == pr or to == ind:
            continue
        dfs_heavy_light(a, poses, top, g, amounts, to, v, to)


def solve():
    n, m = [int(i) for i in input().split()]
    g = [[] for i in range(n + 1)]
    edges = []
    parents = [-1 for i in range(n + 1)]
    amounts = [0 for i in range(n + 1)]
    depth = [0 for i in range(n + 1)]
    poses = [0 for i in range(n + 1)]
    top = [-1 for i in range(n + 1)]
    a = []

    for i in range(n - 1):
        x, y, v = [int(i) for i in input().split()]
        edges.append([x, y, v])
        g[x].append(y)
        g[y].append(x)

    dfs_col(g, amounts, depth, parents, 1, -1)
    dfs_heavy_light(a, poses, top, g, amounts, 1, -1, 1)

    val = [0 for i in range(n + 1)]
    for i in edges:
        x, y, c = i[0], i[1], 0
        if depth[x] < depth[y]:
            i[0], i[1] = i[1], i[0]
            x, y = y, x

        val[x] = c

    tree = [0 for i in range(4 * len(val))]
    for i in range(1, n + 1):
        a[i] = val[a[i]]

    build_tree(tree, a, 1, 0, len(val) - 1)

    val2 = [0 for i in range(n + 1)]
    for i in range(m):
        q = [int(i) for i in input().split()]
        if q[0] == 1:
            posit, vl = q[1], q[2]
            val2[posit] += vl
            tree_update(tree, 1, 0, n, posit, vl)
        else:
            posit = q[1]
            print(val2[posit] - tree_sum(tree, 1, 0, n, posit, 1))


solve()
