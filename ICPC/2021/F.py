##
#	Author:		antikostya
#	Created:	2021-12-19 11:22:25
#	Modified:	2021-12-19 12:00:28
##

n = int(input())
if n < 4:
	print(-1)
	exit(0)
print(n + 1)
for i in range(n - 2):
	print(i + 1, i + 2)
print(n - 1, 1)
print(n, 1)
print(n, n - 1)
