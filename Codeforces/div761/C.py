##
#	Author:		antikostya
#	Created:	2021-12-16 16:30:23
#	Modified:	2021-12-16 17:56:36
##

def inp():
	return list(map(int, input().split()))

_T = int(input())
for _t in range(_T):
	n = int(input())
	a = inp()
	ans = 0
	
	d = dict()
	for i in range(n):
		d[a[i]] = d.get(a[i], 0) + 1

	left = []
	for i in range(1, n + 1):
		if i in d:
			d[i] -= 1
			if d[i] == 0:
				del d[i]
		else:
			left.append(i)
	# print('left:', left)
	b = []
	for i in d:
		b += [(i - 1) // 2] * d[i]
	b.sort()
	# print('b:', b)
	n = len(b)
	ans = 0
	for i in range(n):
		if b[i] < left[i]:
			ans = -1
			break
		ans += 1
	print(ans)
