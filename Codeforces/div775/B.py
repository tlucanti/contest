# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-06 12:52:19
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-06 13:32:07

def inp():
	return list(map(int, input().split()))


_It = int(input())
for _ in range(_It):
	n = int(input())
	a = inp()
	a.sort()
	sm = sum(a)
	if sm == 0:
		print(0)
	elif a[-1] > sm - a[-1]:
		rem = 2 * a[-1] - sm
		print(rem)
	else:
		print(1)
