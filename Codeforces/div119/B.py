##
#	Author:		antikostya
#	Created:	2021-12-18 18:32:04
#	Modified:	2021-12-18 18:59:58
##

def inp():
	return list(map(int, input().split()))

_T = int(input())
for _t in range(_T):
	w, h = inp()
	x1 = inp()[1:]
	x2 = inp()[1:]
	x3 = inp()[1:]
	x4 = inp()[1:]
	s1 = abs(x1[-1] - x1[0]) * h
	s2 = abs(x3[-1] - x3[0]) * w
	s3 = abs(x2[-1] - x2[0]) * h
	s4 = abs(x4[-1] - x4[0]) * w
	print(max(s1, s2, s3, s4))
