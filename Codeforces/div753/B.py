##
#	Author:		antikostya
#	Created:	2021-11-02 17:33:04
#	Modified:	2021-11-02 17:57:19
##

def rsum(a, b, k):
	n = 1 + (b - a) // k
	return a * n + k * n * (n - 1) // 2

for _t in range(int(input())):
	x, n = map(int, input().split())
	if (x % 2 == 0):
		print(
			rsum(2, n, 4)
			+ rsum(3, n, 4)
			- rsum(1, n, 4)
			- rsum(4, n, 4)
			+ x
		)
	else:
		print(
			rsum(1, n, 4)
			+ rsum(4, n, 4)
			- rsum(2, n, 4)
			- rsum(3, n, 4)
			+ x
		)
