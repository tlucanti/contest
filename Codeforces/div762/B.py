##
#	Author:		antikostya
#	Created:	2021-12-20 17:31:24
#	Modified:	2021-12-20 17:41:26
##

def inp():
	return list(map(int, input().split()))

_T = int(input())
for _t in range(_T):
	n = int(input())
	ans = 0
	i = 1
	s = set()
	while i * i <= n:
		s.add(i * i)
		ans += 1
		i += 1
	i = 1
	while i * i * i <= n:
		if i * i * i in s:
			i += 1
			continue
		ans += 1
		i += 1
	print(ans)
