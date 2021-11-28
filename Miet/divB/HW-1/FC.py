
n = int(input())
x = [0 for _ in range(n)]
h = x.copy()
for i in range(n):
	x[i], h[i] = map(int, input().split())
ans = 2 if n > 2 else n
delta = 0
for i in range(1, n - 1):
	l = x[i - 1] + delta
	r = x[i + 1]
	delta = 0
	if x[i] - h[i] > l:
		ans += 1
	elif x[i] + h[i] < r:
		ans += 1
		delta = h[i]
print(ans)
