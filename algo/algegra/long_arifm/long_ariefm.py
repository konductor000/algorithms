base = 10 ** 9
a = []

def print_num(a):
	if len(a): print("0" * (9 - len(a[-1])) + str(a[-1]), end="")
	else: print("0")

	for i in range(len(a) - 2, 0, -1):
		print("0" * (9 - len(a[i])) + str(a[i]), end="")

	print()

def read_num(s):
	num = []

	for i in range(len(s), 0, -9):
		if i < 9:
			num.append(int(s[i:0]))
		else:
			num.append(int(s[i:i-9]))


def addition(a, b):
	carry = 0
	i = 0
	while i < max(len(a), len(b)) or carry:
		if i == len(a):
			a.append(0)
		a[i] += carry
		if i < len(b): a[i] += b[i]
		carry = a[i] >= base
		if carry:
			a[i] -= base
		i += 1


def substruction(a, b):
	carry = 0
	i = 0
	while i < len(b) or carry:
		a[i] -= carry
		if i < len(b): a[i] -= b[i]
		carry = a[i] < 0
		if carry:
			a[i] += base
		i += 1

	while len(a) > 1 and a[-1] == 0:
		a.pop()


def multiplication(a, b):
	carry = 0
	i = 0
	while i < len(a) or carry:
		if i == len(a):
			a.append(0)
		cur = carry + a[i] * b
		a[i] = cur % base
		carry = cur // base
	i += 1

	while len(a) > 1 and a[-1] == 0:
		a.pop()


def hard_multiplication(a, b):
	c = [0 for i in range(len(a) + len(b))]
	for i in range(len(a)):
		carry = 0
		j = 0
		while j < len(b) or carry:
			cur = c[i + j] + carry
			if j < len(b):
				cur += a[i] * b[j]
			carry = cur // base
			c[i + j] = cur % base
			j += 1

	while len(c) > 1 and c[-1] == 0:
		c.pop()


def division(a, b):
	carry = 0
	for i in range(len(a) - 1, -1, -1):
		cur = a[i] + carry * base
		a[i] = cur // b
		carry = cur % b

	while len(a) > 1 and a[-1] == 0:
		a.pop()











































