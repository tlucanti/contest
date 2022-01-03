##
#	Author:		antikostya
#	Created:	2022-01-03 17:29:23
#	Modified:	2022-01-03 17:48:49
##

def inp():
	return list(map(int, input().split()))

for i in range(int(input())):
	n, k = inp()
	if n >= k * 2 - 1:
		mat = [list('.' * n) for _ in range(n)]
		for i in range(k):
			mat[i * 2][i * 2] = 'R'
		for i in range(n):
			print(''.join(mat[i]))
	else:
		print(-1)
