import itertools


def prod(ar):
	s = 1
	for i in ar:
		s *= i
	return s


def next(s):
	s[0] += 1
	for i in range(len(s)):
		if s[i] > p[i][1]:
			s[i] = 0
			if i < len(s) - 1:
				s[i + 1] += 1
			else:
				return 0
		else:
			break
	return 1


for t in range(int(input())):
	m = int(input())
	if m == 0:
		print(f'Case #{t + 1}: {0}')
		continue
	p = []
	for i in range(m):
		pr, n = map(int, input().split())
		p.append((pr, n))
	ans = 0
	s = [0 for i in range(m)]
	while 1:
		# print(s)
		l = 0
		r = 1
		for i in range(len(s)):
			l += s[i] * p[i][0]
			r *= pow(p[i][0], p[i][1] - s[i])
		if l == r:
			ans = max(l, ans)
		if next(s) == 0:
			break
	print(f'Case #{t + 1}: {ans}')


# for t in range(int(input())):
# 	m = int(input())
# 	nums = []
# 	for i in range(m):
# 		p, n = map(int, input().split())
# 		nums.append((p, n))
# 	ans = 0
# 	for s in itertools.permutations(ar):
# 		for i in range(len(s)):
# 			l = s[:i]
# 			r = s[i:]
# 			sm = sum(l)
# 			if sm == prod(r):
# 				l_max = l
# 				r_max = r
# 				ans = max(ans, sm)
# 	# print(*l_max)
# 	# print(*r_max)
# 	print(f'Case #{t + 1}: {ans}')
