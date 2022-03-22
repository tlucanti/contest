# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-20 14:32:18
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-20 14:52:28

def inp():
	return list(map(int, input().split()))


_It = int(input())
for _ in range(_It):
	a = input()
	d = dict()
	for i in a:
		d[i] = d.get(i, 0) + 1
	for i in range(len(a)):
		if d[a[i]] >= 2:
			d[a[i]] -= 1
		else:
			print(a[i:])
			break
