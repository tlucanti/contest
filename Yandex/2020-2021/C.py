n, k = map(int, input().split())
_s = list(map(int, input().split()))
s = [[]] * n
for i in range(n):
	s[i] = [_s[i], i]
s.sort(key=lambda x: x[0])
cumsum = [0] * n
cumsum[0] = s[0][0]
for i in range(1, n):
	cumsum[i] = cumsum[i - 1] + s[i][0]
F = []
for i in range(n):
	l = i - k//2 - k%2
	r = i + k//2
	if l < 0:
		r += abs(l)
	l -= 1
	f = 
	f = (0 if l < 0 else cumsum[l]) - cumsum[r] - s[i][0]
	F.append(f)
print(*F)
