##
#	Author:		antikostya
#	Created:	2021-11-23 17:49:51
#	Modified:	2021-11-23 18:05:12
##

for _ in range(int(input())):
	a, b = map(int, input().split())
	if a == 1 and b == 1:
		print(0)
	else:
		print(min(a, b, 2))
