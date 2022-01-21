def sieve(n):
	s = [1 for i in range(n + 1)]
	s[0], s[1] = 0, 0
	i = 2
	while i * i <= n:
		if s[i] == 1:
			j = i * i
			while j <= n:
				s[j] = 0
				j += i
		i += 1

	return s

print(sieve(20))
