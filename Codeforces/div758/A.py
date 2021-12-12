##
#	Author:		antikostya
#	Created:	2021-12-11 13:05:10
#	Modified:	2021-12-11 13:11:23
##

def inp():
	return list(map(int, input().split()))

for t in range(int(input())):
	n = int(input())
	print(*list(range(2, n + 2)))
