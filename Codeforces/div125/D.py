# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-22 17:33:58
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-22 19:29:52

def inp():
	return list(map(int, input().split()))

class war:
	def __init__(self, c, d, h):
		self.c = c
		self.d = d
		self.h = h

	def __repr__(self):
		return '{' f'c:{self.c}, d:{self.d}, h:{self.h}' '}'


n, C = inp()
W = []
for i in range(n):
	W.append(war(*inp()))

for _ in range(int(input())):
	d, h = inp()
	c = W[0].c * h
	wi = 0
	ni = 0
	for w in W:
		ni = h * d // (w.d * w.h)
		if ni * w.d * w.h <= h * d:
			ni += 1
		ci = w.c * ni
		if ci < c:
			c = ci
	if c <= C:
		print(c)
	else:
		print(-1)
