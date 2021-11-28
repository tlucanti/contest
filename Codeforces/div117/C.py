##
#	Author:		antikostya
#	Created:	2021-11-22 12:27:48
#	Modified:	2021-11-24 19:50:38
##

import math

def inp():
	return list(map(int, input().split()))

def rng(n):
	return n * (n + 1) // 2

def rng2(n, k):
	if n <= 0:
		return 0
	elif n >= k:
		return rng(k)
	return n * (k + 1) - n * (n + 1) // 2

def solve(k, x):
	if rng(k) + rng(k - 1) <= x:
		return 2 * k - 1
	elif rng(k) < x:
		_x = x
		x -= rng(k)
		ans = k + math.ceil(0.5 * (2*k - 1 - math.sqrt(pow(2*k - 1, 2) - 8*x)))
		for ans in range(max(ans - 10, 0), ans + 10):
			if rng(k) + rng2(ans - k, k - 1) >= _x:
				return ans
	else:
		ans = math.ceil(0.5 * (-1 + math.sqrt(1 + 8*x)))
		for ans in range(max(ans - 10, 0), ans + 10):
			if rng(ans) >= x:
				return ans

for _ in range(int(input())):
	k, x = inp()
	print(solve(k, x))



