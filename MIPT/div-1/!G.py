##
#	Author:		antikostya
#	Created:	2021-09-20 20:21:19
#	Modified:	2021-09-20 20:37:38
##

N, R = map(int, input().split())
lake = 0
for i in range(n):
	_, r = map(int, input().split())
	if (i == n-1):
		ans = min(R*n, lake)
	lake += r

print(min(R * n, lake))
