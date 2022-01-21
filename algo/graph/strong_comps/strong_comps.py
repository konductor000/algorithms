def dfs1(v):
	for i in range(len(g[v])):
		to = g[v][i]
		if not used[to]:
			used[to] = 1
			dfs1(to)
	order.append(v)


def dfs2(v):
	comps.append(v)
	for i in range(len(g[v])):
		to = g[v][i]
		if not used[to]:
			used[to] = 1
			dfs2(to)


def solve():
	global comps, order, g, gr, used
	comps = []
	order = []
	n, m = [int(i) for i in input().split()]
	g = [[] for i in range(n + 1)]
	gr = [[] for i in range(n + 1)]
	used = [0 for i in range(n + 1)]

	for i in range(m):
		x, y = [int(j) for j in input().split()]
		g[x].append(y)
		gr[y].append(x)

	for i in range(1, n + 1):
		if not used[i]:
			used[i] = 1
			dfs1(i)

	used = [0 for i in range(n + 1)]
	for i in range(n, 0, -1):
		comps = []
		if not used[i]:
			used[i] = 1
			dfs2(i)
			print(*comps)

solve()
