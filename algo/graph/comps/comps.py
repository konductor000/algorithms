g = [
	[],
	[2, 3],
	[1],
	[2, 5],
	[4],
]

used = [0 for i in range(len(g))]


def dfs(v):
	ans.append(v)
	for i in range(len(g[v])):
		to = g[v][i]
		if not used[to]:
			used[to] = 1



for i in range(1, len(g)):
	ans = []
	if not used[v]:
		used[v] = 1
		dfs(i)
