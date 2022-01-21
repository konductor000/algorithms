def binpow(a, n):
	if n == 0:
		return 1
	if n % 2 == 1:
		return binpow(a, n - 1) * a
	else:
		b = binpow(a, n // 2)
		return b * b

for i in range(11):
	print(binpow(2, i))
