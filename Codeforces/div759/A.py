##
#	Author:		antikostya
#	Created:	2021-12-12 17:57:48
#	Modified:	2021-12-12 18:18:35
##

def inp():
	return list(map(int, input().split()))

_T = int(input())
for _t in range(_T):
	n = int(input())
	a = inp()
	s = 1
	if a[0] == 1:
		s += 1
	for i in range(1, n):
		if a[i] == 0 and a[i - 1] == 0:
			s = -1
			break
		elif a[i] == 1 and a[i - 1] == 1:
			s += 5
		elif a[i] == 1:
			s += 1
	print(s)
