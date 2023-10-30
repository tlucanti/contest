##
#	Author:		kostya
#	Created:	2021-09-03 23:29:01
#	Modified:	2021-09-03 23:29:07
##

n, i, j = map(int, input().split())
i, j = min(i, j), max(i, j)
print(min(abs(j - i - 1), abs(n + i - j - 1)))
