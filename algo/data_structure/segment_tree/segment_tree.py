def build_tree(tree, a, v, tl, tr):
    if tr - tl == 1 and tl < len(a):
        tree[v] = a[tl]
    else:
        tm = (tl + tr) // 2
        build_tree(tree, a, v * 2 + 1, tl, tm)
        build_tree(tree, a, v * 2 + 2, tm, tr)
        tree[v] = tree[v * 2 + 1] + tree[v * 2 + 2]


def sum_tree(tree, v, tl, tr, l, r):
    if l >= tr or tl >= r:
        return 0
    if tl >= l and tr <= r:
        return tree[v]
    tm = (tr + tl) // 2
    return sum_tree(tree, v * 2 + 1, tl, tm, l, r) + sum_tree(tree, v * 2 + 2, tm , tr, l, r)


def update_tree(tree, v, tl, tr, pos, new_val):
    if tr - tl == 1:
        tree[v] = new_val
        return
    else:
        tm = (tr + tl) // 2
        if pos < tm:
            update_tree(tree, v * 2 + 1, tl, tm, pos, new_val)
        else:
            update_tree(tree, v * 2 + 2, tm, tr, pos, new_val)

    tree[v] = tree[v * 2 + 1] + tree[v * 2 + 2]


def solve(): #####$######W########E ONLYT FOR INDEX 00000000000000 SUM WORKS FROM L TO R - 1`!@!!!!!!!!!!!!!!
    n, m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    tree = [0 for i in range(n * 4)]
    build_tree(tree, a, 0, 0, n)

    for _ in range(m):
        q = [int(i) for i in input().split()]
        if q[0] == 1:
            pos, val = q[1], q[2]
            update_tree(tree, 0, 0, n, pos, val)
        else:
            l, r = q[1], q[2]
            print(sum_tree(tree, 0, 0, n, l, r))


solve()
