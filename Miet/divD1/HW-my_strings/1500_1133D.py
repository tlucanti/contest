##
#	Author:		antikostya
#	Created:	2021-11-28 20:50:29
#	Modified:	2021-11-28 21:13:42
##

import math

def inp():
	return list(map(int, input().split()))

def frac(a, b):
	gcd = math.gcd(abs(a), abs(b))
	if a * b < 0:
		return (abs(a) // gcd, -abs(b) // gcd)
	else:
		return (abs(a) // gcd, abs(b) // gcd)


n = int(input())
ar, br = inp(), inp()
d = {(0, 0): 0}
zeros = 0
for i in range(n):
	a, b = ar[i], br[i]
	if a == 0:
		if b == 0:
			zeros += 1
		continue
	fr = frac(-b, a)
	d[fr] = d.get(fr, 0) + 1


print(max(d.values()) + zeros)
