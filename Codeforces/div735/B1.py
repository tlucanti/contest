
for t in range(int(input())):
	n, k = map(int, input().split())
	ar = list(map(int, input().split()))
	a = [(ar[i], i+1) for i in range(n)]
	a.sort(key=lambda x: x[1], reverse=True)
	a.sort(key=lambda x: x[0])
	# print(a)

	m = None
	for i in range(n-1):
		mi = (a[i][1]) * (a[i + 1][1]) - k * (a[i][0] | a[i + 1][0])
		if m is None:
			m = mi
		else:
			m = max(m, mi)
	print(m)

