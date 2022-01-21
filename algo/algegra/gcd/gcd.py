def gcd(a, b):
	if b == 0:
		return a

	return gcd(b, a % b)

for i in range(5, 10):
	for j in range(10, 20):
		print(i, j, gcd(i, j))
