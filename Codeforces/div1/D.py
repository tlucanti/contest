
for t in range(int(input())):
	n = int(input())
	s = list(map(int, input().split()))
	sm = sum(s)
	st = dict()
	for i in s:
		st[i] = st.get(i, 0) + 1
	f = 1
	for i in range(n + 2):
		x = s[i]
		S = sm - s[i]
		if S % 2:
			continue
		S //= 2
		if x == S:
			if st[x] < 2:
				continue
		if st.get(S, 0) > 0:
			s.remove(x)
			s.remove(S)
			print(*s)
			f = 0
			break
	if f:
		print(-1)
