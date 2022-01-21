def euler_func(n):
	result = n
	i = 2
	while i * i <= n:
		if n % i == 0:
			while n % i == 0:
				n //= i
			result -= result // i
		i += 1

	if n > 1:
		result -= result // n

	return result


for i in range(1, 11):
	print(euler_func(i))
