##
#	Author:		kostya
#	Created:	2021-10-10 15:42:29
#	Modified:	2021-10-10 16:10:50
##

for _ in range(int(input())):
	n, m = map(int, input().split())
	i = 0
	at = [0] * n
	_ar = list(map(int, input().split()))
	for i in range(n):
		at[_ar[i] - 1] = i
	ptr = 0
	gu = list(map(int, input().split()))
	for i in range(m):
		g = at[gu[i] - 1]
		if ptr <= g:
			print(g - ptr, end=' ')
		else:
			print(n - ptr + g, end=' ')
		ptr = g
	print()
