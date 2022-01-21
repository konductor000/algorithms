n, m = [int(i) for i in input().split()]

bl = [i for i in range(n + 1)]
comp = [i for i in range(n + 1)]
par = [-1 for i in range(n + 1)]
size = [1 for i in range(n + 1)]
bridges = 0
cu = 0
u = [0 for i in range(n + 1)]

for q in range(m):
	a, b = [int(i) for i in input().split()]
	add_edge(a, b)


def get(v):
	if v == -1: return -1
	if bl[v] == v: return v
	else:
		bl[v] = get(bl[v])
		return bl[v]


def get_comp(v):
	v = get(v)
	if comp[v] == v: return v
	else:
		comp[v] = get_comp(comp[v])
		return comp[v]


def make_root(v):
	v = get(v)
	root = v
	child = -1

	while v != -1:
		p = get(par[v])
		par[v] = child
		comp[v] = root
		child = v
		v = p

	size[root] = size[child]


def merge_path(a, b):
	cu += 1
	va = []
	vb = []
	lca = -1

	while True:
		if a != -1:
			a = get(a)
			va.append(a)
			if u[a] == a:
				lca = a
				break

			u[a] = a
			a = par[a]

		if b != -1:
			b = get(b)
			vb.append(b)
			if u[b] == b:
				lca = b
				break

			u[b] = b
			a = par[b]

	for i in range(len(va)):
		bl[va[i]] = lca
		if va[i] == lca:
			break
		bridges -= 1

	for i in range(len(vb)):
		bl[vb[i]] = lca
		if va[i] == lca:
			break
		bridges -= 1


def add_edge(a, b):
	a = get(a)
	b = get(b)
	if a == b:
		return
	ca = get_comp(a)
	cb = get_comp(b)

	if ca != cb:
		bridge += 1
		if size[ca] > size[cb]:
			ca, cb = cb, ca
			a, b = b, a

		make_root(a)
		par[a] = b
		comp[a] = b
		size[cb] += size[a]

	else:
		merge_path(a, b)

	print(bridges)
