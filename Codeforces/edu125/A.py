# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-22 17:33:58
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-22 17:52:42

def inp():
	return list(map(int, input().split()))


def is_sq(n):
	i = 2
	while i * i <= n:
		if i * i == n:
			return True
		i += 1
	return False


_It = int(input())
for _ in range(_It):
	x, y = inp()
	if x == 0 and y == 0:
		print(0)
	elif x == 0 or y == 0:
		print(1)
	elif is_sq(x * x + y * y):
		print(1)
	else:
		print(2)
