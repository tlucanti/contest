# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-04 18:30:47
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-04 18:50:10


def inp():
	return list(map(int, input().split()))


_It = int(input())
for _ in range(_It):
	n = int(input())
	a = inp()
	a.sort()
	l = 0
	r = n
	ok = False
	lsum = a[0]
	rsum = 0
	while l < r:
		if lsum < rsum:
			ok = True
			break
		l += 1
		lsum += a[l]
		r -= 1
		rsum += a[r]
	print ('YES' if ok else 'NO')

