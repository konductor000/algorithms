def pdf(n, k):
	res = 0
	while n:
		n //= k
		res += n

	return res
