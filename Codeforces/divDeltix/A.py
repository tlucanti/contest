##
#	Author:		antikostya
#	Created:	2021-11-28 17:20:23
#	Modified:	2021-11-28 17:47:40
##

def inp():
	return list(map(int, input().split()))

_t = int(input())
for _ in range(_t):
	n = int(input())
	a = inp()
	twos = 0
	for i in range(n):
		while a[i] % 2 == 0:
			twos += 1
			a[i] //= 2
	a.sort()
	a[i] *= pow(2, twos)
	print(sum(a))
