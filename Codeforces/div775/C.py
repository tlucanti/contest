# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-06 12:52:19
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-06 13:55:18

import itertools


def inp():
	return list(map(int, input().split()))


n, m = inp()
Map = [inp() for _ in range(n)]
dic = dict()
for x in range(m):
	for y in range(n):
		c = Map[y][x]
		if c in dic:
			dic[c].append((y, x))
		else:
			dic[c] = [(y, x)]

ans = 0
for c in dic:
	a = dic[c]
	y = [coord[0] for coord in a]
	x = [coord[1] for coord in a]
	y.sort()
	x.sort()
	cumx = list(itertools.accumulate(x))
	cumy = list(itertools.accumulate(y))
	for i in range(len(a) - 2, -1, -1):
		ans += x[i + 1] * (i + 1) - cumx[i]
		ans += y[i + 1] * (i + 1) - cumy[i]
print(ans)
