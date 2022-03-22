# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-06 12:52:19
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-06 13:01:15

def inp():
	return list(map(int, input().split()))


_It = int(input())
for _ in range(_It):
	n = int(input())
	a = inp()
	if not 0 in a:
		print(0)
	else:
		l = a.index(0)
		r = len(a) - a[::-1].index(0) - 1
		print(r - l + 2)
