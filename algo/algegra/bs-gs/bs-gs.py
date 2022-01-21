from math import sqrt


def bin_pow(a, b, m):
	res = 1
	while b:
		if b % 2:
			b -= 1
			res = res * a % m
		else:
			a = (a * a) % m
			b //= 2

	return res % m


def solve(a, b, m):
	n = int(sqrt(m)) + 1
	vals = {}
	for i in range(n, 0, -1):
		vals[bin_pow(a, i * n, m)] = i

	for i in range(n + 1):
		cur = (bin_pow(a, i, m) * b) % m
		if cur in vals:
			ans = vals[cur] * n - i

			if ans < m:
				return ans

	return -1


print(solve(3, 13, 17))
print(3 ** 4 % 17)