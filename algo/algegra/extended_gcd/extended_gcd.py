def extended_gcd(a, b):
	if a == 0:
		return b, 0, 1
	else:
		d, x, y = extended_gcd(b % a, a)
		return (d, y - (b // a) * x, x)

a = extended_gcd(426, 334)
print(f'Делитель равен {a[0]}, x = {a[1]}, y = {a[2]}')
 