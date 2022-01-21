def solve():
	n, m = [int(i) for i in input().split()]
	g = [[] for i in range(n + 1)]
	for j in range(m):
		l, a, b = [int(i) for i in input().split()]
		g[a].append([b, l])
		g[b].append([a, l])
	s = int(input())
	inf = 10 ** 10

	d = [inf for i in range(n + 1)]
	p = [-1 for i in range(n + 1)]
	u = [0 for i in range(n + 1)]
	d[s] = 0

	for i in range(n):
		v = -1
		for j in range(1, n + 1):
			if not u[j] and (v == -1 or d[j] < d[v]):
				v = j

		if d[v] == inf: break
		u[v] = 1

		for i in range(len(g[v])):
			to, l = g[v][i][0], g[v][i][1]
			if d[v] + l < d[to]:
				p[to] = v
				d[to] = d[v] + l

	path = []
	t = int(input())
	v = t
	while v != s:
		path.append(v)
		v = p[v]
	path.append(s)
	path.reverse()

	print(path)
	print(d[t])


