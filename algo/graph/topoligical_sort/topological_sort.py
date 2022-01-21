g = [
	[],
	[2, 3],
	[1],
	[2, 5],
	[4],
]

used = [0 for i in range(len(g))]
ans = []

def dfs(v):
	for i in range(len(g[v])):
		to = g[v][i]
		if not used[to]:
			dfs(to)
	ans.append(v)

dfs(1)
ans.reverse()
print(ans)
