##
#	Author:		antikostya
#	Created:	2022-01-03 17:29:23
#	Modified:	2022-01-03 18:25:22
##

def inp():
	return list(map(int, input().split()))

for _ in range(int(input())):
	n = int(input())
	it = dict()
	min_l = None
	lc = None
	max_r = None
	rc = None
	for i in range(n):
		l, r, c = inp()
		if min_l is None or l < min_l:
			min_l = l
			lc = c
		elif l == min_l:
			lc = min(c, lc)

		if max_r is None or r > max_r:
			max_r = r
			rc = c
		elif r == max_r:
			rc = min(c, rc)

		p = (l, r)
		if p in it:
			it[p] = min(it[p], c)
		else:
			it[p] = c
		m1 = it.get((min_l, max_r), None)
		if m1 is None:
			print(lc + rc)
		else:
			print(min(m1, lc + rc))
