# -*- coding: utf-8 -*-
# @Author: tlucanti
# @Date:   2022-03-20 14:32:18
# @Last Modified by:   tlucanti
# @Last Modified time: 2022-03-20 15:50:06

import bisect

def inp():
	return list(map(int, input().split()))


_It = int(input())
for _ in range(_It):
	n = int(input())
	a = inp()
	a.sort()
	s = sum(a)
	b = [s]
	ok = True
	while len(b) > 0:
		if b[-1] < a[-1]:
			ok = False
			break
		while len(a) != 0 and len(b) !=0 and b[-1] == a[-1]:
			del b[-1]
			del a[-1]
		if len(b) == 0:
			break
		if b[-1] > 1:
			p1 = b[-1] // 2
			p2 = b[-1] - p1
			del b[-1]
			bisect.insort(b, p1)
			bisect.insort(b, p2)
	print ('YES' if ok else 'NO')



# _It = int(input())
# for _ in range(_It):
# 	n = int(input())
# 	a = inp()
# 	a.sort()
# 	ok = True
# 	while len(a) > 1:
# 		print(a)
# 		if a[1] - a[0] > 1:
# 			ok = False
# 			break
# 		else:
# 			piece = a[0] + a[1]
# 			del a[0]
# 			del a[0]
# 			bisect.insort(a, piece)
# 	print ('YES' if ok else 'NO')
