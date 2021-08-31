
def inv(s):
	ss = ''
	if s[0] == '0':
		ss += '1'
	else:
		ss += '0'
	if s[1] == '0':
		ss += '1'
	else:
		ss += '0'
	return ss


for t in range(int(input())):
	n = int(input())
	a = input()
	b = input()
	if n % 2:
		if a[-1] != b[-1]:
			print('NO')
			continue
		a = a[:-1]
		b = b[:-1]
		n -= 1
		if n == 0:
			print('YES')
			continue

	# zeros, ones
	o = [[] for i in range(n // 2)]
	inverts = 0
	a_ = []
	b_ = []
	for i in range(n // 2):
		a_.append(a[i * 2:i * 2 + 2])
		b_.append(b[i * 2:i * 2 + 2])
	a = a_
	b = b_
	o[0] = a[0].count('0'), a[0].count('1')
	for i in range(1, len(a)):
		o[i] = o[i - 1][0] + a[i].count('0'), o[i - 1][1] + a[i].count('1')
	ans = 'YES'
	for i in range(len(a) - 1, -1, -1):
		if a[i] == b[i] and inverts % 2 == 0:
			continue
		if inv(a[i]) == b[i] and inverts % 2:
			continue
		elif inv(a[i]) == b[i] and inverts % 2:
			continue
		elif (inv(a[i]) == b[i] and inverts % 2 == 0) or (a[i] == b[i] and inverts % 2):
			if o[i][0] == o[i][1]:
				inverts += 1
				continue
			else:
				ans = 'NO'
				break
		else:
			ans = 'NO'
			break
	print(ans)
