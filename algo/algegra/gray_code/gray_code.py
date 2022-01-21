def gray_code(g):
	return g ^ (g >> 1)


def rev_gray(g):
	n = 0
	while g:
		g >>= 1
		n ^= g
	return n


for i in range(1, 10):
	print(i, gray_code(i), rev_gray(i))
