##
#	Author:		antikostya
#	Created:	2021-12-18 18:32:04
#	Modified:	2021-12-18 18:41:47
##

def inp():
	return list(map(int, input().split()))

_T = int(input())
for _t in range(_T):
	s = input()
	if s.count('N') == 1:
		print('NO')
	else:
		print('YES')
