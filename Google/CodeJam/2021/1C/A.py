
def calc(a, b, p1, p2):
	if a > b or (a == b and p1 > p2):
		a, b = b, a
		p1, p2 = p2, p1
	if a + 1 == b and p1 == 1 and p2 == -1:
		return s[b] - s[a] - 1
	if a == 0 and p1 == -1:
		m1 = s[a] - 1
	elif a == n - 1 and p1 == +1:
		m1 = k - s[-1]
	else:
		m1 = abs(s[a] - s[a + p1]) // 2
	if b == n - 1 and p2 == +1:
		m2 = k - s[-1]
	else:
		m2 = abs(s[b] - s[b + p2]) // 2
	if a == b and p1 == p2:
		return m1
	else:
		return m1 + m2


for t in range(int(input())):
	n, k = map(int, input().split())
	s = list(map(int, input().split()))
	s = sorted(set(s))
	n = len(s)
	score = 0
	for i in range(n):
		if s[i] - 1 > 0:
			a = i
			p1 = -1
			for j in range(n):
				if s[j] - 1 > 0:
					b = j
					p2 = -1
					score = max(score, calc(a, b, p1, p2))
				if s[j] + 1 <= k:
					b = j
					p2 = +1
					score = max(score, calc(a, b, p1, p2))
		if s[i] + 1 < k:
			a = i
			p1 = +1
			for j in range(n):
				if s[j] - 1 > 0:
					b = j
					p2 = -1
					score = max(score, calc(a, b, p1, p2))
				if s[j] + 1 <= k:
					b = j
					p2 = +1
					score = max(score, calc(a, b, p1, p2))
		# print(score)

	print(f'Case #{t + 1}: {score / k}')
