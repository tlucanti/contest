##
#	Author:		antikostya
#	Created:	2021-12-20 17:31:17
#	Modified:	2021-12-20 17:37:10
##

def inp():
	return list(map(int, input().split()))

_T = int(input())
for _t in range(_T):
	s = input()
	if len(s) % 2:
		print('NO')
	elif s[:len(s) // 2] * 2 == s:
		print('YES')
	else:
		print('NO')
