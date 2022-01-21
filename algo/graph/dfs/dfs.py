g = [
	[],
	[2, 3],
	[1],
	[2, 5],
	[4],
]

v = 1
d = [0 for i in range(len(g))]
p = [-1 for i in range(len(g))]
used = [0 for i in range(len(g))]
used[v] = 1


def dfs(v, l):
	for i in range(len(g[v])):
		to = g[v][i]
		if not used[to]:
			used[to] = 1
			if l != -1:
				d[v] = d[l] + 1
				p[v] = v


dfs(v, -1)


