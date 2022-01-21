def solve():
    n, m = [int(i) for i in input().split()]
    a = [[0 for i in range(n)] for j in range(n)]
    eps = 10 ** -9

    for i in range(m):
        x, y = [int(i) for i in input().split()]
        x -= 1
        y -= 1
        a[x][y] -= 1
        a[y][x] -= 1

    for i in range(n):
        for j in range(n):
            if i == j: continue
            a[i][i] += -a[i][j]

    for i in range(n):
        a[i].pop()
    a.pop()
    n -= 1

    det = 1

    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[k][i]):
                k = j

        if abs(a[k][i]) < eps:
            det = 0
            break

        a[i], a[k] = a[k], a[i]
        if i != k:
            det = -det
        det *= a[i][i]

        for j in range(i + 1, n):
            a[i][j] /= a[i][i]
        for j in range(n):
            if j != i and a[j][i] > eps:
                for k in range(i + 1, n):
                    a[j][k] -= a[i][k] * a[j][i]

    print(det)


solve()
