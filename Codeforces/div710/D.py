
for t in range(int(input())):
	n = int(input())
	s = list(map(int, input().split()))
	d = dict()
	for i in range(n):
		d[s[i]] = d.get(s[i], 0) + 1
	m = max(d.values())
	if m <= n // 2:
		print(n % 2)
	else:
		print(2 * m - n)
