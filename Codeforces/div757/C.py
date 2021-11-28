##
#	Author:		antikostya
#	Created:	2021-11-26 13:58:17
#	Modified:	2021-11-26 16:07:17
##

mod = 1000000007

def inp():
	return list(map(int, input().split()))

_t = int(input())
for _ in range(_t):
	n, m = inp()
	bit = 0
	for i in range(m):
		l, r, x = inp()
		bit |= x
	ans = bit * pow(2, n - 1, mod=mod)
	print(ans % mod)

