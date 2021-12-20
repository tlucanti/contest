##
#	Author:		antikostya
#	Created:	2021-12-16 16:30:23
#	Modified:	2021-12-16 16:54:10
##

import math

def inp():
	return list(map(int, input().split()))

_T = int(input())
for _t in range(_T):
	n = int(input())
	c = 1
	for a in range(2, n):
		b = n - a - c
		if a != b and b != c and a != c and math.gcd(a, b) == c:
			print(a, b, c)
			break
	# ans = []
	# for a in range(1, n):
	# 	for b in range(1, n):
	# 		c = n - a - b
	# 		if math.gcd(a, b) == c and a != b and b != c and a != c:
	# 			ans.append((a, b, c))
	# print(*ans)
