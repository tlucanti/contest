##
#	Author:		antikostya
#	Created:	2021-11-26 13:58:17
#	Modified:	2021-11-26 14:43:34
##

def inp():
	return list(map(int, input().split()))

_t = int(input())
for _ in range(_t):
	n = int(input())
	a = inp()
	a = [(a[i], i + 1) for i in range(n)]
	a.sort(reverse=True, key=lambda x: x[0])
	ans = 0
	for i in range(n):
		ans += a[i][0] * (i//2 + 1) * 2
	print(ans)
	path = [0] * (n + 1)
	for i in range(1, n + 1):
		path[a[i - 1][1]] = (i + 1) // 2 * (i % 2 * 2 - 1)
	print(*path)
