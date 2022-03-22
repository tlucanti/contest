# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-20 14:32:18
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-20 14:43:18

def inp():
	return list(map(int, input().split()))


_It = int(input())
for _ in range(_It):
	n = int(input())
	a = inp()
	cost = a[0] + a[1]
	for i in range(n - 1):
		cost = min(cost, a[i] + a[i + 1])
	for i in range(n):
		for j in range(n):
			a[i], a[j] = a[j], a[i]
			if i >= 1:
				cost = max(cost, a[i - 1] + a[i])
			if i < n - 1:
				cost = max(cost, a[i] + a[i + 1])
			if j >= 1:
				cost = max(cost, a[j - 1] + a[j])
			if j < n - 1:
				cost = max(cost, a[j] + a[j + 1])
			a[i], a[j] = a[j], a[i]
	print(cost)

