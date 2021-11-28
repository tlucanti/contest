##
#	Author:		antikostya
#	Created:	2021-11-25 17:27:49
#	Modified:	2021-11-25 17:45:30
##


def inp():
	return list(map(int, input().split()))

for _ in range(int(input())):
	a, b = inp()
	teams = (a + b) // 4
	teams = min(teams, a, b)
	print(teams)
