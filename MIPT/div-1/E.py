##
#	Author:		antikostya
#	Created:	2021-09-20 21:18:45
#	Modified:	2021-09-20 21:31:36
##

from math import *

EPS = 1e-8

s, r, n, z = input().split()
s = float(s)
r = float(r)
n = int(n)
z = int(z)

f = s / r
if f < 1 - EPS:
	m = min(0, n)
elif f < 2 - EPS:
	m = min(1, n)
elif f < 1 + 2 * sqrt(3) / 3 - EPS:
	m = min(2, n)
elif f < 1 + sqrt(2) - EPS:
	m = min(3, n)
elif f < 1 + sqrt(2 * (1 + 1/sqrt(5))) - EPS:
	m = min(4, n)
elif f < 3 - EPS:
	m = min(5, n)
else:
	m = n

ans = 0
S = pi * r * r
s = pi * s * s * z / 100
for i in range(1, m + 1):
	if S * i < s - EPS:
		ans += 1
print(ans)
