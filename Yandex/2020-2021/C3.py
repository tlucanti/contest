def setsum(f, i):
	_k = k
	sm = 0
	l = i - 1
	r = i + 1
	while _k:
		if l < 0:
			sm += abs(f - s[r][0])
			r += 1
		elif r >= n:
			sm += abs(f - s[l][0])
			l -= 1
		else:
			if abs(f - s[r][0]) > abs(f - s[l][0]):
				sm += abs(f - s[l][0])
				l -= 1
			else:
				sm += abs(f - s[r][0])
				r += 1
		_k -= 1
	return sm

n, k = map(int, input().split())
_s = list(map(int, input().split()))
s = [[]] * n
for i in range(n):
	s[i] = [_s[i], i]
s.sort(key=lambda x: x[0])

F = [0] * n
for i in range(n):
	f = setsum(s[i][0], i)
	F[s[i][1]] = f
print(*F)
