# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-22 17:33:58
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-22 17:57:10

def inp():
	return list(map(int, input().split()))


for _ in range(int(input())):
	n, b, x, y = inp()
	s = 0
	last = 0
	for i in range(n):
		if last + x <= b:
			last += x
			s += last
		else:
			last -= y
			s += last
	print(s)
