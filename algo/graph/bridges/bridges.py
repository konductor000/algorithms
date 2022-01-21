def dfs(v, p, timer):
	used[v] = 1
	tin[v] = timer
	fup[v] = timer
	timer += 1
	for i in range(len(g[v])):
		to = g[v][i]
		if to == p:
			continue
		if used[to]:
			fup[v] = min(fup[v], tin[to])
		else:
			dfs(to, v, timer)
			fup[v] = min(fup[v], fup[to])
			if fup[to] > tin[v]:
				ans.append([v, to])


def solve():
	global n, m, g, used, tin, fup, ans, timer
	n, m = [int(i) for i in input().split()]
	g = [[] for i in range(n + 1)]
	used = [0 for i in range(n + 1)]
	tin = [0 for i in range(n + 1)]
	fup = [0 for i in range(n + 1)]
	timer = 1
	ans = []

	for i in range(m):
		x, y = [int(i) for i in input().split()]
		g[x].append(y)
		g[y].append(x)

	for i in range(1, n + 1):
		if not used[i]:
			dfs(i, -1, timer)

	print(ans)


solve()
