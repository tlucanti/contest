##
#	Author:		antikostya
#	Created:	2021-12-12 17:57:48
#	Modified:	2021-12-12 18:27:25
##

def inp():
	return list(map(int, input().split()))

_T = int(input())
for _t in range(_T):
	n = int(input())
	a = inp()
	k = 0
	m = max(a)
	x = a[-1]
	for i in range(n - 1, -1, -1):
		if x == m:
			break
		if a[i] > x:
			k += 1
			x = a[i]
	print(k)

