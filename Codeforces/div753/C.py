##
#	Author:		antikostya
#	Created:	2021-11-02 17:33:04
#	Modified:	2021-11-02 18:12:38
##

for _t in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	a.sort()
	ans = a[0]
	s = a[0]
	g = -a[0]
	for i in range(1, n):
		s = a[i] + g
		g -= s
		ans = max(ans, s)
	print(ans)
