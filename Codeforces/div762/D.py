##
#	Author:		antikostya
#	Created:	2021-12-20 18:10:51
#	Modified:	2021-12-20 18:53:32
##

def inp():
	return list(map(int, input().split()))

def m2(a):
	m = a[0]
	m1 = a[1]
	idx = [0, 1]
	if m1 > m:
		m, m1 = m1, m
		idx = idx[::-1]
	for i in range(2, len(a)):
		if a[i] > m:
			m, m1 = a[i], m
			idx = [i, idx[0]]
		elif a[i] > m1:
			m1 = a[i]
			idx[1] = i
	return m1

_T = int(input())
for _t in range(_T):
	input()
	m, n = inp()
	cols = [inp() for i in range(m)]
	rows = [[0] * m for i in range(n)]
	for i in range(n):
		for j in range(m):
			rows[i][j] = cols[j][i]
	maxes = [max(a) for a in rows]
	m2s = list(map(m2, cols))
	# print(m2s)
	print(min(min(maxes), max(m2s)))
	# print(rows)
	# print(m2s)
