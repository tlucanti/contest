# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-06 12:52:19
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-06 14:58:47

import itertools


def inp():
	return list(map(int, input().split()))


def find(n):
	d = 1
	u = d * n
	while u < c:
		hi = min(c, u + d)
		cb = cumbar[hi] - cumbar[u - 1]
		if bar[d] and cb:
			return True
		d += 1
		u = d * n
	return False


_It = int(input())
for _ in range(_It):
	n, c = inp()
	a = inp()
	if not 1 in a:
		print('No')
		continue
	a.sort()
	bar = [0] * (c + 1)
	for i in a:
		bar[i] = 1
	cumbar = list(itertools.accumulate(bar))
	ok = [0] * (c + 1)
	for i in range(1, c + 1):
		ok[i] = int(find(i))
	a = set(a)
	ans = 'Yes'
	for i in range(1, c + 1):
		if ok[i] and i not in a:
			ans = 'No'
			break
	print(ans)
