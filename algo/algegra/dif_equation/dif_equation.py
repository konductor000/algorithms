def extended_gcd(a, b):
	if a == 0:
		return b, 0, 1
	else:
		d, x, y = extended_gcd(b % a, a)
		return (d, y - (b // a) * x, x)


def solve(a, b, c):
	g = extended_gcd(a, b)[0]
	if c % g != 0:
		return -1
	x = c // g
	if a < 0: x *= -1
	y = c // g
	if a < 0: x *= -1
	return x, y


print(solve(4, 12, 68))

print(4 * 17 + 4 * 17)