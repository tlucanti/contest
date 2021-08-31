
def solver(x, y, s):
	n = len(s)
	dp = [[0 for i in range(n)] for _ in range(2)]
	# 0 -> J
	# 1 -> C
	# x -> CJ
	# y -> JC
	if s[0] == 'C':
		dp[1][0] = None
	elif s[0] == 'J':
		dp[0][0] = None
	for i in range(1, n):
		if s[i] == '?' and s[i - 1] == '?':
			dp[0][i] = min(dp[0][i - 1], dp[1][i - 1] + y)
			dp[1][i] = min(dp[1][i - 1], dp[0][i - 1] + x)
		elif s[i - 1] == '?':
			if s[i] == 'C':
				dp[0][i] = min(dp[0][i - 1], dp[1][i - 1] + y)
				dp[1][i] = None
			else:
				dp[0][i] = None
				dp[1][i] = min(dp[1][i - 1], dp[0][i - 1] + x)
		elif s[i] == '?':
			if dp[0][i - 1] is not None:
				dp[0][i] = dp[0][i - 1]
				dp[1][i] = dp[0][i - 1] + x
			else:
				dp[0][i] = dp[1][i - 1] + y
				dp[1][i] = dp[1][i - 1]
		else:
			cc = s[i - 1:i + 1]
			if cc == 'CC':
				dp[0][i] = dp[0][i - 1]
				dp[1][i] = None
			elif cc == 'CJ':
				dp[0][i] = None
				dp[1][i] = dp[0][i - 1] + x
			elif cc == 'JC':
				dp[0][i] = dp[1][i - 1] + y
				dp[1][i] = None
			else:  # JJ
				dp[0][i] = None
				dp[1][i] = dp[1][i - 1]
	if dp[0][-1] is not None and dp[1][-1] is not None:
		ans = min(dp[0][-1], dp[1][-1])
	elif dp[0][-1] is not None:
		ans = dp[0][-1]
	else:
		ans = dp[1][-1]
	return ans


def solver_slow(x, y, s):
	q = s.count('?')
	s = list(s)
	qq = []
	n = len(s)
	ans = None
	for i in range(n):
		if s[i] == '?':
			qq.append(i)
	for i in range(pow(2, q)):
		b = bin(i)[2:]
		b = '0' * (q - len(b)) + b
		for j in range(q):
			s[qq[j]] = 'C' if b[j] == '1' else 'J'
		ans_s = ''.join(s)
		if ans is None:
			ans = ans_s.count('CJ') * x + ans_s.count('JC') * y
		else:
			ans = min(ans, ans_s.count('CJ') * x + ans_s.count('JC') * y)
	return ans

# for t in range(int(input())):
# 	x, y, s = input().split()
# 	x, y = int(x), int(y)
# 	print(solver_slow(x, y, s))
# afegrtb



from random import randint as r
for t in range(1000):
	x = r(-100, 100)
	y = r(-100, 100)
	s = []
	aa = ['C', 'J', '?']
	for i in range(20):
		s.append(aa[r(0, 2)])
	s = ''.join(s)

	# print(x, y, s)
	a1 = solver(x, y, s)
	a2 = solver_slow(x, y, s)
	if a1 != a2:
		print(x, y, s)
		print(a1, a2)
		print()
