##
#	Author:		antikostya
#	Created:	2021-11-23 17:50:31
#	Modified:	2021-11-23 19:22:02
##

def inp():
	return list(map(int, input().split()))

for _ in range(int(input())):
	n = int(input())
	a = []
	for i in range(int(input())):
		_a, _b = inp()
		a.append((_a, _b, i))
	a.sort(key=lambda x: x[0])
	a.sort(key=lambda x: x[1])
	for i in range(n)
