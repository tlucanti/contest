##
#	Author:		antikostya
#	Created:	2021-10-24 12:33:40
#	Modified:	2021-10-24 13:39:00
##

for _ in range(int(input())):
	a, b, c = map(int, input().split())
	a = min(10 + a % 10, a)
	b = min(10 + b % 10, b)
	c = min(10 + c % 10, c)
	m = a + b * 2 + c * 3
	for ia in range(a + 1):
		for ib in range(b + 1):
			for ic in range(c + 1):
				l = ia + ib * 2 + ic * 3
				r = (a - ia) + (b - ib) * 2 + (c - ic) * 3
				m = min(m, abs(l - r))
	print(m)
