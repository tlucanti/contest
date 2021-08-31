
for t in range(int(input())):
	a, b = map(int, input().split())
	s = list(input())
	n = len(s)
	a -= s.count('0')
	b -= s.count('1')
	if a < 0 or b < 0:
		print(-1)
		continue
	for i in range(n):
		if s[i] == '?':
			s[i] = s[n - i - 1]
			if s[i] == '0':
				a -= 1
			elif s[i] == '1':
				b -= 1
			else:
				s[i] = '*'
	if a < 0 or b < 0:
		print(-1)
		continue
	for i in range(n):
		if i == n // 2 and n % 2:
			continue
		if s[i] == '*':
			if a >= 2:
				s[i] = '0'
				s[n - i - 1] = '0'
				a -= 2
			else:
				s[i] = '1'
				s[n - i - 1] = '1'
				b -= 2
	if s[n // 2] == '*':
		if a > 0:
			s[n // 2] = '0'
			a -= 1
		else:
			s[n // 2] = '1'
			b -= 1
	if a != 0 or b != 0:
		print(-1)
	else:
		if s != s[::-1]:
			print(-1)
		else:
			print(''.join(s))