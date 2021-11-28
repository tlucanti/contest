##
#	Author:		antikostya
#	Created:	2021-11-25 17:27:49
#	Modified:	2021-11-25 18:21:02
##


def inp():
	return list(map(int, input().split()))

for _ in range(int(input())):
	n = int(input())
	a = inp()
	if a[0] != n - 1 and a[-1] != n - 1:
		print(-1)
		continue
	if a[0] == n - 1:
		a = a[1:] + a[0]
	one = a.index(1)
	ans = a[:one][::-1] + a[one:][::-1]
	print(ans)
