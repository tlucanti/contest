##
#	Author:		antikostya
#	Created:	2021-11-02 17:33:04
#	Modified:	2021-11-02 18:58:38
##

for _t in range(int(input())):
	n, m = map(int, input().split())
	n -= 1
	m -= 1
	s = input()
	c = [0, 0]
	l, r, u, d = 0, 0, 0, 0
	ans = [1, 1]
	for i in range(len(s)):
		if s[i] == 'L':
			c[0] -= 1
		elif s[i] == 'R':
			c[0] += 1
		elif s[i] == 'U':
			c[1] += 1
		else:
			c[1] -= 1
		l = min(l, c[0])
		r = max(r, c[0])
		u = max(u, c[1])
		d = min(d, c[1])
		# print([l, r, u, d])
		if r - l > m or u - d > n:
			break
		ans = [1 - l, 1 + u]
	print(ans[1], ans[0])
