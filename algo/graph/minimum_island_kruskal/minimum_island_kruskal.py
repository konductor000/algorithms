from random import random


def make_set(v):
	parent[v] = v


def find_set(v):
	if v == parent[v]: return v
	parent[v] = find_set(parent[v])
	return parent[v]


def union_set(a, b):
	a = find_set(a)
	b = find_set(b)
	if random() % 2:
		a, b = b, a

	if a != b:
		parent[b] = a



def solve():
	global parent
	res = []
	cost = 0
	n, m = [int(i) for i in input().split()]
	e = []
	for i in range(m):
		e.append([int(i) for i in input().split()])

	parent = [i for i in range(n + 1)]
	e.sort()

	for i in range(m):
		l, a, b = e[i][0], e[i][1], e[i][2]
		if find_set(a) != find_set(b):
			res.append([a, b])
			cost += l
			union_set(a, b)

	print(res, cost)


solve()

'''
6 7
100 1 2
1 1 3
1 2 4
1 3 4
1 4 5
1 4 6
100 5 6
'''
