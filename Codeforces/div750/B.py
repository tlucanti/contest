##
#	Author:		antikostya
#	Created:	2021-10-24 12:33:40
#	Modified:	2021-10-24 13:48:35
##

from math import factorial as f


def cnk(n, k):
	return f(n) // (f(k) * f(n - k))


for _ in range(int(input())):
	n = int(input())
	s = list(map(int, input().split()))
	z = s.count(0)
	o = s.count(1)
	sm = sum(s)
	ans = 0
	for i in range(0, z + 1):
		ans += cnk(z, i)
	print(ans * o)
