##
#	Author:		antikostya
#	Created:	2021-11-02 19:02:11
#	Modified:	2021-11-02 19:14:24
##

for _t in range(int(input())):
	_s = input()
	n, m = map(int, input().split())
	a = [0] * n
	b = [0] * n
	for i in range(n):
		a[i], b[i] = map(int, input().split())
	sa = sum(a)
	sb = sum(b)
	d = 0
	for i in range(n):
		d += s
