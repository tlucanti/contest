
from math import factorial as f

def cnk(n, k):
	if n < k:
		return 0
	return f(n) //(f(k) * f(n - k))

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	a = [a[i] - i for i in range(n)]
	d = dict()
	for i in a:
		d[i] = d.get(i, 0) + 1
	ans = 0
	for i in d:
		ans += cnk(d[i], 2)
	print(ans)
