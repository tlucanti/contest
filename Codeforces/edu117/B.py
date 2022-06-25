##
#	Author:		antikostya
#	Created:	2021-11-22 12:27:48
#	Modified:	2021-11-22 12:54:23
##

for _ in range(int(input())):
	n, a, b = map(int, input().split())
	ar = list(range(1, n + 1))
	ar = ar[::-1]
	if min(ar[:n // 2]) == a and max(ar[n // 2:]) == b:
		print(*ar)
		continue
	ar = ar[::-1]
	ar[a - 1], ar[b - 1] = ar[b - 1], ar[a - 1]
	ar = ar[::-1]
	if min(ar[:n // 2]) == a and max(ar[n // 2:]) == b:
		print(*ar)
	else:
		print(-1)
