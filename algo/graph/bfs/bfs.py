from collections import deque


g = [
	[],
	[2, 3],
	[1],
	[2, 5],
	[4],
]

v = 1

q = deque()

q.append(v)
used = [0 for i in range(len(g))]
used[v] = 1

while len(q):
	v = q.pop()
	for i in range(len(g[v])):
		to = g[v][i]
		if not used[to]:
			used[to] = 1
			q.append(to)



