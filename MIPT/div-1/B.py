##
#	Author:		antikostya
#	Created:	2021-09-20 17:46:25
#	Modified:	2021-09-20 18:09:32
##

n, m = map(int, input().split())
if m < n - 1 or (m > 2*n - 3):# and n > 2):
	print(-1)
	exit(0)

it = 0
for i in range(1, n):
	if it >= m:
		break
	print(1, i + 1)
	it += 1
for i in range(n - 1, -1, -1):
	if it >= m:
		break
	print(n, i)
	it += 1
