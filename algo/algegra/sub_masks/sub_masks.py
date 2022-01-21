m = 41
s = m
while s > 0:
	print(s)
	s = (s - 1) & m


print("-------")

n = 3

m = 0
while m < (1 << n):
	s = m
	while s > 0:
		print(s)
		s = (s - 1) & m
	m += 1
