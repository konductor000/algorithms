def solve():
    n = int(input())
    a = [[int(i) for i in input().split()] for j in range(n)]
    x = []

    for i in range(n):
        x.append([a[i][0], 0])
        x.append([a[i][1], 1])
    x.sort()

    res = 0
    c = 0
    for i in range(2 * n - 1):
        if x[i][1] == 1:
            c -= 1
        else:
            c += 1

        if c == 0:
            res += x[i + 1][0] - x[i][0]

    print(res)


solve()
