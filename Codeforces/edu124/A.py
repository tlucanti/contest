# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-10 17:26:31
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-10 17:48:07

def inp():
	return list(map(int, input().split()))


def who(a, b):
	if (a + b) % 2:
		return min(a, b)
	return max(a, b)


def solve(n):
	a = list(range(1, 2 ** n + 1))
	while True:
		if len(a) == 1:
			return a[0]
		b = []
		for i in range(0, len(a), 2):
			b.append(who(a[i], a[i + 1]))
		a = b


for t in range(int(input())):
	n = int(input())
	print(2 ** n - 1)

