for i in range(int(input())):
	input()
	k, n, m = map(int, input().split())
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	ai = 0
	bi = 0
	ans = []
	for i in range(m + n):
		if ai < n and a[ai] == 0:
			k += 1
			ai += 1
			ans.append(0)
		elif bi < m and b[bi] == 0:
			k += 1
			bi += 1
			ans.append(0)
		else:
			if ai < n and bi < m:
				mi = min(a[ai], b[bi])
			elif ai < n:
				mi = a[ai]
			else:
				mi = b[bi]
			if mi > k:
				ans = [-1]
				break
			if ai < n and a[ai] == mi:
				ai += 1
			else:
				bi += 1
			ans.append(mi)
	print(*ans)
