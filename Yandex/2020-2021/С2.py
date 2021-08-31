def idxsum(x, f, left, right):
	__sm = 0
	for __i in range(left, right):
		__sm += abs(x[__i][0] - f)
	return __sm


n, k = map(int, input().split())
_s = list(map(int, input().split()))
s = [[]] * n
for i in range(n):
	s[i] = [_s[i], i]
s.sort(key=lambda x: x[0])
for i in range(n):
	if i < n // 2:
		l = max(i - k//2 - k%2, 0)
		r = l + k + 1
	else:
		r = min(i + k + 1, n)
		l = r - k - 1
	f1 = idxsum(s, s[i][0], l, r)
	if i < n//2:
		l = max(i - k//2, 0)
		r = l + k + 1
	else:
		r = min(i + k + 1 + k%2, n)
		l = r - k - 1
	f2 = idxsum(s, s[i][0], l, r)
	f = min(f1, f2)
	print(f, end=' ')
print()