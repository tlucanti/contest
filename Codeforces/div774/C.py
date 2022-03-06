# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-04 18:30:47
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-04 19:15:34

def inp():
	return list(map(int, input().split()))

fac = [
	6,
	24,
	120,
	720,
	5040,
	40320,
	362880,
	3628800,
	39916800,
	479001600,
	6227020800,
	87178291200,
]

def next(a, mx=2):
	a[-1] += 1
	for i in range(len(a) - 1, -1, -1):
		if a[i] == mx:
			a[i] = 0
			if i == 0:
				return True
			a[i - 1] += 1
	return False


def dot(a, b):
	s = 0
	for q, w in zip(a, b):
		s += q * w
	return s


_It = int(input())
for _ in range(_It):
	n = int(input())
	ans = bin(n).count('1')
	mask = [0] * 13
	while True:
		if next(mask):
			break
		dt = dot(mask, fac)
		if dt > n:
			continue
		ans = min(sum(mask) + bin(n - dt).count('1'), ans)
	print(ans)
