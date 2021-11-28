##
#	Author:		antikostya
#	Created:	2021-11-26 13:58:17
#	Modified:	2021-11-26 14:17:47
##

def inp():
	return list(map(int, input().split()))

_t = int(input())
for _ in range(_t):
	n, l, r, k = inp()
	a = inp()
	a.sort()
	ans = 0
	cost = 0
	for i in range(n):
		if r >= a[i] >= l:
			cost += a[i]
			if cost > k:
				break
			ans += 1
	print(ans)
